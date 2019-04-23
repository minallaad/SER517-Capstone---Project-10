'''
    Description: This class represents the actual UI for the application. It consist of the functions for creating
                 the backbone of the UI and adding various components to it. It also has the functionality of updating
                 the UI.
'''

import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import QSplitter, QApplication, QHBoxLayout, QVBoxLayout

import Components.ATMega_PIN_Diagram
import Components.Globalmap
import Components.List_of_Registers
import Components.Register_Values
import Components.stackedWidget
import Components.EEPROM
from simulavr.adaptor import SimulavrAdaptor
from helper import UIHelper
from multiprocessing import Process, Manager




sys.stdout = open('test/logs.log', 'w')

class Landing(QtWidgets.QWidget):

    def __init__(self):
        super(Landing, self).__init__()
        self.Register_Values = None
        self.List_of_Registers = None
        self.PIN_Diagram = None
        self.stackWidget = None
        self.initUI()

    '''
    Description: Function for initializing the UI and setting default properties to it.
    '''
    def initUI(self):
        self.title = "ATMega Simulator"
        self.top = 100
        self.left = 600
        self.width = 1100
        self.height = 800
        self.setWindowTitle(self.title)
        self.setStyleSheet("background-color: white")
        self.window()
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    '''
    Description: Function for creating a window for the UI and adding various components to it. 
    '''
    def window(self):

        # Component for displaying the register values. This is the bottom left component of the UI.
        self.Register_Values = Components.Register_Values.Register_Values().getInstance()

        # Component for displaying the list of register. This is the top left list component of the UI.
        self.List_of_Registers = Components.List_of_Registers.List_of_Registers().getInstance()

        # Component for displaying the microcontroller and the pins.
        self.PIN_Diagram = Components.ATMega_PIN_Diagram.PIN_Diagram()

        self.stackWidget = Components.stackedWidget.stackWidget().getInstance()

        self.splitter = QSplitter(Qt.Vertical)

        self.splitter.addWidget(self.List_of_Registers)
        self.splitter.addWidget(self.Register_Values)
        self.splitter.setSizes([300, 150])

        self.horizontalLayout = QHBoxLayout()

        self.rightFrame = self.PIN_Diagram.getPIN_Digram()

        self.stackWidget.addWidget(self.rightFrame)

        self.horizontalSplitter = QSplitter(Qt.Horizontal)
        self.horizontalLayout.addWidget(self.splitter)
        self.horizontalSplitter.addWidget(self.stackWidget)
        self.horizontalSplitter.setSizes([80, 320])
        self.horizontalSplitter.adjustSize()

        self.titleFont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
        self.Title = QtWidgets.QLabel(self)
        self.Title.setText("ATMega328p Simulator")
        self.Title.setFont(self.titleFont)
        self.Title.setAlignment(Qt.AlignCenter)

        # Associating back button to UI.
        self.backButton = QtWidgets.QPushButton("Back")
        self.backButton.clicked.connect(lambda: self.backClicked())

        self.horizontalLayout.addWidget(self.horizontalSplitter)

        # Displauying the connection status of the simulator.
        self.StatusFont = QtGui.QFont("Helvetica", 10, QtGui.QFont.Bold)
        self.Status = QtWidgets.QLabel(self)
        self.Status.setText(self.getConnectionStatus())
        self.Status.setFont(self.StatusFont)
        self.Status.setStyleSheet('color : green')
        self.Status.setAlignment(Qt.AlignCenter)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.addWidget(self.Title)
        self.verticalLayout.addWidget(self.Status)
        self.verticalLayout.addWidget(self.backButton, 0, Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.setLayout(self.verticalLayout)

    '''
    Description: This function returns the connection status of the simulator.
    '''
    def getConnectionStatus(self):
        return "Connected to Simulavr"

    '''
    Description: Function to create the back button functionality. This button helps in navigation on UI between 
                 various screens. 
    '''
    def backClicked(self):
        UIHelper.UIHelper().refreshItems()
        topWidget = Components.stackedWidget.stackWidget.top
        if topWidget != 0:
            widgetToRemove = Components.stackedWidget.stackWidget.StackWidget.widget(topWidget)
            Components.stackedWidget.stackWidget.decrementTopCount()
            Components.stackedWidget.stackWidget.removeWidget(widgetToRemove)

    '''
    Description: This function updates the values in PORTS, PINS and registers on UI. It fetches the data from global
     map and updates the UI components with the new data.
    '''
    def updateUI(self, sharedMap, sharedMemoryMap):
        while True:

            if sharedMap['refresh_ui_flag']:
                sharedMap['refresh_ui_flag'] = False
                Components.Globalmap.Map.map = sharedMap
                for key, value in sharedMap.items():
                    port = key.split('.')[0]
                    if key in ['PORTB.PORT', 'PORTC.PORT', 'PORTD.PORT']:
                        UIHelper.UIHelper().setPortValues(port, value)
                    if key in ['PORTB.DDR', 'PORTC.DDR', 'PORTD.DDR']:
                        UIHelper.UIHelper().setDdrValues(port, value)
                    if key in ['PORTB.PIN', 'PORTC.PIN', 'PORTD.PIN']:
                        UIHelper.UIHelper().setPinValues(port, value, self.PIN_Diagram)

                if Components.Globalmap.Map.port_clicked != None:
                    self.PIN_Diagram.refreshPortValues(Components.Globalmap.Map.port_clicked)

                if Components.Globalmap.Map.register_clicked != None:
                    if Components.Globalmap.Map.register_clicked_type == 'r':
                        self.PIN_Diagram.refreshLeftPanelRegisterValues(Components.Globalmap.Map.register_clicked)
                    elif Components.Globalmap.Map.register_clicked_type == 'p':
                        self.PIN_Diagram.refreshLeftPanelPortValues(Components.Globalmap.Map.register_clicked)

                if Components.Globalmap.Map.refresh_flag:
                    Components.Globalmap.Map.refresh_flag = False
                    sharedMap['eeprom_address'] = Components.Globalmap.Map.eeprom_address
                    sharedMap['eeprom_update'] = True

                if sharedMap['eeprom_is_updated']:
                    sharedMap['eeprom_is_updated'] = False
                    Components.EEPROM.memoryDump.UpdateEEPROM(sharedMemoryMap)


class UiThread(QThread):

    def __init__(self, ui, sharedMap, sharedMemoryMap):
        QThread.__init__(self)
        self.ui = ui
        self.sharedMap = sharedMap
        self.sharedMemoryMap = sharedMemoryMap

    def run(self):
        self.ui.updateUI(self.sharedMap, self.sharedMemoryMap)


def run(sharedMap, sharedMemoryMap):
    app = QApplication(sys.argv)
    obj = Landing()
    uiThread = UiThread(obj, sharedMap, sharedMemoryMap)
    uiThread.start()
    app.exec_()
    del obj
    del app
            
if __name__ == '__main__':

    manager = Manager()
    sharedMap = manager.dict()
    sharedMemoryMap = manager.dict()

    p = Process(target=run, args=[sharedMap, sharedMemoryMap])
    p.start()

    try:
        sim = SimulavrAdaptor.SimulavrAdapter()
        sim.runProgram(sharedMap, sharedMemoryMap)
    except:
        p.terminate()

