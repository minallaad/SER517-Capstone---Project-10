# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
from Components import pinLevelDiagram


class PC6_View(QtWidgets.QWidget):

    PC6Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PC6_View, self).__init__()

        if PC6_View.PC6Frame == None:
            PC6_View.PC6Frame = QFrame()

            PC6_View.standard = Components.Standard.value
            PC6_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PC6_View.pinFrame.setupUi(PC6_View.PC6Frame)


    @staticmethod
    def getViewFrame():
        return PC6_View.PC6Frame

    @staticmethod
    def getInstance():
        return PC6_View

    @staticmethod
    def setDDR(value):
        PC6_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            PC6_View.pinFrame.ddrLine1.setStyleSheet(PC6_View.standard.high)
            PC6_View.pinFrame.ddrLine2.setStyleSheet(PC6_View.standard.high)
        else:
            PC6_View.pinFrame.ddrLine1.setStyleSheet(PC6_View.standard.low)
            PC6_View.pinFrame.ddrLine2.setStyleSheet(PC6_View.standard.low)

    @staticmethod
    def setPort(value):
        PC6_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            PC6_View.pinFrame.portLine.setStyleSheet(PC6_View.standard.high)
        else:
            PC6_View.pinFrame.portLine.setStyleSheet(PC6_View.standard.low)

    @staticmethod
    def setPin(value):
        if value == 1:
            PC6_View.pinFrame.pinLine.setStyleSheet(PC6_View.standard.high)
            PC6_View.pinFrame.pinOutputFrame.setStyleSheet(PC6_View.standard.highBackground)
        else:
            PC6_View.pinFrame.pinLine.setStyleSheet(PC6_View.standard.low)
            PC6_View.pinFrame.pinOutputFrame.setStyleSheet(PC6_View.standard.lowBackground)