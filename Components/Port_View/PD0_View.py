# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
from Components import pinLevelDiagram


class PD0_View(QtWidgets.QWidget):

    PD0Frame = None
    pinFrame = None

    def __init__(self):
        super(PD0_View, self).__init__()

        if PD0_View.PD0Frame == None:
            PD0_View.PD0Frame = QFrame()

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
    def setDDR(value):
        PD0_View.pinFrame.ddrValueLabel.setText(value)



    # def getPortDiagramLayout(self):
    #     print("Here")
    #     Components.stackedWidget.stackWidget.addWidget(self.PD1Frame)
    #     Components.stackedWidget.stackWidget.incrementTopCount()







