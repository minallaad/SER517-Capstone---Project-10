# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
from Components import pinLevelDiagram


class PC3_View(QtWidgets.QWidget):

    PC3Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PC3_View, self).__init__()

        if PC3_View.PC3Frame == None:
            PC3_View.PC3Frame = QFrame()

            PC3_View.standard = Components.Standard.value
            PC3_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PC3_View.pinFrame.setupUi(PC3_View.PC3Frame)


    @staticmethod
    def getViewFrame():
        return PC3_View.PC3Frame

    @staticmethod
    def getInstance():
        return PC3_View

    @staticmethod
    def setDDR(value):
        PC3_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            PC3_View.pinFrame.ddrLine1.setStyleSheet(PC3_View.standard.high)
            PC3_View.pinFrame.ddrLine2.setStyleSheet(PC3_View.standard.high)
        else:
            PC3_View.pinFrame.ddrLine1.setStyleSheet(PC3_View.standard.low)
            PC3_View.pinFrame.ddrLine2.setStyleSheet(PC3_View.standard.low)

    @staticmethod
    def setPort(value):
        PC3_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            PC3_View.pinFrame.portLine.setStyleSheet(PC3_View.standard.high)
        else:
            PC3_View.pinFrame.portLine.setStyleSheet(PC3_View.standard.low)

    @staticmethod
    def setPin(value):
        if value == 1:
            PC3_View.pinFrame.pinLine.setStyleSheet(PC3_View.standard.high)
            PC3_View.pinFrame.pinOutputFrame.setStyleSheet(PC3_View.standard.highBackground)
        else:
            PC3_View.pinFrame.pinLine.setStyleSheet(PC3_View.standard.low)
            PC3_View.pinFrame.pinOutputFrame.setStyleSheet(PC3_View.standard.lowBackground)