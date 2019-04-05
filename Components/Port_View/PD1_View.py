# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
from Components import pinLevelDiagram


class PD1_View(QtWidgets.QWidget):

    PD1Frame = None

    def __init__(self):
        super(PD1_View, self).__init__()

        if PD1_View.PD1Frame == None:
            # self.rightFrame = None

            PD1_View.PD1Frame = QFrame()
            print("Now here")

            PD1_View.pinFrame = pinLevelDiagram.Ui_Frame()
            PD1_View.pinFrame.setupUi(PD1_View.PD1Frame)

            # simulatorFont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
            # simulatorTitle = QtWidgets.QLabel(self)
            # simulatorTitle.setText("Port PD1")
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
            # PD1_View.PD1Frame.setFrameShape(QFrame.StyledPanel)
            # PD1_View.PD1Frame.layout = QHBoxLayout()
            # PD1_View.PD1Frame.layout.addWidget(simulatorFrame)
            # PD1_View.PD1Frame.setLayout(self.PD1Frame.layout)

    @staticmethod
    def getPD1ViewDiagram():
        return PD1_View.PD1Frame

    @staticmethod
    def getInstance():
        return PD1_View

    @staticmethod
    def setDDR(value):
        PD1_View.pinFrame.ddrValueLabel.setText(str(value))


    # def getLayout(self):
    #     print("Here")
    #     Components.stackedWidget.stackWidget.addWidget(self.PD1Frame)
    #     Components.stackedWidget.stackWidget.incrementTopCount()







