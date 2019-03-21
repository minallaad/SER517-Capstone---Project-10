# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QFrame, QVBoxLayout
from PyQt5.QtCore import Qt

import Components.stackedWidget
import Components.ViewFactory


class Block_Diagram(QtWidgets.QWidget):

    rightFrame = None

    def __init__(self):
        super(Block_Diagram, self).__init__()

        if Block_Diagram.rightFrame == None:
            Block_Diagram.rightFrame = QFrame()

            simulatorFont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
            simulatorTitle = QtWidgets.QLabel(self)
            simulatorTitle.setText("ATMega328p Block Diagram")
            simulatorTitle.setStyleSheet('color : Black')
            simulatorTitle.setAlignment(Qt.AlignCenter)
            simulatorTitle.setFont(simulatorFont)

            Block_Diagram.rightFrame.setFrameShape(QFrame.StyledPanel)
            Block_Diagram.rightFrame.layout = QVBoxLayout()
            Block_Diagram.rightFrame.layout.addWidget(simulatorTitle)
            Block_Diagram.rightFrame.setLayout(self.rightFrame.layout)


    @staticmethod
    def getBlock_Digram():
        return Block_Diagram.rightFrame







