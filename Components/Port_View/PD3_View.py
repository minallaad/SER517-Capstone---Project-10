# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFrame
from Components import pinLevelDiagram

import Components.stackedWidget


class PD3_View(QtWidgets.QWidget):
    PD3Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PD3_View, self).__init__()

        if PD3_View.PD3Frame == None:
            PD3_View.standard = Components.Standard.value
            PD3_View.PD3Frame = QFrame()
            PD3_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PD3_View.pinFrame.setupUi(PD3_View.PD3Frame)

    @staticmethod
    def getViewFrame():
        return PD3_View.PD3Frame

    @staticmethod
    def getInstance():
        return PD3_View

    @staticmethod
    def setDDR(value):
        PD3_View.pinFrame.ddrValueLabel.setText(str(value))
        if value == 1:
            PD3_View.pinFrame.ddrLine1.setStyleSheet(PD3_View.standard.high)
            PD3_View.pinFrame.ddrLine2.setStyleSheet(PD3_View.standard.high)
        else:
            PD3_View.pinFrame.ddrLine1.setStyleSheet(PD3_View.standard.low)
            PD3_View.pinFrame.ddrLine2.setStyleSheet(PD3_View.standard.low)

    @staticmethod
    def setPort(value):
        if value == 1:
            PD3_View.pinFrame.portLine.setStyleSheet(PD3_View.standard.high)
        else:
            PD3_View.pinFrame.portLine.setStyleSheet(PD3_View.standard.low)

    @staticmethod
    def setPin(value):
        PD3_View.pinFrame.pinLine.setText(str(value))

        if value == 1:
            PD3_View.pinFrame.pinLine.setStyleSheet(PD3_View.standard.high)
            PD3_View.pinFrame.pinOutputFrame.setStyleSheet(PD3_View.standard.highBackground)
        else:
            PD3_View.pinFrame.pinLine.setStyleSheet(PD3_View.standard.low)
            PD3_View.pinFrame.pinOutputFrame.setStyleSheet(PD3_View.standard.lowBackground)
