# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPainter, QPen

from PyQt5.QtWidgets import QWidget, QLabel, QSplitter, QApplication, QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt

import Components.Register_Values
import Components.List_of_Registers
import Components.stackedWidget
import Components.ViewFactory
import Components.ATMega_Block_Diagram
import Components.Globalmap

from Components import ATMega_Block_Diagram



class PIN_Diagram(QtWidgets.QWidget):
    rightFrame = None
    stackedLayout = None
    pinr_dict = {}
    pinl_dict = {}

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

            # .itemClicked.connect(self.Clicked)

            for i in pinsl:
                self.pinl_dict[i] = QtWidgets.QPushButton(self)

                self.pinl_dict[i].setText(i)
                self.pinl_dict[i].setStyleSheet('color : dark grey')
                self.pinl_dict[i].setEnabled(False)
                # pinl_dict[i].setAlignment(Qt.AlignRight)
                self.pinl_dict[i].setFixedSize(30, 30)
                self.pinl_dict[i].setFont(pinFont)
                self.pinl_dict[i].clicked.connect(lambda state, x=i: self.portClicked(x))
                leftPinFrame.layout.setSpacing(10)
                leftPinFrame.layout.addWidget(self.pinl_dict[i])

            leftPinFrame.setLayout(leftPinFrame.layout)
            leftPinFrame.layout.addStretch()

            rightPinFrame = QFrame()
            rightPinFrame.layout = QVBoxLayout()
            rightPinFrame.layout.setAlignment(Qt.AlignLeft)
            rightPinFrame.layout.addStretch()

            pinsr = ['PC6', 'PC5', 'PC4', 'PC3', 'PC2', 'PC1', 'PC0', 'PB1', 'PB2', 'VCC', 'GND']

            for i in pinsr:
                self.pinr_dict[i] = QtWidgets.QPushButton(self)

                self.pinr_dict[i].setText(i)
                self.pinr_dict[i].setStyleSheet('color : dark grey')
                self.pinr_dict[i].setEnabled(False)
                self.pinr_dict[i].setFixedSize(30, 30)
                self.pinr_dict[i].setFont(pinFont)
                self.pinr_dict[i].clicked.connect(lambda state, x=i: self.portClicked(x))
                rightPinFrame.layout.setSpacing(10)
                rightPinFrame.layout.addWidget(self.pinr_dict[i])

            rightPinFrame.layout.addStretch()
            rightPinFrame.setLayout(rightPinFrame.layout)
            #enable pin clicks for left
            for val in pinsl:
                self.pinl_dict[val].setEnabled(True)
                self.pinl_dict[val].setStyleSheet('color : red')

            # enable pin clicks for left
            for val in pinsl:
                self.pinl_dict[val].setEnabled(True)
                self.pinl_dict[val].setStyleSheet('color : red')

            # enable pin clicks for right
            for val in pinsr:
                self.pinr_dict[val].setEnabled(True)
                self.pinr_dict[val].setStyleSheet('color : red')

            self.rightFrame.setFrameShape(QFrame.StyledPanel)
            self.rightFrame.layout = QHBoxLayout()
            self.rightFrame.layout.addWidget(leftPinFrame)
            self.rightFrame.layout.addWidget(simulatorFrame)
            self.rightFrame.layout.addWidget(rightPinFrame)
            self.rightFrame.setLayout(self.rightFrame.layout)

    def getPIN_Digram(self):
        return self.rightFrame

    @staticmethod
    def setPinStatus(port, value):
        if value != "0":
            if port in PIN_Diagram.pinl_dict:
                PIN_Diagram.pinl_dict[port].setStyleSheet('color : green')
                # PIN_Diagram.pinl_dict[port].setFont(QtGui.QFont("Arial", 9, QtGui.QFont.ExtraBold))
            elif port in PIN_Diagram.pinr_dict:
                PIN_Diagram.pinr_dict[port].setStyleSheet('color : green')
                # PIN_Diagram.pinr_dict[port].setEnabled(True)

        else:
            if port in PIN_Diagram.pinl_dict:
                PIN_Diagram.pinl_dict[port].setStyleSheet('color : red')
                # PIN_Diagram.pinl_dict[port].setFont(QtGui.QFont("Arial", 5, QtGui.QFont.ExtraBold))
            elif port in PIN_Diagram.pinr_dict:
                PIN_Diagram.pinr_dict[port].setStyleSheet('color : red')
                # PIN_Diagram.pinr_dict[port].setEnabled(True)

    def microcontrollerClicked(self):
        print("micro")
        microcontrollerBlock = QFrame()
        blockDiagramFrame = ATMega_Block_Diagram.Ui_microcontrollerBlock()
        blockDiagramFrame.setupUi(microcontrollerBlock)
        blockDiagramFrame.eepromFrame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram, "EEPROM", ['EEPROM.EEARL', 'EEPROM.EEARH', 'EEPROM.EEDR', 'EEPROM.EECR'])
        blockDiagramFrame.gpiorFrame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "GPIOR")
        blockDiagramFrame.flashFrame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "FLASH")
        blockDiagramFrame.tc0Frame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "TIMER0")
        blockDiagramFrame.tc1Frame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "TIMER1")
        blockDiagramFrame.tc2Frame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "TIMER2")
        blockDiagramFrame.watchdogFrame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "WATCHDOG", [])
        blockDiagramFrame.spiFrame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "SPI", [])
        blockDiagramFrame.usartFrame.mousePressEvent = lambda x: PIN_Diagram.blockComponentClicked(PIN_Diagram,
                                                                                                    "UART0")
        Components.stackedWidget.stackWidget.addWidget(microcontrollerBlock)
        Components.stackedWidget.stackWidget.incrementTopCount()

    def portClicked(self, port):  # On Click opens up port circuit diagram
        print(port)
        Components.Register_Values.Register_Values.clearList()

        pinRegister = "PORT" + port[1] + ".PIN"
        pinValue = Components.Globalmap.Map.getValue(pinRegister)
        pinAddress = Components.Globalmap.Map.getRegisterAddress(pinRegister)


        ddrRegister = "PORT" + port[1] + ".DDR"
        ddrValue = Components.Globalmap.Map.getValue(ddrRegister)
        ddrAddress = Components.Globalmap.Map.getRegisterAddress(ddrRegister)

        portRegister = "PORT" + port[1] + ".PORT"
        portValue = Components.Globalmap.Map.getValue(portRegister)
        portAddress = Components.Globalmap.Map.getRegisterAddress(portRegister)

        if pinValue!=None:
            Components.Register_Values.Register_Values.addRegister(pinRegister, hex(pinAddress), pinValue)
        else:
            Components.Register_Values.Register_Values.addRegister(pinRegister, hex(pinAddress), "0")

        if ddrValue!=None:
            Components.Register_Values.Register_Values.addRegister(ddrRegister,hex(ddrAddress) , ddrValue)
        else:
            Components.Register_Values.Register_Values.addRegister(ddrRegister, hex(ddrAddress), "0")

        if portValue!=None:
            Components.Register_Values.Register_Values.addRegister(ddrRegister, hex(portAddress), portValue)
        else:
            Components.Register_Values.Register_Values.addRegister(ddrRegister, hex(portAddress), "0")

        #uncomment this code for showing pin diagrams
        pinFrame = Components.ViewFactory.ViewFactory.getView(port)
        print(type(pinFrame))
        Components.stackedWidget.stackWidget.addWidget(pinFrame)
        Components.stackedWidget.stackWidget.incrementTopCount()

    def blockComponentClicked(self, component, registers):
        frame = Components.ViewFactory.ViewFactory.getView(component)

        if frame != None:
            block = QFrame()
            frame.setupUi(block)
            Components.stackedWidget.stackWidget.addWidget(block)
            Components.stackedWidget.stackWidget.incrementTopCount()

        Components.Register_Values.Register_Values.clearList()
        for key in registers:
            registerAddress = Components.Globalmap.Map.getRegisterAddress(key)
            registerValue = Components.Globalmap.Map.getValue(key)
            Components.Register_Values.Register_Values.addRegister(key, hex(registerAddress), registerValue)





