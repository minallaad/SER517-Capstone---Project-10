import Components.Port_View.PD0_View
import Components.Port_View.PD1_View
import Components.Port_View.PD2_View
from Components import WatchDogTimer
from Components import  SPI


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
        if(viewName == 'PD0'):
            return Components.Port_View.PD0_View.PD0_View().getPD0ViewDiagram()
        elif viewName == 'PD1':
            return Components.Port_View.PD1_View.PD1_View().getPD1ViewDiagram()
        elif viewName == 'WATCHDOG':
            return WatchDogTimer.Ui_watchDogFrame()
        elif viewName == 'SPI':
            return SPI.Ui_SPIFrame()
        else:
            return None

