# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
from Components import pinLevelDiagram


class PB0_View(QtWidgets.QWidget):

    PB0Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PB0_View, self).__init__()

        if PB0_View.PB0Frame == None:
            PB0_View.PB0Frame = QFrame()

            PB0_View.standard = Components.Standard.value
            PB0_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PB0_View.pinFrame.setupUi(PB0_View.PB0Frame)


    @staticmethod
    def getViewFrame():
        return PB0_View.PB0Frame

    @staticmethod
    def getInstance():
        return PB0_View

    @staticmethod
    def setDDR(value):
        PB0_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            PB0_View.pinFrame.ddrLine1.setStyleSheet(PB0_View.standard.high)
            PB0_View.pinFrame.ddrLine2.setStyleSheet(PB0_View.standard.high)
        else:
            PB0_View.pinFrame.ddrLine1.setStyleSheet(PB0_View.standard.low)
            PB0_View.pinFrame.ddrLine2.setStyleSheet(PB0_View.standard.low)

    @staticmethod
    def setPort(value):
        PB0_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            PB0_View.pinFrame.portLine.setStyleSheet(PB0_View.standard.high)
        else:
            PB0_View.pinFrame.portLine.setStyleSheet(PB0_View.standard.low)

    @staticmethod
    def setPin(value):
        if value == 1:
            PB0_View.pinFrame.pinLine.setStyleSheet(PB0_View.standard.high)
            PB0_View.pinFrame.pinOutputFrame.setStyleSheet(PB0_View.standard.highBackground)
        else:
            PB0_View.pinFrame.pinLine.setStyleSheet(PB0_View.standard.low)
            PB0_View.pinFrame.pinOutputFrame.setStyleSheet(PB0_View.standard.lowBackground)
