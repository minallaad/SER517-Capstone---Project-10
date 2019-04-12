import pysimulavr
import Components.Globalmap
import Components.EEPROM

class SimulavrAdapter(object):
    DEFAULT_CLOCK_SETTING = 63
    uiUpdateFlag = False

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

    def runProgram(self, ui, thread):
        dev = self.loadDevice("atmega328", "simulavr/adaptor/simadc.elf")

        i = 0
        while True:
            
            if i == 5000:
                self.getMemoryValue(dev)

                if self.uiUpdateFlag == True :
                    ui.updateUI()

                    self.uiUpdateFlag == False

                if Components.Globalmap.Map.refresh_flag:

                    Components.Globalmap.Map.refresh_flag = False
                    self.getMemoryDumpRange(dev)
                    Components.EEPROM.memoryDump.UpdateEEPROM()
                i = 0

            i = i + 1
            
            self.doStep()

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

    def getMemoryValue(self, dev):
        self.getDDRValues(dev)

    def getDDRValues(self, dev):
        for key, value in Components.Globalmap.Map.registerAddressMap.items():
            val = dev.getRWMem(value)

            if (len(Components.Globalmap.Map.map) == len(Components.Globalmap.Map.registerAddressMap) and val != Components.Globalmap.Map.map[key]) :
                self.uiUpdateFlag = True
            Components.Globalmap.Map.map[key] = val

    def getMemoryDumpRange(self, dev):
        map = {}
        address = Components.Globalmap.Map.eeprom_address
        for i in range(0, 20):
            address += i
            value_list = []
            new_address = 0
            for j in range(0, 16):
                new_address = address + j
                val = dev.eeprom.ReadFromAddress(new_address)
                value_list.append(str(val))
            map[address] = value_list
            address = new_address

        Components.Globalmap.Map.memory_map = map
