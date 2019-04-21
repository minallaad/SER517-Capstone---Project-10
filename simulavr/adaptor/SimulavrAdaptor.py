"""
This file is used to create simulavr adaptor. The adaptor object can be used to call various
functions in order to fetch and update the values from simulavr. These values are then sent to
UI to display the updated values as per the simulation cycle.
"""

import pysimulavr
import Components.Globalmap
import Components.EEPROM


class SimulavrAdapter(object):
    DEFAULT_CLOCK_SETTING = 63
    uiUpdateFlag = False

    ''' Description: Function to create the device object.
        @param t: The type of device/microcontroller used.
        @param e: The path of the target file (.elf file) that needs to run. The default path is set to the elf
                present in the current directory.
    '''

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

    '''
    Description: This function is required to run the target file. It is called from the Simulavr thread.
    @param ui: The object of the UI.
    @param thread: The reference of simulavr thread which is run at the start of the application.
    '''

    def runProgram(self, ui, thread):
        dev = self.loadDevice("atmega328", "simulavr/adaptor/simadc.elf")

        i = 0
        while True:
            if i == 5000:
                '''fetching values from memory address'''
                self.getMemoryValue(dev)

                if self.uiUpdateFlag == True:
                    ui.updateUI()

                    self.uiUpdateFlag == False

                '''if referesh flag is true, update the values again.'''
                if Components.Globalmap.Map.refresh_flag:
                    Components.Globalmap.Map.refresh_flag = False
                    self.getMemoryDumpRange(dev)
                    Components.EEPROM.memoryDump.UpdateEEPROM()
                i = 0

            i = i + 1

            self.doStep()

    '''
    Description: This function is used to perform step operation of simulavr
    @param stepcount: number of times the step needs to be called. Default value is 1.
    '''

    def doStep(self, stepcount=1):
        while stepcount > 0:
            res = self.__sc.Step()
            if res is not 0: return res
            stepcount -= 1
        return 0

    '''
    Description: This function is used to fetch the memory values from the addresses.
    @param dev: The reference of the device object.
    '''

    def getMemoryValue(self, dev):
        self.getDDRValues(dev)

    '''
    Description: This function is to fetch DDR values from specific memory addresses.
    @param dev: The reference of the device object.
    '''

    def getDDRValues(self, dev):
        for key, value in Components.Globalmap.Map.registerAddressMap.items():
            val = dev.getRWMem(value)
            if (len(Components.Globalmap.Map.map) == len(Components.Globalmap.Map.registerAddressMap) and val !=
                    Components.Globalmap.Map.map[key]):
                self.uiUpdateFlag = True
            Components.Globalmap.Map.map[key] = val

    '''
    Description: This function is used to fetch the values from the EEPROM.
    @param dev: The reference of the device object.
    '''
    def getMemoryDumpRange(self, dev):
        map = {}
        address = Components.Globalmap.Map.eeprom_address
        for i in range(0, 20):
            address += i
            address = address % 1024
            value_list = []
            new_address = 0
            for j in range(0, 16):
                new_address = address + j
                val = dev.eeprom.ReadFromAddress(new_address % 1024)
                value_list.append(str(val))
            map[address] = value_list
            address = new_address

        Components.Globalmap.Map.memory_map = map
