import pysimulavr
import SimulavrAdaptor
import threading


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


def callGdb(dev):
    #Open Simulavr in GDB mode in a different thread to listen at port 1212
    gdb = pysimulavr.GdbServer(dev, 1212, 0, True)
    gdb.TryConnectGdb()
    t1 = pysimulavr.SystemClock.Instance()
    t1.Add(gdb)
    t1.Endless()


def call(dev):
    HOST = '127.0.0.1'
    PORT = 7777
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    while 1:
        connection, client = s.accept()
        i = 0
	current_thread = dev.stack.m_ThreadList.GetCurrentThreadForGDB()
    	thread = dev.stack.m_ThreadList.GetThreadFromGDB(current_thread)
	registers = thread.registers
        while i < 32:
            connection.send(b'Register - ')
            connection.send(bytes(i))
            connection.send(b'---->')
            connection.send(bytes(getRegisterByAddress(dev, i)))
            connection.send(b'\n')
            i +=1

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
    sim.dmanStop()

    thread1 = threading.Thread(target=callGdb, args=[dev])

    thread = threading.Thread(target=call, args=[dev])
    thread.start()
    thread1.start()

    thread.join()
    thread1.join()

    del dev
