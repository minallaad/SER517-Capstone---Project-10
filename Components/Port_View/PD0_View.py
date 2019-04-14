# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt


import Components.stackedWidget
import Components.Standard
from Components import pinLevelDiagram



class PD0_View(QtWidgets.QWidget):

    PD0Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PD0_View, self).__init__()

        if PD0_View.PD0Frame == None:
            PD0_View.PD0Frame = QFrame()

            PD0_View.standard =  Components.Standard.value
            PD0_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PD0_View.pinFrame.setupUi(PD0_View.PD0Frame)


    @staticmethod
    def getViewFrame():
        return PD0_View.PD0Frame

    @staticmethod
    def getInstance():
        return PD0_View

    @staticmethod
    def setDDR(value):
        PD0_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            PD0_View.pinFrame.ddrLine1.setStyleSheet(PD0_View.standard.high)
            PD0_View.pinFrame.ddrLine2.setStyleSheet(PD0_View.standard.high)
        else:
            PD0_View.pinFrame.ddrLine1.setStyleSheet(PD0_View.standard.low)
            PD0_View.pinFrame.ddrLine2.setStyleSheet(PD0_View.standard.low)

    @staticmethod
    def setPort(value):
        PD0_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            PD0_View.pinFrame.portLine.setStyleSheet(PD0_View.standard.high)
        else:
            PD0_View.pinFrame.portLine.setStyleSheet(PD0_View.standard.low)

    @staticmethod
    def setPin(value):
        if value == 1:
            PD0_View.pinFrame.pinLine.setStyleSheet(PD0_View.standard.high)
            PD0_View.pinFrame.pinOutputFrame.setStyleSheet(PD0_View.standard.highBackground)
        else:
            PD0_View.pinFrame.pinLine.setStyleSheet(PD0_View.standard.low)
            PD0_View.pinFrame.pinOutputFrame.setStyleSheet(PD0_View.standard.lowBackground)