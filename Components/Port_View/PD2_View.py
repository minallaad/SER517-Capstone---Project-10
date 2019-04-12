# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import   QFrame
from Components import pinLevelDiagram


import Components.stackedWidget


class PD2_View(QtWidgets.QWidget):

    PD2Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PD2_View, self).__init__()

        if PD2_View.PD2Frame == None:
            PD2_View.standard = Components.Standard.value
            PD2_View.PD2Frame = QFrame()
            PD2_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PD2_View.pinFrame.setupUi(PD2_View.PD2Frame)


    @staticmethod
    def getViewFrame():
        return PD2_View.PD2Frame

    @staticmethod
    def getInstance():
        return PD2_View

    @staticmethod
    def setDDR(value):
        PD2_View.pinFrame.ddrValueLabel.setText(str(value))
        if value == 1:
            PD2_View.pinFrame.ddrLine1.setStyleSheet(PD2_View.standard.high)
            PD2_View.pinFrame.ddrLine2.setStyleSheet(PD2_View.standard.high)
        else:
            PD2_View.pinFrame.ddrLine1.setStyleSheet(PD2_View.standard.low)
            PD2_View.pinFrame.ddrLine2.setStyleSheet(PD2_View.standard.low)

    @staticmethod
    def setPort(value):
        if value == 1:
            PD2_View.pinFrame.portLine.setStyleSheet(PD2_View.standard.high)
        else:
            PD2_View.pinFrame.portLine.setStyleSheet(PD2_View.standard.low)

    @staticmethod
    def setPin(value):
        PD2_View.pinFrame.pinLine.setText(str(value))

        if value == 1:
            PD2_View.pinFrame.pinLine.setStyleSheet(PD2_View.standard.high)
            PD2_View.pinFrame.pinOutputFrame.setStyleSheet(PD2_View.standard.highBackground)
        else:
            PD2_View.pinFrame.pinLine.setStyleSheet(PD2_View.standard.low)
            PD2_View.pinFrame.pinOutputFrame.setStyleSheet(PD2_View.standard.lowBackground)
