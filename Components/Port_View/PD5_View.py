# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFrame
from Components import pinLevelDiagram

import Components.stackedWidget


class PD5_View(QtWidgets.QWidget):
    PD5Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PD5_View, self).__init__()

        if PD5_View.PD5Frame == None:
            PD5_View.standard = Components.Standard.value
            PD5_View.PD5Frame = QFrame()
            PD5_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PD5_View.pinFrame.setupUi(PD5_View.PD5Frame)

    @staticmethod
    def getViewFrame():
        return PD5_View.PD5Frame

    @staticmethod
    def getInstance():
        return PD5_View

    @staticmethod
    def setDDR(value):
        PD5_View.pinFrame.ddrValueLabel.setText(str(value))
        if value == 1:
            PD5_View.pinFrame.ddrLine1.setStyleSheet(PD5_View.standard.high)
            PD5_View.pinFrame.ddrLine2.setStyleSheet(PD5_View.standard.high)
        else:
            PD5_View.pinFrame.ddrLine1.setStyleSheet(PD5_View.standard.low)
            PD5_View.pinFrame.ddrLine2.setStyleSheet(PD5_View.standard.low)

    @staticmethod
    def setPort(value):
        if value == 1:
            PD5_View.pinFrame.portLine.setStyleSheet(PD5_View.standard.high)
        else:
            PD5_View.pinFrame.portLine.setStyleSheet(PD5_View.standard.low)

    @staticmethod
    def setPin(value):
        PD5_View.pinFrame.pinLine.setText(str(value))

        if value == 1:
            PD5_View.pinFrame.pinLine.setStyleSheet(PD5_View.standard.high)
            PD5_View.pinFrame.pinOutputFrame.setStyleSheet(PD5_View.standard.highBackground)
        else:
            PD5_View.pinFrame.pinLine.setStyleSheet(PD5_View.standard.low)
            PD5_View.pinFrame.pinOutputFrame.setStyleSheet(PD5_View.standard.lowBackground)