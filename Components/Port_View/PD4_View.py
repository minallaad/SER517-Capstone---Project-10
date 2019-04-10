# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFrame
from Components import pinLevelDiagram

import Components.stackedWidget


class PD4_View(QtWidgets.QWidget):
    PD4Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PD4_View, self).__init__()

        if PD4_View.PD4Frame == None:
            PD4_View.standard = Components.Standard.value
            PD4_View.PD4Frame = QFrame()
            PD4_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PD4_View.pinFrame.setupUi(PD4_View.PD4Frame)

    @staticmethod
    def getViewFrame():
        return PD4_View.PD4Frame

    @staticmethod
    def getInstance():
        return PD4_View

    @staticmethod
    def setDDR(value):
        PD4_View.pinFrame.ddrValueLabel.setText(str(value))
        if value == 1:
            PD4_View.pinFrame.ddrLine1.setStyleSheet(PD4_View.standard.high)
            PD4_View.pinFrame.ddrLine2.setStyleSheet(PD4_View.standard.high)
        else:
            PD4_View.pinFrame.ddrLine1.setStyleSheet(PD4_View.standard.low)
            PD4_View.pinFrame.ddrLine2.setStyleSheet(PD4_View.standard.low)

    @staticmethod
    def setPort(value):
        if value == 1:
            PD4_View.pinFrame.portLine.setStyleSheet(PD4_View.standard.high)
        else:
            PD4_View.pinFrame.portLine.setStyleSheet(PD4_View.standard.low)

    @staticmethod
    def setPin(value):
        PD4_View.pinFrame.pinLine.setText(str(value))

        if value == 1:
            PD4_View.pinFrame.pinLine.setStyleSheet(PD4_View.standard.high)
            PD4_View.pinFrame.pinOutputFrame.setStyleSheet(PD4_View.standard.highBackground)
            print('here2', value)
        else:
            PD4_View.pinFrame.pinLine.setStyleSheet(PD4_View.standard.low)
            PD4_View.pinFrame.pinOutputFrame.setStyleSheet(PD4_View.standard.lowBackground)







