######################################################################
# avr2.py
#
# This script demonstrates how to connect the simulavr simulator
# with python. The script is intended to be used in conjunction with
# avr-gdb in a debugging context.  GDB is used to step and trace
# the code through the simulator, the simulator is provided though
# the simulavr library (compiled using SWIG), and the ui is provided
# through this file.
#
# Startup should folllow this flow:
# 1. User starts avr-gdb
# 2. From within gdb, shell commands are used to start this script
# 3. This script starts simulavr in debug server mode
# 4. gdb connects with simulavr
# 5. Code execution begins under direction of gdb.  While running,
#    the ui updates based on the simulator state
#
#===================================================================
# Copyright (C) 2019, Arizona State University
# All rights reserved
#
# Author: Doug Sandy

# Imports
from sys import argv
from threading import *
from tkinter import *
import pysimulavr

# Global variables
slider_value = 256        # the value of the analog pin as
                          # controlled by the ui.
previous_temperature = 0  # the previous temperature that was sent
                          # to the simulator from the ui
sim = None                # the simulation object (wrapper for simulavr)
dev = None                # the device object that will be simulated
ui = None                 # the user interface
a0 = None


#===================================================================
# class UiThread
#
# This thread initializes and runs the UI.  A separate thread is
# required because the simulator both the simulator step function
# and the Tkiner mainloop are blocking.
#
class UiThread(Thread):

  #=================================================================
  # UiThread.__init__
  #
  # Constructor - initialize the state, and start the thread
  def __init__(self):
    Thread.__init__(self)
    self.root = None
    self.window = None
    self.portBValue = -1
    self.ddrbValue = -1
    self.start()


  #=================================================================
  # UiThread.callback
  #
  # This callback function is invoked if there is a request to close
  # the simulator window.
  def callback(self):
      self.root.quit()   # stop the Tcl interpreter

  #=================================================================
  # UiThread.run
  #
  # create the main frame and window and begin execution of the
  # user interface.  This function will not exit as long as
  # the UI is running.
  def run(self):
    # create the window and run the tkinter mainloop
    self.root= Tk()
    self.root.protocol("WM_DELETE_WINDOW", self.callback)
    self.root.geometry("300x250")
    self.window = Window(self.root)
    self.root.mainloop()

  #=================================================================
  # UiThread.setLedColor
  #
  # Change the led color if and only if the hardware state has changed
  # since the LED color was last updateed.
  #
  def setLedColor(self, portbValue, ddrbValue):
    # if the window is not yet created, just return
    if self.window == None: return

    # if the hardware state has not changed, just return
    if (self.portBValue == portbValue) and (self.ddrbValue == ddrbValue): return

    # update the LED state based on the port direction and value
    if (ddrbValue != 0):
      # port set to output - set the color based on the value of portb
      if (portbValue != 0):
        # led is driven on
        self.window.setLedColor("green")
      else:
        # led is driven off
        self.window.setLedColor("black")
    else:
      # port is set to input - set the color based on the pullup value
      if (portbValue != 0):
        # led will be on due to pullup
        self.window.setLedColor("green")
      else:
        # led state is not driven
        self.window.setLedColor("grey")
    self.portBValue = portbValue
    self.ddrbValue = ddrbValue


#===================================================================
# class Window
#
# This class implements the UI window and controls.
#
class Window(Frame):
  #=================================================================
  # Window.__init__
  #
  # Constructor - initialize the state of the UI window.
  def __init__(self, master = None):
    Frame.__init__(self,master)
    self.master = master
    self.init_widgets()   # place control widgets on the window


  #=================================================================
  # Window.init_widgets
  #
  # Place control widgets on the window and configure them.
  #
  def init_widgets(self):
    # set the title of our master window
    self.master.title("Simulavr")
    self.pack(fill=BOTH, expand=1)

    # add a button to represent the LED.  The button will be
    # disabled by default.
    self.button = Button(self, text="    ")
    self.button.configure(state="disabled")
    self.button.place(x=100, y=100)

    # add a slider to control the analog input value
    self.slider = Scale(self, from_=1023, to=0,length=200, command=self.sliderCommand)
    self.slider.set(256)
    self.slider.place(x=200, y=10)
    self.update()


  # =================================================================
  # Window.sliderCommand
  #
  # This function is called whenever the slider widget is moved.
  # The new value is buffered in teh tempearture global variable
  # so that the analog input pin will be updated during the next
  # simulation step.
  #
  def sliderCommand(self, newval):
    global slider_value
    global a0
    slider_value = float(newval)
    a0.SetAnalogValue(5.0 * slider_value / 1024.0)


  #=================================================================
  # Window.setLedColor
  #
  # Set the color of the LED button to the specified value and wait
  # for the color to change on the screen.
  #
  def setLedColor(self, color):
    # set the led color and wait for it to update
    self.button.configure(bg=color)
    self.update()


# =================================================================
# Class XPin
#
# This class implements a wrapper for simulator's device pins.
# this class is derived from the Simulavr Pin Class.
#
# This code was based largely on the SIMULAVR python example code
#
class XPin(pysimulavr.Pin):
  #=================================================================
  # XPin.__init__
  #
  # Constructor - initialize the pin object and connect an external net to
  # the pin.
  #
  def __init__(self, dev, name, state = None):
    pysimulavr.Pin.__init__(self)
    self.dev=dev
    self.name = name
    devpin = dev.GetPin(name)

    if state is not None: self.SetPin(state)

    # add the connecting net
    self.__net = pysimulavr.Net()
    self.__net.Add(self)
    self.__net.Add(devpin)


# =================================================================
# Class SimulavrDebugAdapter
#
# This class implements a wrapper for simulator's simulation
class SimulavrDebugAdapter(object):
  DEFAULT_CLOCK_SETTING = 63  # 63ns = 15.87MHz

  #=================================================================
  # SimulavrDebugAdapter.loadDevice
  #
  # Create the specific atmega device to simulate and load the
  # specified elf file into the device's memory space.
  #
  # This code was based largely on the SIMULAVR python example code
  #
  def loadDevice(self, t, e):
    # create the simulation system clock
    self.__sc = pysimulavr.SystemClock.Instance()
    self.__sc.ResetClock()
    # creaate the atmega device to simulate
    dev = pysimulavr.AvrFactory.instance().makeDevice(t)
    # loat the program file into device memory
    dev.Load(e)
    # set the system clock frequency, and start the gdb server
    dev.SetClockFreq(self.DEFAULT_CLOCK_SETTING)
    gdbs = pysimulavr.GdbServer(dev,1212,False,True)
    self.__gdbs = gdbs
    self.__sc.Add(gdbs)
    return dev

  #=================================================================
  # SimulavrDebugAdapter.doStep
  #
  # simulate one simulation step.  Note that since the simulation
  # library is written in c, it will block the python interpreter
  # until it returns.
  #
  # This code was based largely on the SIMULAVR python example code
  #
  def doStep(self, stepcount=1):
    while stepcount > 0:
      res = self.__sc.Step()
      if res is not 0: return res
      stepcount -= 1
    return 0


proc, elffile = argv[1].split(":")

# start the GDB Server, Initialize the device, and load the program image
sim = SimulavrDebugAdapter()
dev = sim.loadDevice(proc, elffile)

# apply analog signals to the external pins for the ADC channel and the
# voltage reference
a0 = XPin(dev, "C0", 'a')
aref = XPin(dev, "AREF", 'a')
aref.SetAnalogValue(5.0)
a0.SetAnalogValue(5.0*90.0/120.0)

# open the display window and wait for it to appear
ui = UiThread()

# loop until the simulation is completed by GDB
while True:
  # update the LED color if it has changed
  ui.setLedColor(dev.getRWMem(0x25) & 2, dev.getRWMem(0x24) & 2)

  # update the device temperature if it has changed since last update
  if slider_value != previous_temperature:
    a0.SetAnalogValue(5.0 * slider_value / 1024.0)
    previous_temperature = slider_value

  # step the simulation by one clock
  sim.doStep()

