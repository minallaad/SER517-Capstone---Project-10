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

    def __init__(self):
        super(PC7_View, self).__init__()

        if PC7_View.PC7Frame == None:
            PC7_View.PC7Frame = QFrame()

            PC7_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PC7_View.pinFrame.setupUi(PC7_View.PC7Frame)


            # simPC7FrameulatorFont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
            # simulatorTitle = QtWidgets.QLabel(self)
            # simulatorTitle.setText("Port PD0")
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
            # PC7_View.PC7Frame.setFrameShape(QFrame.StyledPanel)
            # PC7_View.PC7Frame.layout = QHBoxLayout()
            # PC7_View.PC7Frame.layout.addWidget(simulatorFrame)
            # PC7_View.PC7Frame.setLayout(PC7_View.PC7Frame.layout)



    @staticmethod
    def getPC7ViewDiagram():
        return PC7_View.PC7Frame

    @staticmethod
    def getInstance():
        return PC7_View

    @staticmethod
    def setDDR(value):
        PC7_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            PC7_View.pinFrame.ddrLine1.setStyleSheet("color : green")
            PC7_View.pinFrame.ddrLine2.setStyleSheet("color : green")
        else:
            PC7_View.pinFrame.ddrLine1.setStyleSheet("color : red")
            PC7_View.pinFrame.ddrLine2.setStyleSheet("color : red")

    @staticmethod
    def setPort(value):
        PC7_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            PC7_View.pinFrame.portLine.setStyleSheet('color : green')
            print('here2', value)
        else:
            PC7_View.pinFrame.portLine.setStyleSheet('color : red')

    @staticmethod
    def setPin(value):
        if value == 1:
            PC7_View.pinFrame.pinLine.setStyleSheet('color : green')
            PC7_View.pinFrame.pinOutputFrame.setStyleSheet("background-color: green;")
            print('here2', value)
        else:
            PC7_View.pinFrame.pinLine.setStyleSheet('color : red')
            PC7_View.pinFrame.pinOutputFrame.setStyleSheet("background-color: red;")


    # def getPortDiagramLayout(self):
    #     print("Here")
    #     Components.stackedWidget.stackWidget.addWidget(self.PD1Frame)
    #     Components.stackedWidget.stackWidget.incrementTopCount()







