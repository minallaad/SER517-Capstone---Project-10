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

    #set the DDR value to high or low visually in the pin level diagram
    @staticmethod
    def setDDR(value):
        Port_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            Port_View.pinFrame.ddrLine1.setStyleSheet(Port_View.standard.high)
            Port_View.pinFrame.ddrLine2.setStyleSheet(Port_View.standard.high)
        else:
            Port_View.pinFrame.ddrLine1.setStyleSheet(Port_View.standard.low)
            Port_View.pinFrame.ddrLine2.setStyleSheet(Port_View.standard.low)

    #set the PORT value to high or low visually in the pin level diagram
    @staticmethod
    def setPort(value):
        Port_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            Port_View.pinFrame.portLine.setStyleSheet(Port_View.standard.high)
        else:
            Port_View.pinFrame.portLine.setStyleSheet(Port_View.standard.low)

    #function to set the pin value to high or low visually based on pin value
    @staticmethod
    def setPin(value):
        if value == 1:
            Port_View.pinFrame.pinLine.setStyleSheet(Port_View.standard.high)
            Port_View.pinFrame.pinOutputFrame.setStyleSheet(Port_View.standard.highBackground)
            Port_View.pinFrame.pullupLine.setStyleSheet(Port_View.standard.high)
        else:
            Port_View.pinFrame.pinLine.setStyleSheet(Port_View.standard.low)
            Port_View.pinFrame.pinOutputFrame.setStyleSheet(Port_View.standard.lowBackground)
            Port_View.pinFrame.pullupLine.setStyleSheet(Port_View.standard.low)