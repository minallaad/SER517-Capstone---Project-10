# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
from Components import pinLevelDiagram


class PC4_View(QtWidgets.QWidget):

    PC4Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PC4_View, self).__init__()

        if PC4_View.PC4Frame == None:
            PC4_View.PC4Frame = QFrame()

            PC4_View.standard = Components.Standard.value
            PC4_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PC4_View.pinFrame.setupUi(PC4_View.PC4Frame)


    @staticmethod
    def getViewFrame():
        return PC4_View.PC4Frame

    @staticmethod
    def getInstance():
        return PC4_View

    @staticmethod
    def setDDR(value):
        PC4_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            PC4_View.pinFrame.ddrLine1.setStyleSheet(PC4_View.standard.high)
            PC4_View.pinFrame.ddrLine2.setStyleSheet(PC4_View.standard.high)
        else:
            PC4_View.pinFrame.ddrLine1.setStyleSheet(PC4_View.standard.low)
            PC4_View.pinFrame.ddrLine2.setStyleSheet(PC4_View.standard.low)

    @staticmethod
    def setPort(value):
        PC4_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            PC4_View.pinFrame.portLine.setStyleSheet(PC4_View.standard.high)
        else:
            PC4_View.pinFrame.portLine.setStyleSheet(PC4_View.standard.low)

    @staticmethod
    def setPin(value):
        if value == 1:
            PC4_View.pinFrame.pinLine.setStyleSheet(PC4_View.standard.high)
            PC4_View.pinFrame.pinOutputFrame.setStyleSheet(PC4_View.standard.highBackground)
        else:
            PC4_View.pinFrame.pinLine.setStyleSheet(PC4_View.standard.low)
            PC4_View.pinFrame.pinOutputFrame.setStyleSheet(PC4_View.standard.lowBackground)