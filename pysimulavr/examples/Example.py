import pysimulavr
import SimulavrAdaptor
import socket
import sys
from multiprocessing import Process

class XPin(pysimulavr.Pin):

    def __init__(self, dev, name, state=None):
        pysimulavr.Pin.__init__(self)
        self.name = name
        if state is not None: self.SetPin(state)
        # hold the connecting net here, it have not be destroyed, if we leave this method
        self.__net = pysimulavr.Net()
        self.__net.Add(self)
        self.__net.Add(dev.GetPin(name))

    def SetInState(self, pin):
        pysimulavr.Pin.SetInState(self, pin)
        print "%s='%s' (t=%dns)" % (self.name, pin.toChar(), sim.getCurrentTime())


'''def callGdb(dev1):

    gdb = pysimulavr.GdbServer(dev1, 1212, 0, True)
    gdb.TryConnectGdb()
    t1 = pysimulavr.SystemClock.Instance()
    t1.AddAsyncMember(dev1)
    t1.Add(gdb)
    t1.Endless()
    print "Here"'''


def call(dev):
    HOST = '127.0.0.1'
    PORT = 7777
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    while 1:
        connection, client = s.accept()
        i = 0
        # while i < 32:
        #     connection.send(b'Register - ')
        #     connection.send(bytes(i))
        #     connection.send(b'---->')
        #     connection.send(bytes(getRegisterByAddress(dev, i)))
        #     connection.send(b'\n')
        #     i +=1
        connection.send(bytes(dev.getRWMem(0x1)))
        connection.send(bytes(dev.getRWMem(0x50)))
        connection.send(bytes(dev.getRWMem(0x6)))
        connection.close()

def getRegisterByAddress(dev, addr):
    v = dev.GetCoreReg(addr)
    return v

if __name__ == "__main__":
    proc = "atmega128"
    elffile = "example_io.elf"

    sim = SimulavrAdaptor.SimulavrAdapter()
    sim.dmanSingleDeviceApplication()
    dev = sim.loadDevice(proc, elffile)

    Process(target=sim.runGDB, args=[dev]).start()
    Process(target=call, args=[dev]).start()

    a0 = XPin(dev, "A0")
    a1 = XPin(dev, "A1", "H")
    a7 = XPin(dev, "A7", "H")

    sim.dmanStart()
    print "simulation start: (t=%dns)" % sim.getCurrentTime()
    sim.doRun(sim.getCurrentTime() + 7000000)
    a1.SetPin("L")
    sim.doRun(sim.getCurrentTime() + 5000000)
    a7.SetPin("L")
    print sim.getAllRegisteredTraceValues()
    sim.doRun(sim.getCurrentTime() + 2000000)
    a1.SetPin("H")
    sim.doRun(sim.getCurrentTime() + 1000000)
    print "simulation end: (t=%dns)" % sim.getCurrentTime()
    print dev.PC
    print "value 'timer2_ticks'=%d" % sim.getWordByName(dev, "timer2_ticks")
    print "value 'port_val'=0x%x" % sim.getWordByName(dev, "port_val")
    print "EEPRom"
    print dev.eeprom.CTRL_IRQ
    print "Mem total size"
    print dev.GetMemTotalSize()
    print "Mem io size"
    print dev.GetMemIOSize()
    print "Register Size"
    print dev.GetMemRegisterSize()
    print "RWMemory"
    mem = [0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B]
    mem += [0x35, 0x36, 0x37, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F, 0x40]
    mem += [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x4A]
    mem += [0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x50, 0x53, 0x54, 0x55]
    for memory in mem:
        print dev.data.GetSymbolAtAddress(memory) + '-' + str(dev.getRWMem(memory))
    sim.dmanStop()

