# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
from Components import pinLevelDiagram


class PD1_View(QtWidgets.QWidget):

    PD1Frame = None
    standard = None

    def __init__(self):
        super(PD1_View, self).__init__()

        if PD1_View.PD1Frame == None:

            PD1_View.standard = Components.Standard.value
            PD1_View.PD1Frame = QFrame()

            PD1_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PD1_View.pinFrame.setupUi(PD1_View.PD1Frame)


    @staticmethod
    def getViewFrame():
        return PD1_View.PD1Frame

    @staticmethod
    def getInstance():
        return PD1_View

    @staticmethod
    def setDDR(value):
        PD1_View.pinFrame.ddrValueLabel.setText(str(value))
        if value == 1:
            PD1_View.pinFrame.ddrLine1.setStyleSheet(PD1_View.standard.high)
            PD1_View.pinFrame.ddrLine2.setStyleSheet(PD1_View.standard.high)
        else:
            PD1_View.pinFrame.ddrLine1.setStyleSheet(PD1_View.standard.low)
            PD1_View.pinFrame.ddrLine2.setStyleSheet(PD1_View.standard.low)

    @staticmethod
    def setPort(value):
        PD1_View.pinFrame.portValueLabel.setText(str(value))
        if value == 1:
            PD1_View.pinFrame.portLine.setStyleSheet(PD1_View.standard.high)
        else:
            PD1_View.pinFrame.portLine.setStyleSheet(PD1_View.standard.low)

    @staticmethod
    def setPin(value):
        if value == 1:
            PD1_View.pinFrame.pinLine.setStyleSheet(PD1_View.standard.high)
            PD1_View.pinFrame.pinOutputFrame.setStyleSheet(PD1_View.standard.highBackground)
        else:
            PD1_View.pinFrame.pinLine.setStyleSheet(PD1_View.standard.low)
            PD1_View.pinFrame.pinOutputFrame.setStyleSheet(PD1_View.standard.lowBackground)
