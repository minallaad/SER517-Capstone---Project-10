# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QTableWidget , QTableWidgetItem
from PyQt5.QtCore import Qt, QRect

import Components.stackedWidget
from Components import pinLevelDiagram


class memoryDump(QtWidgets.QWidget):

    memoryDumpFrame = None

    def __init__(self):
        super(memoryDump, self).__init__()

        if memoryDump.memoryDumpFrame == None:
            memoryDump.memoryDumpFrame = QFrame()


            Font = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
            Font.setBold(True)
            Title = QtWidgets.QLabel(self)
            Title.setText("EEPROM Memory Dump")
            Title.setAlignment(Qt.AlignCenter)
            Title.setFont(Font)
            Title.setAlignment(Qt.AlignCenter)
            Title.setGeometry(QRect(290, 40, 191, 31))

            self.refreshButton = QtWidgets.QPushButton("Refresh")
            self.refreshButton.clicked.connect(lambda: self.reloadMemoryDump())

            headerfont = QtGui.QFont()
            headerfont.setFamily("Arial Black")
            headerfont.setPointSize(11)


            memoryDump.tableWidget = QTableWidget()
            memoryDump.tableWidget.setRowCount(2)
            memoryDump.tableWidget.setColumnCount(3)
            memoryDump.List = []



            memoryDump.tableWidget.setItem(0, 0, QTableWidgetItem("Address  (in hex)  "))
            memoryDump.tableWidget.setItem(0, 1, QTableWidgetItem("1 byte hexadecimal number (needs to be 16 of them)"))
            memoryDump.tableWidget.setItem(0, 2, QTableWidgetItem("Value"))

            #Comment this code when showing EEPROM memory dump at runtime
            memoryDump.tableWidget.setItem(1, 0, QTableWidgetItem("0X23"))
            memoryDump.tableWidget.setItem(1, 1, QTableWidgetItem(bin(0X23)))
            memoryDump.tableWidget.setItem(1, 2, QTableWidgetItem("A"))

            tableview = QtWidgets.QTableView()
            tableview.setAlternatingRowColors(True)
            tableview.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)





            memoryDump.tableWidget.resizeColumnsToContents()




            simulatorFrame = QFrame()
            simulatorFrame.layout = QVBoxLayout()
            simulatorFrame.layout.addWidget(Title)
            simulatorFrame.layout.addWidget(self.refreshButton,0, Qt.AlignRight)
            simulatorFrame.layout.addWidget(memoryDump.tableWidget)
            simulatorFrame.setFrameShadow(simulatorFrame.Raised)
            simulatorFrame.setLayout(simulatorFrame.layout)



            memoryDump.memoryDumpFrame.setFrameShape(QFrame.StyledPanel)
            memoryDump.memoryDumpFrame.layout = QHBoxLayout()
            memoryDump.memoryDumpFrame.layout.addWidget(simulatorFrame)
            memoryDump.memoryDumpFrame.setLayout(memoryDump.memoryDumpFrame.layout)



    @staticmethod
    def getMemoryDump():
        return memoryDump.memoryDumpFrame


    def reloadMemoryDump(self):
        print("refreshing to get EEPROM content")

    @staticmethod
    def updateTable():
        i = 0
        j = 0
        memoryDump.tableWidget.setRowCount(len(memoryDump.List) + 1)

        while (i < len(memoryDump.List)):
            j = 0
            memoryDump.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(memoryDump.List[i].address)))
            j = j + 1
            memoryDump.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(memoryDump.List[i].hexNumber)))
            j = j + 1
            memoryDump.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(memoryDump.List[i].value)))
            i = i + 1

            memoryDump.tableWidget.repaint()

    @staticmethod
    def clearList():
        memoryDump.List = []

    @staticmethod
    def UpdateEEPROM(address, hexNumber, value):
        hexNumber= bin(hexNumber)
        rowObj = row( address,hexNumber, value)
        memoryDump.List.append(rowObj)
        memoryDump.updateTable()

class row():
    name = None
    address = None
    value = None

    def __init__(self,address,hexNumber,value):
        self.address= address
        self.hexNumber = hexNumber
        self.value = value








