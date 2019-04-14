# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFrame
from Components import pinLevelDiagram

import Components.stackedWidget


class PD7_View(QtWidgets.QWidget):
    PD7Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PD7_View, self).__init__()

        if PD7_View.PD7Frame == None:
            PD7_View.standard = Components.Standard.value
            PD7_View.PD7Frame = QFrame()
            PD7_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PD7_View.pinFrame.setupUi(PD7_View.PD7Frame)

    @staticmethod
    def getViewFrame():
        return PD7_View.PD7Frame

    @staticmethod
    def getInstance():
        return PD7_View

    @staticmethod
    def setDDR(value):
        PD7_View.pinFrame.ddrValueLabel.setText(str(value))
        if value == 1:
            PD7_View.pinFrame.ddrLine1.setStyleSheet(PD7_View.standard.high)
            PD7_View.pinFrame.ddrLine2.setStyleSheet(PD7_View.standard.high)
        else:
            PD7_View.pinFrame.ddrLine1.setStyleSheet(PD7_View.standard.low)
            PD7_View.pinFrame.ddrLine2.setStyleSheet(PD7_View.standard.low)

    @staticmethod
    def setPort(value):
        if value == 1:
            PD7_View.pinFrame.portLine.setStyleSheet(PD7_View.standard.high)
        else:
            PD7_View.pinFrame.portLine.setStyleSheet(PD7_View.standard.low)

    @staticmethod
    def setPin(value):
        PD7_View.pinFrame.pinLine.setText(str(value))

        if value == 1:
            PD7_View.pinFrame.pinLine.setStyleSheet(PD7_View.standard.high)
            PD7_View.pinFrame.pinOutputFrame.setStyleSheet(PD7_View.standard.highBackground)
        else:
            PD7_View.pinFrame.pinLine.setStyleSheet(PD7_View.standard.low)
            PD7_View.pinFrame.pinOutputFrame.setStyleSheet(PD7_View.standard.lowBackground)