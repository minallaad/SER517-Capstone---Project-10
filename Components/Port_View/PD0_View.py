# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt


import Components.stackedWidget
import Components.Standard
from Components import pinLevelDiagram



class PD0_View(QtWidgets.QWidget):

    PD0Frame = None
    pinFrame = None
    standard = None

    def __init__(self):
        super(PD0_View, self).__init__()

        if PD0_View.PD0Frame == None:
            PD0_View.PD0Frame = QFrame()

            PD0_View.standard =  Components.Standard.value
            PD0_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PD0_View.pinFrame.setupUi(PD0_View.PD0Frame)


            # simPD0FrameulatorFont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
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
            # PD0_View.PD0Frame.setFrameShape(QFrame.StyledPanel)
            # PD0_View.PD0Frame.layout = QHBoxLayout()
            # PD0_View.PD0Frame.layout.addWidget(simulatorFrame)
            # PD0_View.PD0Frame.setLayout(PD0_View.PD0Frame.layout)



    @staticmethod
    def getPD0ViewDiagram():
        return PD0_View.PD0Frame

    @staticmethod
    def getInstance():
        return PD0_View

    @staticmethod
    def setDDR(value):
        PD0_View.pinFrame.ddrValueLabel.setText(str(value))

        if value == 1:
            PD0_View.pinFrame.ddrLine1.setStyleSheet(PD0_View.standard.high)
            PD0_View.pinFrame.ddrLine2.setStyleSheet(PD0_View.standard.high)
        else:
            PD0_View.pinFrame.ddrLine1.setStyleSheet(PD0_View.standard.low)
            PD0_View.pinFrame.ddrLine2.setStyleSheet(PD0_View.standard.low)

    @staticmethod
    def setPort(value):
        PD0_View.pinFrame.portValueLabel.setText(str(value))

        if value == 1:
            PD0_View.pinFrame.portLine.setStyleSheet(PD0_View.standard.high)
            print('here2', value)
        else:
            PD0_View.pinFrame.portLine.setStyleSheet(PD0_View.standard.low)

    @staticmethod
    def setPin(value):
        if value == 1:
            PD0_View.pinFrame.pinLine.setStyleSheet(PD0_View.standard.high)
            PD0_View.pinFrame.pinOutputFrame.setStyleSheet(PD0_View.standard.highBackground)
            print('here2', value)
        else:
            PD0_View.pinFrame.pinLine.setStyleSheet(PD0_View.standard.low)
            PD0_View.pinFrame.pinOutputFrame.setStyleSheet(PD0_View.standard.lowBackground)


    # def getPortDiagramLayout(self):
    #     print("Here")
    #     Components.stackedWidget.stackWidget.addWidget(self.PD1Frame)
    #     Components.stackedWidget.stackWidget.incrementTopCount()







