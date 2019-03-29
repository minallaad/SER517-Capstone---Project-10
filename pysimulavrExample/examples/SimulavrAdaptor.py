import pysimulavr
import Components.Globalmap
import time


class SimulavrAdapter(object):
    DEFAULT_CLOCK_SETTING = 63

    def loadDevice(self, t, e):
        self.__sc = pysimulavr.SystemClock.Instance()
        self.__sc.ResetClock()
        dev = pysimulavr.AvrFactory.instance().makeDevice(t)
        dev.Load(e)
        dev.SetClockFreq(self.DEFAULT_CLOCK_SETTING)
        self.__sc.Add(dev)
        gdb = pysimulavr.GdbServer(dev, 1212, 0, True)
        self.__gdb = gdb
        self.__sc.Add(gdb)
        return dev

    def runProgram(self, ui):
        dev = self.loadDevice("atmega328", "/home/ayan/Desktop/TestProject/simadoc/bin/Release/simadc.elf")
        while True:
            self.getMemoryValue(dev)
            ui.updateUI()
            self.doStep()
            time.sleep(2)

    def doRun(self, n):
        ct = self.__sc.GetCurrentTime
        while ct() < n:
            res = self.__sc.Step()
            if res is not 0: return res
        return 0

    def doStep(self, stepcount=1):
        while stepcount > 0:
            res = self.__sc.Step()
            if res is not 0: return res
            stepcount -= 1
        return 0

    def getCurrentTime(self):
        return self.__sc.GetCurrentTime()

    def getAllRegisteredTraceValues(self):
        os = pysimulavr.ostringstream()
        pysimulavr.DumpManager.Instance().save(os)
        return filter(None, [i.strip() for i in os.str().split("\n")])

    def dmanSingleDeviceApplication(self):
        pysimulavr.DumpManager.Instance().SetSingleDeviceApp()

    def dmanStart(self):
        pysimulavr.DumpManager.Instance().start()

    def dmanStop(self):
        pysimulavr.DumpManager.Instance().stopApplication()

    def setVCDDump(self, vcdname, signals, rstrobe=False, wstrobe=False):
        dman = pysimulavr.DumpManager.Instance()
        sigs = ["+ " + i for i in signals]
        dman.addDumpVCD(vcdname, "\n".join(sigs), "ns", rstrobe, wstrobe)

    def getWordByName(self, dev, label):
        addr = dev.data.GetAddressAtSymbol(label)
        v = dev.getRWMem(addr)
        addr += 1
        v = (dev.getRWMem(addr) << 8) + v
        return v

    def getFlashWordByName(self, dev, label):
        addr = dev.Flash.GetAddressAtSymbol(label)
        v = dev.getRWMem(addr)
        addr += 1
        v = (dev.getRWMem(addr) << 8) + v
        return v

    def getMemoryValue(self, dev):
        values = {}

        # self.getPortValues(dev)
        self.getDDRValues(dev)

        return values

    def getDDRValues(self, dev):
        for key, value in Components.Globalmap.Map.registerAddressMap.items():
            val = dev.getRWMem(value)
            Components.Globalmap.Map.map[key] = val

    def getPortValues(self, dev):

        for key, value in Components.Globalmap.Map.port_address_map.items():
            val = dev.getRWMem(value) & 2
            #code to change if required
            binVal = bin(val)[2:]
            if len(binVal) < 7:
                binVal = '0'*(7-len(binVal)) + binVal
            #till here
            for i in range(len(binVal)-1, -1, -1):
                update = Components.Globalmap.Map.port_register_map[key] + str(len(binVal) - i - 1)
                Components.Globalmap.Map.map[update] = binVal[i]