# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import QSplitter, QApplication, QHBoxLayout, QVBoxLayout

import Components.ATMega_PIN_Diagram
import Components.Globalmap
import Components.List_of_Registers
import Components.Register_Values
import Components.stackedWidget
import Components.EEPROM
from simulavr.adaptor import SimulavrAdaptor
from helper import UIHelper
from multiprocessing import Process, Manager


class Landing(QtWidgets.QWidget):

    def __init__(self):
        super(Landing, self).__init__()
        self.Register_Values = None
        self.List_of_Registers = None
        self.PIN_Diagram = None
        self.stackWidget = None
        self.initUI()

    # initializing UI here and setting properties
    def initUI(self):
        self.title = "ATMega Simulator"
        self.top = 100
        self.left = 600
        self.width = 1100
        self.height = 800
        self.setWindowTitle(self.title)
        self.setStyleSheet("background-color: white")
        self.window()
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    # setting window components for the main page
    def window(self):

        self.Register_Values = Components.Register_Values.Register_Values().getInstance()  # Object of Class Register Values
        self.List_of_Registers = Components.List_of_Registers.List_of_Registers().getInstance()  # Object of Class List of Registers

        self.PIN_Diagram = Components.ATMega_PIN_Diagram.PIN_Diagram()  # Object of Class PIN Diagram

        self.stackWidget = Components.stackedWidget.stackWidget().getInstance()

        self.splitter = QSplitter(Qt.Vertical)

        self.splitter.addWidget(self.List_of_Registers)
        self.splitter.addWidget(self.Register_Values)
        self.splitter.setSizes([300, 150])

        self.horizontalLayout = QHBoxLayout()

        self.rightFrame = self.PIN_Diagram.getPIN_Digram()

        self.stackWidget.addWidget(self.rightFrame)

        self.horizontalSplitter = QSplitter(Qt.Horizontal)
        self.horizontalLayout.addWidget(self.splitter)
        self.horizontalSplitter.addWidget(self.stackWidget)
        self.horizontalSplitter.setSizes([80, 320])
        self.horizontalSplitter.adjustSize()

        self.titleFont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
        self.Title = QtWidgets.QLabel(self)
        self.Title.setText("ATMega328p Simulator")
        self.Title.setFont(self.titleFont)
        self.Title.setAlignment(Qt.AlignCenter)

        self.backButton = QtWidgets.QPushButton("Back")
        self.backButton.clicked.connect(lambda: self.backClicked())

        self.horizontalLayout.addWidget(self.horizontalSplitter)

        self.StatusFont = QtGui.QFont("Helvetica", 10, QtGui.QFont.Bold)
        self.Status = QtWidgets.QLabel(self)
        self.Status.setText(self.getConnectionStatus())
        self.Status.setFont(self.StatusFont)
        self.Status.setStyleSheet('color : green')
        self.Status.setAlignment(Qt.AlignCenter)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.addWidget(self.Title)
        self.verticalLayout.addWidget(self.Status)
        self.verticalLayout.addWidget(self.backButton, 0, Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.setLayout(self.verticalLayout)

    def getConnectionStatus(self):  # Function returns status (Connected / Disconnected)
        return "Connected to Simulavr"

    # functionality for back button
    def backClicked(self):
        UIHelper.UIHelper().refreshItems()
        topWidget = Components.stackedWidget.stackWidget.top
        if topWidget != 0:
            widgetToRemove = Components.stackedWidget.stackWidget.StackWidget.widget(topWidget)
            Components.stackedWidget.stackWidget.decrementTopCount()
            Components.stackedWidget.stackWidget.removeWidget(widgetToRemove)

    # function to update UI for ports and pins
    def updateUI(self, sharedMap, sharedMemoryMap):
        while True:

            if sharedMap['refresh_ui_flag']:
                sharedMap['refresh_ui_flag'] = False
                for key, value in sharedMap.items():
                    port = key.split('.')[0]
                    if key in ['PORTB.PORT', 'PORTC.PORT', 'PORTD.PORT']:
                        UIHelper.UIHelper().setPortValues(port, value)
                    if key in ['PORTB.DDR', 'PORTC.DDR', 'PORTD.DDR']:
                        UIHelper.UIHelper().setDdrValues(port, value)
                    if key in ['PORTB.PIN', 'PORTC.PIN', 'PORTD.PIN']:
                        UIHelper.UIHelper().setPinValues(port, value, self.PIN_Diagram)

                if Components.Globalmap.Map.port_clicked != None:
                    self.PIN_Diagram.refreshPortValues(Components.Globalmap.Map.port_clicked)

                if Components.Globalmap.Map.register_clicked != None:
                    if Components.Globalmap.Map.register_clicked_type == 'r':
                        self.PIN_Diagram.refreshLeftPanelRegisterValues(Components.Globalmap.Map.register_clicked)
                    elif Components.Globalmap.Map.register_clicked_type == 'p':
                        self.PIN_Diagram.refreshLeftPanelPortValues(Components.Globalmap.Map.register_clicked)

                if Components.Globalmap.Map.refresh_flag:
                    Components.Globalmap.Map.refresh_flag = False
                    sharedMap['eeprom_address'] = Components.Globalmap.Map.eeprom_address
                    sharedMap['eeprom_update'] = True

                if sharedMap['eeprom_is_updated']:
                    sharedMap['eeprom_is_updated'] = False
                    Components.EEPROM.memoryDump.UpdateEEPROM(sharedMemoryMap)


class UiThread(QThread):

    def __init__(self, ui, sharedMap, sharedMemoryMap):
        QThread.__init__(self)
        self.ui = ui
        self.sharedMap = sharedMap
        self.sharedMemoryMap = sharedMemoryMap

    def run(self):
        self.ui.updateUI(self.sharedMap, self.sharedMemoryMap)


def run(sharedMap, sharedMemoryMap):
    app = QApplication(sys.argv)
    obj = Landing()
    uiThread = UiThread(obj, sharedMap, sharedMemoryMap)
    uiThread.start()
    app.exec_()

            
if __name__ == '__main__':

    manager = Manager()
    sharedMap = manager.dict()
    sharedMemoryMap = manager.dict()

    p = Process(target=run, args=[sharedMap, sharedMemoryMap])
    p.start()
    sim = SimulavrAdaptor.SimulavrAdapter()
    sim.runProgram(sharedMap, sharedMemoryMap)
