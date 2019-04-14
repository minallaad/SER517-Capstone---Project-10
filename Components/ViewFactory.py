
import Components.Port_View.Port_View
import Components.Port_View.PB0_View
import Components.Port_View.PB1_View
import Components.Port_View.PB2_View

from Components import WatchDogTimer
from Components import  SPI
from Components import EEPROM


class ViewFactory():

    viewFactory = None
    top = None

    def __init__(self):
        """ Virtually private constructor. """
        super().__init__()
        if ViewFactory.viewFactory != None:
            raise Exception("This class is a singleton!")
        else:
            ViewFactory.viewFactory = ViewFactory()


    @staticmethod
    def getInstance():
        if ViewFactory.viewFactory == None:
            ViewFactory()
        return ViewFactory.viewFactory

    @staticmethod
    def getView(viewName):
        if 'PD' in viewName or 'PB' in viewName or 'PC' in viewName:
            return Components.Port_View.Port_View.PD0_View().getViewFrame()
        elif viewName == 'WATCHDOG':
            return WatchDogTimer.Ui_watchDogFrame()
        elif viewName == 'EEPROM':
            return EEPROM.memoryDump().getMemoryDump()
        elif viewName == 'SPI':
            return SPI.Ui_SPIFrame()
        else:
            return None

