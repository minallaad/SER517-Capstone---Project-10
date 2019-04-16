# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
from Components import pinLevelDiagram


class PC5_View(QtWidgets.QWidget):

    PC5Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PC5_View, self).__init__()

        if PC5_View.PC5Frame == None:
            PC5_View.PC5Frame = QFrame()

            PC5_View.standard = Components.Standard.value
            PC5_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PC5_View.pinFrame.setupUi(PC5_View.PC5Frame)


    @staticmethod
    def getViewFrame():
        return PC5_View.PC5Frame

    @staticmethod
    def getInstance():
        return PC5_View

    @staticmethod
    def setDDR(value):
        PC5_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            PC5_View.pinFrame.ddrLine1.setStyleSheet(PC5_View.standard.high)
            PC5_View.pinFrame.ddrLine2.setStyleSheet(PC5_View.standard.high)
        else:
            PC5_View.pinFrame.ddrLine1.setStyleSheet(PC5_View.standard.low)
            PC5_View.pinFrame.ddrLine2.setStyleSheet(PC5_View.standard.low)

    @staticmethod
    def setPort(value):
        PC5_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            PC5_View.pinFrame.portLine.setStyleSheet(PC5_View.standard.high)
        else:
            PC5_View.pinFrame.portLine.setStyleSheet(PC5_View.standard.low)

    @staticmethod
    def setPin(value):
        if value == 1:
            PC5_View.pinFrame.pinLine.setStyleSheet(PC5_View.standard.high)
            PC5_View.pinFrame.pinOutputFrame.setStyleSheet(PC5_View.standard.highBackground)
        else:
            PC5_View.pinFrame.pinLine.setStyleSheet(PC5_View.standard.low)
            PC5_View.pinFrame.pinOutputFrame.setStyleSheet(PC5_View.standard.lowBackground)