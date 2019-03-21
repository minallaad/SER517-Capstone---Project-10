# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QSplitter, QApplication, QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt

import Components.Register_Values
import Components.List_of_Registers
import Components.ATMega_Block_Diagram
import Components.stackedWidget
import Components.ViewFactory

class PIN_Diagram(QtWidgets.QWidget):

    rightFrame = None
    stackedLayout = None

    def __init__(self):
        super(PIN_Diagram, self).__init__()

        if self.rightFrame == None:
            self.rightFrame = QFrame()

            simulatorFont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
            simulatorTitle = QtWidgets.QLabel(self)
            simulatorTitle.setText("ATMega328p")
            simulatorTitle.setStyleSheet('color : white')
            simulatorTitle.setAlignment(Qt.AlignCenter)
            simulatorTitle.setFont(simulatorFont)

            simulatorFrame = QFrame()
            simulatorFrame.setStyleSheet("QWidget { background-color: black }")
            simulatorFrame.setLineWidth(3)
            simulatorFrame.setMidLineWidth(3)
            simulatorFrame.mousePressEvent = PIN_Diagram.microcontrollerClicked
            simulatorFrame.setFrameShape(QFrame.Panel)
            simulatorFrame.setFixedSize(250, 450)
            simulatorFrame.layout = QHBoxLayout()
            simulatorFrame.layout.addWidget(simulatorTitle)

            simulatorFrame.setFrameShadow(simulatorFrame.Raised)
            simulatorFrame.setLayout(simulatorFrame.layout)

            pinFont = QtGui.QFont("Arial", 9, QtGui.QFont.Bold)

            pinsl = ['PD0', 'PD1', 'PD2', 'PD3', 'PD4', 'PD5', 'PD6', 'PB3', 'PB4', 'PB5', 'PB6']

            leftPinFrame = QFrame()
            leftPinFrame.layout = QVBoxLayout()
            leftPinFrame.layout.setAlignment(Qt.AlignRight)
            leftPinFrame.layout.addStretch()

            pinl_dict = {}
            #.itemClicked.connect(self.Clicked)

            for i in pinsl:
                pinl_dict[i] = QtWidgets.QPushButton(self)

                pinl_dict[i].setText(i)
                pinl_dict[i].setStyleSheet('color : dark grey')
                pinl_dict[i].setEnabled(False)
                # pinl_dict[i].setAlignment(Qt.AlignRight)
                pinl_dict[i].setFixedSize(30, 30)
                pinl_dict[i].setFont(pinFont)
                pinl_dict[i].clicked.connect(lambda state , x=i : self.portClicked(x))
                leftPinFrame.layout.setSpacing(10)
                leftPinFrame.layout.addWidget(pinl_dict[i])

            leftPinFrame.setLayout(leftPinFrame.layout)
            leftPinFrame.layout.addStretch()

            rightPinFrame = QFrame()
            rightPinFrame.layout = QVBoxLayout()
            rightPinFrame.layout.setAlignment(Qt.AlignLeft)
            rightPinFrame.layout.addStretch()

            pinsr = ['PC6', 'PC5', 'PC4', 'PC3', 'PC2', 'PC1', 'PC0', 'PB1', 'PB2', 'VCC', 'GND']
            pinr_dict = {}

            for i in pinsr:
                pinr_dict[i] = QtWidgets.QPushButton(self)

                pinr_dict[i].setText(i)
                pinr_dict[i].setStyleSheet('color : dark grey')
                pinr_dict[i].setEnabled(False)
                pinr_dict[i].setFixedSize(30, 30)
                pinr_dict[i].setFont(pinFont)
                pinr_dict[i].clicked.connect(lambda state , x = i : self.portClicked(x))
                rightPinFrame.layout.setSpacing(10)
                rightPinFrame.layout.addWidget(pinr_dict[i])

            rightPinFrame.layout.addStretch()
            rightPinFrame.setLayout(rightPinFrame.layout)

            pinl_dict['PD0'].setStyleSheet('color : red')
            pinl_dict['PD0'].setEnabled(True)
            pinl_dict['PD1'].setStyleSheet('color : green')
            pinl_dict['PD1'].setEnabled(True)

            self.rightFrame.setFrameShape(QFrame.StyledPanel)
            self.rightFrame.layout = QHBoxLayout()
            self.rightFrame.layout.addWidget(leftPinFrame)
            self.rightFrame.layout.addWidget(simulatorFrame)
            self.rightFrame.layout.addWidget(rightPinFrame)
            self.rightFrame.setLayout(self.rightFrame.layout)


    def getPIN_Digram(self):
        return self.rightFrame


    def microcontrollerClicked(self):
        blockDiagramFrame = Components.ATMega_Block_Diagram.Block_Diagram().getBlock_Digram()
        Components.stackedWidget.stackWidget.addWidget(blockDiagramFrame)
        Components.stackedWidget.stackWidget.incrementTopCount()



    def portClicked(self, port):  # On Click opens up port circuit diagram
        print(port)
        Components.Register_Values.Register_Values.clearList()
        Components.Register_Values.Register_Values.addRegister(port,"0X0b","0")
        Components.Register_Values.Register_Values.addRegister("DDRx", "0X0a", "0")
        pinFrame = Components.ViewFactory.ViewFactory.getView(port)
        print(type(pinFrame))
        Components.stackedWidget.stackWidget.addWidget(pinFrame)
        Components.stackedWidget.stackWidget.incrementTopCount()






