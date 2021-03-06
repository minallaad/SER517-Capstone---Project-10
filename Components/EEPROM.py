'''
This class is used to fetch and display the EEPROM values.
'''

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import  QHBoxLayout, QLabel, QFrame, QVBoxLayout, QTableWidget , QTableWidgetItem,QLineEdit,QPushButton
from PyQt5.QtCore import Qt, QRect

import Components.stackedWidget
from Components import pinLevelDiagram
import Components.Globalmap


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
            self.refreshButton.clicked.connect(lambda: self.submitClicked)

            self.memoryAddressLabel = QLabel(self)
            self.memoryAddressLabel.setText('Memory Address:')
            self.line = QLineEdit(self)

            self.line.move(80, 20)
            self.line.resize(100, 32)
            self.memoryAddressLabel.move(20, 20)

            submitbutton = QPushButton('Submit', self)
            submitbutton.clicked.connect(self.submitClicked)
            submitbutton.resize(100, 32)
            submitbutton.move(80, 60)

            self.inputFrame = QFrame()
            self.inputFrame.layout = QHBoxLayout()
            self.inputFrame.layout.addWidget(self.memoryAddressLabel)
            self.inputFrame.layout.addWidget(self.line)
            self.inputFrame.layout.addWidget(submitbutton)
            self.inputFrame.layout.addWidget(self.refreshButton,0, Qt.AlignRight)
            self.inputFrame.setLayout(self.inputFrame.layout)

            headerfont = QtGui.QFont()
            headerfont.setFamily("Arial Black")
            headerfont.setPointSize(11)

            memoryDump.tableWidget = QTableWidget()
            memoryDump.tableWidget.setRowCount(2)
            memoryDump.tableWidget.setColumnCount(3)
            memoryDump.map = {}

            memoryDump.tableWidget.setItem(0, 0, QTableWidgetItem("Address   "))
            memoryDump.tableWidget.setItem(0, 1, QTableWidgetItem("Hex Values"))
            memoryDump.tableWidget.setItem(0, 2, QTableWidgetItem("Text Values"))

            tableview = QtWidgets.QTableView()
            tableview.setAlternatingRowColors(True)
            tableview.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

            memoryDump.tableWidget.resizeColumnsToContents()

            simulatorFrame = QFrame()
            simulatorFrame.layout = QVBoxLayout()
            simulatorFrame.layout.addWidget(Title)
            simulatorFrame.layout.addWidget(self.inputFrame)
            simulatorFrame.layout.addWidget(memoryDump.tableWidget)
            simulatorFrame.setFrameShadow(simulatorFrame.Raised)
            simulatorFrame.setLayout(simulatorFrame.layout)

            memoryDump.memoryDumpFrame.setFrameShape(QFrame.StyledPanel)
            memoryDump.memoryDumpFrame.layout = QHBoxLayout()
            memoryDump.memoryDumpFrame.layout.addWidget(simulatorFrame)
            memoryDump.memoryDumpFrame.setLayout(memoryDump.memoryDumpFrame.layout)

    '''
    Description: Function to fetch the memory dump map
    '''
    @staticmethod
    def getMemoryDump():
        return memoryDump.memoryDumpFrame

    '''
    Description: Function to fetch clear and reload the memory dump
    '''
    def reloadMemoryDump(self):
        self.clearMap()
        self.updateTable()

    def submitClicked(self):
        Components.Globalmap.Map.eeprom_address = int(self.line.text(), 16)
        Components.Globalmap.Map.refresh_flag = True

    '''
    Description: function to update the EEPROM values in the EERPOM tables
    @param sharedMemoryMap: Map which contains the updated values of EEPROM.
    '''
    @staticmethod
    def updateTable(sharedMemoryMap):
        i = 0
        memoryDump.map = sharedMemoryMap
        memoryDump.tableWidget.setRowCount(len(memoryDump.map) + 1)
        for key, Value in sharedMemoryMap.items():
            j = 0
            memoryDump.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(hex(key))))
            j = j + 1
            memoryDump.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(' '.join([hex(int(x)) for x in Value]))))
            j = j + 1
            s = ''
            for val in Value:
                s += chr(int(val)) if int(val) < 176 and int(val) > 32 and int(val) != 127 else ' . '
            memoryDump.tableWidget.setItem(i + 1, j, QTableWidgetItem(s))
            i = i + 1
        memoryDump.tableWidget.resizeColumnsToContents()

    @staticmethod
    def clearMap():
        memoryDump.map = {}

    @staticmethod
    def UpdateEEPROM(sharedMemoryMap):
        memoryDump.updateTable(sharedMemoryMap)

class row():
    name = None
    address = None
    value = None

    def __init__(self,address,hexNumber,value):
        self.address= address
        self.hexNumber = hexNumber
        self.value = value
