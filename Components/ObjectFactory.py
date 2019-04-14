
import Components.Port_View.Port_View
from Components import WatchDogTimer
from Components import  SPI
from Components import EEPROM


class ObjectFactory():

    objectFactory = None
    top = None

    def __init__(self):
        """ Virtually private constructor. """
        super().__init__()
        if ObjectFactory.objectFactory != None:
            raise Exception("This class is a singleton!")
        else:
            ObjectFactory.objectFactory = ObjectFactory()


    @staticmethod
    def getInstance():
        if ObjectFactory.objectFactory == None:
            ObjectFactory()
        return ObjectFactory.objectFactory

    @staticmethod
    def getObject(objectName):
        if 'PD' in objectName or 'PB' in objectName or 'PC' in objectName:
            return Components.Port_View.Port_View.PD0_View().getInstance()
        else:
            return None
