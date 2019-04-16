# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
from Components import pinLevelDiagram


class PB1_View(QtWidgets.QWidget):

    PB1Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PB1_View, self).__init__()

        if PB1_View.PB1Frame == None:
            PB1_View.PB1Frame = QFrame()

            PB1_View.standard = Components.Standard.value
            PB1_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PB1_View.pinFrame.setupUi(PB1_View.PB1Frame)


    @staticmethod
    def getViewFrame():
        return PB1_View.PB1Frame

    @staticmethod
    def getInstance():
        return PB1_View

    @staticmethod
    def setDDR(value):
        PB1_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            PB1_View.pinFrame.ddrLine1.setStyleSheet(PB1_View.standard.high)
            PB1_View.pinFrame.ddrLine2.setStyleSheet(PB1_View.standard.high)
        else:
            PB1_View.pinFrame.ddrLine1.setStyleSheet(PB1_View.standard.low)
            PB1_View.pinFrame.ddrLine2.setStyleSheet(PB1_View.standard.low)

    @staticmethod
    def setPort(value):
        PB1_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            PB1_View.pinFrame.portLine.setStyleSheet(PB1_View.standard.high)
        else:
            PB1_View.pinFrame.portLine.setStyleSheet(PB1_View.standard.low)

    @staticmethod
    def setPin(value):
        if value == 1:
            PB1_View.pinFrame.pinLine.setStyleSheet(PB1_View.standard.high)
            PB1_View.pinFrame.pinOutputFrame.setStyleSheet(PB1_View.standard.highBackground)
        else:
            PB1_View.pinFrame.pinLine.setStyleSheet(PB1_View.standard.low)
            PB1_View.pinFrame.pinOutputFrame.setStyleSheet(PB1_View.standard.lowBackground)
