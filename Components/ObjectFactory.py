import Components.Port_View.PD0_View
import Components.Port_View.PD1_View
import Components.Port_View.PD2_View
import Components.Port_View.PD3_View
import Components.Port_View.PD4_View
import Components.Port_View.PD5_View
import Components.Port_View.PD6_View
import Components.Port_View.PD7_View

import Components.Port_View.PC0_View
import Components.Port_View.PC1_View
import Components.Port_View.PC2_View
import Components.Port_View.PC3_View
import Components.Port_View.PC4_View
import Components.Port_View.PC5_View
import Components.Port_View.PC6_View
import Components.Port_View.PC7_View

import Components.Port_View.PB0_View
import Components.Port_View.PB1_View
import Components.Port_View.PB2_View


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
        if objectName == 'PD0':
            return Components.Port_View.PD0_View.PD0_View().getInstance()
        elif objectName == 'PD1':
            return Components.Port_View.PD1_View.PD1_View().getInstance()
        elif objectName == 'PD2':
            return Components.Port_View.PD2_View.PD2_View().getInstance()
        elif objectName == 'PD3':
            return Components.Port_View.PD3_View.PD3_View().getInstance()
        elif objectName == 'PD4':
            return Components.Port_View.PD4_View.PD4_View().getInstance()
        elif objectName == 'PD5':
            return Components.Port_View.PD5_View.PD5_View().getInstance()
        elif objectName == 'PD6':
            return Components.Port_View.PD6_View.PD6_View().getInstance()
        elif objectName == 'PD7':
            return Components.Port_View.PD7_View.PD7_View().getInstance()
        elif objectName == 'PC0':
            return Components.Port_View.PC0_View.PC0_View().getInstance()
        elif objectName == 'PC1':
            return Components.Port_View.PC1_View.PC1_View().getInstance()
        elif objectName == 'PC2':
            return Components.Port_View.PC2_View.PC2_View().getInstance()
        elif objectName == 'PC3':
            return Components.Port_View.PC3_View.PC3_View().getInstance()
        elif objectName == 'PC4':
            return Components.Port_View.PC4_View.PC4_View().getInstance()
        elif objectName == 'PC5':
            return Components.Port_View.PC5_View.PC5_View().getInstance()
        elif objectName == 'PC6':
            return Components.Port_View.PC6_View.PC6_View().getInstance()
        elif objectName == 'PC7':
            return Components.Port_View.PC7_View.PC7_View().getInstance()
        elif objectName == 'PB0':
            return Components.Port_View.PB0_View.PB0_View().getInstance()
        elif objectName == 'PB1':
            return Components.Port_View.PB1_View.PB1_View().getInstance()
        elif objectName == 'PB2':
            return Components.Port_View.PB2_View.PB2_View().getInstance()
        else:
            return None
