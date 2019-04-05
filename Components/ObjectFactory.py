import Components.Port_View.PD0_View
import Components.Port_View.PD1_View
import Components.Port_View.PD2_View
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
        if(objectName == 'PD0'):
            return Components.Port_View.PD0_View.PD0_View().getInstance()
        elif objectName == 'PD1':
            return Components.Port_View.PD1_View.PD1_View().getInstance()
        elif objectName == 'PD2':
            return Components.Port_View.PD1_View.PD2_View().getInstance()
        else:
            return None

