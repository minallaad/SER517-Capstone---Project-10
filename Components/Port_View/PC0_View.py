# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
from Components import pinLevelDiagram


class PC0_View(QtWidgets.QWidget):

    PC0Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PC0_View, self).__init__()

        if PC0_View.PC0Frame == None:
            PC0_View.PC0Frame = QFrame()

            PC0_View.standard = Components.Standard.value
            PC0_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PC0_View.pinFrame.setupUi(PC0_View.PC0Frame)


    @staticmethod
    def getViewFrame():
        return PC0_View.PC0Frame

    @staticmethod
    def getInstance():
        return PC0_View

    @staticmethod
    def setDDR(value):
        PC0_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            PC0_View.pinFrame.ddrLine1.setStyleSheet(PC0_View.standard.high)
            PC0_View.pinFrame.ddrLine2.setStyleSheet(PC0_View.standard.high)
        else:
            PC0_View.pinFrame.ddrLine1.setStyleSheet(PC0_View.standard.low)
            PC0_View.pinFrame.ddrLine2.setStyleSheet(PC0_View.standard.low)

    @staticmethod
    def setPort(value):
        PC0_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            PC0_View.pinFrame.portLine.setStyleSheet(PC0_View.standard.high)
        else:
            PC0_View.pinFrame.portLine.setStyleSheet(PC0_View.standard.low)

    @staticmethod
    def setPin(value):
        if value == 1:
            PC0_View.pinFrame.pinLine.setStyleSheet(PC0_View.standard.high)
            PC0_View.pinFrame.pinOutputFrame.setStyleSheet(PC0_View.standard.highBackground)
        else:
            PC0_View.pinFrame.pinLine.setStyleSheet(PC0_View.standard.low)
            PC0_View.pinFrame.pinOutputFrame.setStyleSheet(PC0_View.standard.lowBackground)