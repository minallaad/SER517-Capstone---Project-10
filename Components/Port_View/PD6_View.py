# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFrame
from Components import pinLevelDiagram

import Components.stackedWidget


class PD6_View(QtWidgets.QWidget):
    PD6Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PD6_View, self).__init__()

        if PD6_View.PD6Frame == None:
            PD6_View.standard = Components.Standard.value
            PD6_View.PD6Frame = QFrame()
            PD6_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PD6_View.pinFrame.setupUi(PD6_View.PD6Frame)

    @staticmethod
    def getViewFrame():
        return PD6_View.PD6Frame

    @staticmethod
    def getInstance():
        return PD6_View

    @staticmethod
    def setDDR(value):
        PD6_View.pinFrame.ddrValueLabel.setText(str(value))
        if value == 1:
            PD6_View.pinFrame.ddrLine1.setStyleSheet(PD6_View.standard.high)
            PD6_View.pinFrame.ddrLine2.setStyleSheet(PD6_View.standard.high)
        else:
            PD6_View.pinFrame.ddrLine1.setStyleSheet(PD6_View.standard.low)
            PD6_View.pinFrame.ddrLine2.setStyleSheet(PD6_View.standard.low)

    @staticmethod
    def setPort(value):
        if value == 1:
            PD6_View.pinFrame.portLine.setStyleSheet(PD6_View.standard.high)
        else:
            PD6_View.pinFrame.portLine.setStyleSheet(PD6_View.standard.low)

    @staticmethod
    def setPin(value):
        PD6_View.pinFrame.pinLine.setText(str(value))

        if value == 1:
            PD6_View.pinFrame.pinLine.setStyleSheet(PD6_View.standard.high)
            PD6_View.pinFrame.pinOutputFrame.setStyleSheet(PD6_View.standard.highBackground)
        else:
            PD6_View.pinFrame.pinLine.setStyleSheet(PD6_View.standard.low)
            PD6_View.pinFrame.pinOutputFrame.setStyleSheet(PD6_View.standard.lowBackground)