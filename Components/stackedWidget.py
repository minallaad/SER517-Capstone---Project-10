# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget


class stackWidget(QtWidgets.QWidget):    # Used to switch between multiple layout


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


    @staticmethod
    def addWidget(qFrame):
        stackWidget.StackWidget.addWidget(qFrame)

    @staticmethod
    def removeWidget(qFrame):
        stackWidget.StackWidget.removeWidget(qFrame)


    @staticmethod
    def getInstance():
        """ Static access method. """
        if stackWidget.StackWidget == None:
            stackWidget()
        return stackWidget.StackWidget


    @staticmethod
    def incrementTopCount():
        stackWidget.top = stackWidget.top + 1;
        stackWidget.StackWidget.setCurrentIndex(stackWidget.top)

    @staticmethod
    def decrementTopCount():
        stackWidget.top = stackWidget.top - 1;
        stackWidget.StackWidget.setCurrentIndex(stackWidget.top)




