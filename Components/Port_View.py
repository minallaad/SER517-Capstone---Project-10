# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt


import Components.stackedWidget
import Components.Standard
from Components import pinLevelDiagram



class Port_View(QtWidgets.QWidget):

    PortFrame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(Port_View, self).__init__()

        if Port_View.PortFrame == None:
            Port_View.PortFrame = QFrame()

            Port_View.standard =  Components.Standard.value
            Port_View.pinFrame = pinLevelDiagram.Ui_Frame()
            Port_View.pinFrame.setupUi(Port_View.PortFrame)


    @staticmethod
    def getViewFrame():
        return Port_View.PortFrame

    @staticmethod
    def getInstance():
        return Port_View

    '''
    Description: Function to set the DDR value to high or low visually in the pin level diagram
    @param value: Value of the DDR based on which the high and low colors are set.
    '''
    @staticmethod
    def setDDR(value):
        Port_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            Port_View.pinFrame.ddrLine1.setStyleSheet(Port_View.standard.high)
            Port_View.pinFrame.ddrLine2.setStyleSheet(Port_View.standard.high)
        else:
            Port_View.pinFrame.ddrLine1.setStyleSheet(Port_View.standard.low)
            Port_View.pinFrame.ddrLine2.setStyleSheet(Port_View.standard.low)

    '''
    Description: set the PORT value to high or low visually in the pin level diagram
    @param value: Value of the port based on which the high and low colors are set.
    '''
    @staticmethod
    def setPort(value):
        Port_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            Port_View.pinFrame.portLine.setStyleSheet(Port_View.standard.high)
        else:
            Port_View.pinFrame.portLine.setStyleSheet(Port_View.standard.low)

    '''
    Description: Function to set the PIN value to high or low visually based on pin value
    @param value: Value of the PIN based on which the high and low colors are set.
    '''
    @staticmethod
    def setPin(value):
        if value == 1:
            Port_View.pinFrame.pinLine.setStyleSheet(Port_View.standard.high)
            Port_View.pinFrame.pinOutputFrame.setStyleSheet(Port_View.standard.highBackground)
        else:
            Port_View.pinFrame.pinLine.setStyleSheet(Port_View.standard.low)
            Port_View.pinFrame.pinOutputFrame.setStyleSheet(Port_View.standard.lowBackground)