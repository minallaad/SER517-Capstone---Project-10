# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from Components import pinLevelDiagram
from PyQt5.QtCore import Qt

import Components.stackedWidget


class PD2_View(QtWidgets.QWidget):

    PD2Frame = None
    pinFrame = None

    def __init__(self):
        super(PD2_View, self).__init__()

        if PD2_View.PD1Frame == None:
            # self.rightFrame = None

            PD2_View.PD1Frame = QFrame()
            print("Now here")

            # self.rightFrame = QFrame()

            PD2_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PD2_View.pinFrame.setupUi(PD2_View.PD2Frame)


            # simulatorFont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
            # simulatorTitle = QtWidgets.QLabel(self)
            # simulatorTitle.setText("Port PD2")
            # simulatorTitle.setAlignment(Qt.AlignCenter)
            # simulatorTitle.setFont(simulatorFont)
            # simulatorTitle.setAlignment(Qt.AlignCenter)
            #
            # simulatorFrame = QFrame()
            # simulatorFrame.setStyleSheet("QWidget { background-color: black }")
            # simulatorFrame.setLineWidth(3)
            # simulatorFrame.setMidLineWidth(3)
            # simulatorFrame.setFrameShape(QFrame.Panel)
            # simulatorFrame.setFixedSize(250, 450)
            # simulatorFrame.layout = QHBoxLayout()
            # simulatorFrame.layout.addWidget(simulatorTitle)
            #
            # simulatorFrame.setFrameShadow(simulatorFrame.Raised)
            # simulatorFrame.setLayout(simulatorFrame.layout)
            #
            # PD2_View.PD1Frame.setFrameShape(QFrame.StyledPanel)
            # PD2_View.PD1Frame.layout = QHBoxLayout()
            # PD2_View.PD1Frame.layout.addWidget(simulatorFrame)
            # PD2_View.PD1Frame.setLayout(self.PD1Frame.layout)

    @staticmethod
    def getPD1ViewDiagram():
        return PD2_View.PD2Frame

    @staticmethod
    def getInstance():
        return PD2_View

    @staticmethod
    def setDDR(value):
        PD2_View.pinFrame.ddrValueLabel.setText(str(value))
        if value == 1:
            PD2_View.pinFrame.ddrLine1.setStyleSheet('color : green')
            PD2_View.pinFrame.ddrLine2.setStyleSheet('color : green')
        else:
            PD2_View.pinFrame.ddrLine1.setStyleSheet('color : red')
            PD2_View.pinFrame.ddrLine2.setStyleSheet('color : red')

    @staticmethod
    def setPort(value):
        if value == 1:
            PD2_View.pinFrame.portLine.setStyleSheet('color : green')
        else:
            PD2_View.pinFrame.portLine.setStyleSheet('color : red')

    @staticmethod
    def setPin(value):
        PD2_View.pinFrame.pinLine.setText(str(value))

        if value == 1:
            PD2_View.pinFrame.pinLine.setStyleSheet('color : green')
            PD2_View.pinFrame.pinOutputFrame.setStyleSheet("background-color: green;")
            print('here2', value)
        else:
            PD2_View.pinFrame.pinLine.setStyleSheet('color : green')
            PD2_View.pinFrame.pinOutputFrame.setStyleSheet("background-color: red;")
    # def getLayout(self):
    #     print("Here")
    #     Components.stackedWidget.stackWidget.addWidget(self.PD1Frame)
    #     Components.stackedWidget.stackWidget.incrementTopCount()







