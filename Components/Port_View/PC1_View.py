# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
from Components import pinLevelDiagram


class PC1_View(QtWidgets.QWidget):

    PC1Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PC1_View, self).__init__()

        if PC1_View.PC1Frame == None:
            PC1_View.PC1Frame = QFrame()

            PC1_View.standard = Components.Standard.value
            PC1_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PC1_View.pinFrame.setupUi(PC1_View.PC1Frame)


    @staticmethod
    def getViewFrame():
        return PC1_View.PC1Frame

    @staticmethod
    def getInstance():
        return PC1_View

    @staticmethod
    def setDDR(value):
        PC1_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            PC1_View.pinFrame.ddrLine1.setStyleSheet(PC1_View.standard.high)
            PC1_View.pinFrame.ddrLine2.setStyleSheet(PC1_View.standard.high)
        else:
            PC1_View.pinFrame.ddrLine1.setStyleSheet(PC1_View.standard.low)
            PC1_View.pinFrame.ddrLine2.setStyleSheet(PC1_View.standard.low)

    @staticmethod
    def setPort(value):
        PC1_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            PC1_View.pinFrame.portLine.setStyleSheet(PC1_View.standard.high)
        else:
            PC1_View.pinFrame.portLine.setStyleSheet(PC1_View.standard.low)

    @staticmethod
    def setPin(value):
        if value == 1:
            PC1_View.pinFrame.pinLine.setStyleSheet(PC1_View.standard.high)
            PC1_View.pinFrame.pinOutputFrame.setStyleSheet(PC1_View.standard.highBackground)
        else:
            PC1_View.pinFrame.pinLine.setStyleSheet(PC1_View.standard.low)
            PC1_View.pinFrame.pinOutputFrame.setStyleSheet(PC1_View.standard.lowBackground)