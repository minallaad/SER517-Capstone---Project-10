# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QSplitter, QApplication, QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, \
    QScrollArea, QListWidget, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt

import Components.Register_Values
import Components.List_of_Registers


class PIN_Diagram(QtWidgets.QWidget):

    rightFrame = None

    def __init__(self):
        super(PIN_Diagram, self).__init__()

        if self.rightFrame == None:
            self.rightFrame = QFrame()

            simulatorFont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
            simulatorTitle = QtWidgets.QLabel(self)
            simulatorTitle.setText("ATMega328p")
            simulatorTitle.setAlignment(Qt.AlignCenter)
            simulatorTitle.setFont(simulatorFont)
            simulatorTitle.setAlignment(Qt.AlignCenter)

            simulatorFrame = QFrame()
            simulatorFrame.setStyleSheet("QWidget { background-color: silver }")
            simulatorFrame.setLineWidth(3)
            simulatorFrame.setMidLineWidth(3)
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
                # pinl_dict[i].setAlignment(Qt.AlignRight)
                pinl_dict[i].setFixedSize(30, 30)
                pinl_dict[i].setFont(pinFont)
                pinl_dict[i].clicked.connect(self.Clicked)
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
                pinr_dict[i].setFixedSize(30, 30)
                pinr_dict[i].setFont(pinFont)
                pinr_dict[i].clicked.connect(self.Clicked)
                rightPinFrame.layout.setSpacing(10)
                rightPinFrame.layout.addWidget(pinr_dict[i])

            rightPinFrame.layout.addStretch()
            rightPinFrame.setLayout(rightPinFrame.layout)

            pinl_dict['PD0'].setStyleSheet('color : red')
            pinl_dict['PD1'].setStyleSheet('color : red')
            pinl_dict['PD2'].setStyleSheet('color : red')

            pinr_dict['PC6'].setStyleSheet('color : green')
            pinr_dict['PC5'].setStyleSheet('color : green')
            pinr_dict['PC4'].setStyleSheet('color : green')

            self.rightFrame.setFrameShape(QFrame.StyledPanel)
            self.rightFrame.layout = QHBoxLayout()
            self.rightFrame.layout.addWidget(leftPinFrame)
            self.rightFrame.layout.addWidget(simulatorFrame)
            self.rightFrame.layout.addWidget(rightPinFrame)
            self.rightFrame.setLayout(self.rightFrame.layout)



    def getPIN_Digram(self):
        return self.rightFrame

    def Clicked(self, item):  # On Click Register name calls this function
        QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Landing()
    sys.exit(app.exec_())

