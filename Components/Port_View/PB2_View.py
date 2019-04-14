# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
from Components import pinLevelDiagram


class PB2_View(QtWidgets.QWidget):

    PB2Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PB2_View, self).__init__()

        if PB2_View.PB2Frame == None:
            PB2_View.PB2Frame = QFrame()

            PB2_View.standard = Components.Standard.value
            PB2_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PB2_View.pinFrame.setupUi(PB2_View.PB2Frame)


    @staticmethod
    def getViewFrame():
        return PB2_View.PB2Frame

    @staticmethod
    def getInstance():
        return PB2_View

    @staticmethod
    def setDDR(value):
        PB2_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            PB2_View.pinFrame.ddrLine1.setStyleSheet(PB2_View.standard.high)
            PB2_View.pinFrame.ddrLine2.setStyleSheet(PB2_View.standard.high)
        else:
            PB2_View.pinFrame.ddrLine1.setStyleSheet(PB2_View.standard.low)
            PB2_View.pinFrame.ddrLine2.setStyleSheet(PB2_View.standard.low)

    @staticmethod
    def setPort(value):
        PB2_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            PB2_View.pinFrame.portLine.setStyleSheet(PB2_View.standard.high)
        else:
            PB2_View.pinFrame.portLine.setStyleSheet(PB2_View.standard.low)

    @staticmethod
    def setPin(value):
        if value == 1:
            PB2_View.pinFrame.pinLine.setStyleSheet(PB2_View.standard.high)
            PB2_View.pinFrame.pinOutputFrame.setStyleSheet(PB2_View.standard.highBackground)
        else:
            PB2_View.pinFrame.pinLine.setStyleSheet(PB2_View.standard.low)
            PB2_View.pinFrame.pinOutputFrame.setStyleSheet(PB2_View.standard.lowBackground)

