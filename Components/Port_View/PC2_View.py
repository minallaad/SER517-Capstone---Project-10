# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
from Components import pinLevelDiagram


class PC2_View(QtWidgets.QWidget):

    PC2Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PC2_View, self).__init__()

        if PC2_View.PC2Frame == None:
            PC2_View.PC2Frame = QFrame()

            PC2_View.standard = Components.Standard.value
            PC2_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PC2_View.pinFrame.setupUi(PC2_View.PC2Frame)


    @staticmethod
    def getViewFrame():
        return PC2_View.PC2Frame

    @staticmethod
    def getInstance():
        return PC2_View

    @staticmethod
    def setDDR(value):
        PC2_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            PC2_View.pinFrame.ddrLine1.setStyleSheet(PC2_View.standard.high)
            PC2_View.pinFrame.ddrLine2.setStyleSheet(PC2_View.standard.high)
        else:
            PC2_View.pinFrame.ddrLine1.setStyleSheet(PC2_View.standard.low)
            PC2_View.pinFrame.ddrLine2.setStyleSheet(PC2_View.standard.low)

    @staticmethod
    def setPort(value):
        PC2_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            PC2_View.pinFrame.portLine.setStyleSheet(PC2_View.standard.high)
        else:
            PC2_View.pinFrame.portLine.setStyleSheet(PC2_View.standard.low)

    @staticmethod
    def setPin(value):
        if value == 1:
            PC2_View.pinFrame.pinLine.setStyleSheet(PC2_View.standard.high)
            PC2_View.pinFrame.pinOutputFrame.setStyleSheet(PC2_View.standard.highBackground)
        else:
            PC2_View.pinFrame.pinLine.setStyleSheet(PC2_View.standard.low)
            PC2_View.pinFrame.pinOutputFrame.setStyleSheet(PC2_View.standard.lowBackground)
