# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
from Components import pinLevelDiagram


class PC7_View(QtWidgets.QWidget):

    PC7Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PC7_View, self).__init__()

        if PC7_View.PC7Frame == None:
            PC7_View.PC7Frame = QFrame()

            PC7_View.standard = Components.Standard.value
            PC7_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PC7_View.pinFrame.setupUi(PC7_View.PC7Frame)


    @staticmethod
    def getViewFrame():
        return PC7_View.PC7Frame

    @staticmethod
    def getInstance():
        return PC7_View

    @staticmethod
    def setDDR(value):
        PC7_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            PC7_View.pinFrame.ddrLine1.setStyleSheet(PC7_View.standard.high)
            PC7_View.pinFrame.ddrLine2.setStyleSheet(PC7_View.standard.high)
        else:
            PC7_View.pinFrame.ddrLine1.setStyleSheet(PC7_View.standard.low)
            PC7_View.pinFrame.ddrLine2.setStyleSheet(PC7_View.standard.low)

    @staticmethod
    def setPort(value):
        PC7_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            PC7_View.pinFrame.portLine.setStyleSheet(PC7_View.standard.high)
            print('here2', value)
        else:
            PC7_View.pinFrame.portLine.setStyleSheet(PC7_View.standard.low)

    @staticmethod
    def setPin(value):
        if value == 1:
            PC7_View.pinFrame.pinLine.setStyleSheet(PC7_View.standard.high)
            PC7_View.pinFrame.pinOutputFrame.setStyleSheet(PC7_View.standard.highBackground)
            print('here2', value)
        else:
            PC7_View.pinFrame.pinLine.setStyleSheet(PC7_View.standard.low)
            PC7_View.pinFrame.pinOutputFrame.setStyleSheet(PC7_View.standard.lowBackground)









