# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget

""" Singleton Class Stack Widget used to switch the layouts
    To switch to different Layout, add the QFrame of that layout to the Stack and make the top point to the layout.
    To switch Back to previous Layout remove the QFrame from stack and make decrement the top counter"""
class stackWidget(QtWidgets.QWidget):

    StackWidget = None
    top = None


    def __init__(self):
        """ Virtually private constructor. """
        super().__init__()
        if stackWidget.StackWidget != None:
            raise Exception("This class is a singleton!")
        else:
            stackWidget.StackWidget = QStackedWidget()
            stackWidget.top = 0

    """ 
    Description: Static Method to add the Object of QFrame on Stack  
    @param qFrame: Frame of a component that needs to be added."""
    @staticmethod
    def addWidget(qFrame):
        stackWidget.StackWidget.addWidget(qFrame)

    """ 
    Description: Static Method to remove the Object of QFrame on Stack  
    @param qFrame: Frame of a component that needs to be added.
    """
    @staticmethod
    def removeWidget(qFrame):
        stackWidget.StackWidget.removeWidget(qFrame)


    @staticmethod
    def getInstance():
        """ Static access method. """
        if stackWidget.StackWidget == None:
            stackWidget()
        return stackWidget.StackWidget

    """ 
    Description: Static Method to increment the top counter.   
    """
    @staticmethod
    def incrementTopCount():
        stackWidget.top = stackWidget.top + 1
        stackWidget.StackWidget.setCurrentIndex(stackWidget.top)

    """ 
    Description: Static Method to decrement the top counter.
    """
    @staticmethod
    def decrementTopCount():
        stackWidget.top = stackWidget.top - 1
        stackWidget.StackWidget.setCurrentIndex(stackWidget.top)




