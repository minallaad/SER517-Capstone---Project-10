# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import QWidget,QLabel, QSplitter,QApplication, QHBoxLayout, QStackedWidget,QFrame,QVBoxLayout,QScrollArea,QListWidget,  QMessageBox,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QPainter, QPen , QPixmap
from PyQt5.QtCore import Qt
from pysimulavrExample.examples import SimulavrAdaptor
from threading import Thread


import Components.stackedWidget
import Components.Register_Values
import Components.List_of_Registers
import Components.ATMega_PIN_Diagram


class Landing(QtWidgets.QWidget):


	def __init__(self):
		super(Landing, self).__init__()
		self.portBValue = -1
		self.ddrbValue = -1
		self.Register_Values = None
		self.List_of_Registers = None

		self.PIN_Diagram = None

		self.stackWidget = None
		self.initUI()


	def initUI(self):
		self.title = "ATMega Simulator"
		self.top = 100
		self.left = 100
		self.width = 1000
		self.height = 800
		self.setWindowTitle(self.title)
		self.setStyleSheet("background-color: white")
		self.window()
		self.setGeometry(self.top, self.left, self.width, self.height)

		self.show()

	def setLedColor(self, portbValue, ddrbValue):
		# if the window is not yet created, just return
		if self.window == None: return

		# if the hardware state has not changed, just return
		if (self.portBValue == portbValue) and (self.ddrbValue == ddrbValue): return

		# update the LED state based on the port direction and value
		if (ddrbValue != 0):
			# port set to output - set the color based on the value of portb
			if (portbValue != 0):
				# led is driven on
				self.setStyleSheet("background-color: white")
			else:
				# led is driven off
				self.setStyleSheet("background-color: black")
		else:
			# port is set to input - set the color based on the pullup value
			if (portbValue != 0):
				# led will be on due to pullup
				self.setStyleSheet("background-color: white")
			else:
				# led state is not driven
				self.setStyleSheet("background-color: black")
		self.portBValue = portbValue
		self.ddrbValue = ddrbValue


	def window(self):

		self.Register_Values = Components.Register_Values.Register_Values().getInstance()  # Object of Class Register Values
		self.List_of_Registers = Components.List_of_Registers.List_of_Registers().getInstance() # Object of Class List of Registers

		self.PIN_Diagram = Components.ATMega_PIN_Diagram.PIN_Diagram() # Object of Class PIN Diagram

		self.stackWidget = Components.stackedWidget.stackWidget().getInstance()



		splitter = QSplitter(Qt.Vertical)

		splitter.addWidget(self.List_of_Registers)
		splitter.addWidget(self.Register_Values)
		splitter.setSizes([300,150])

		horizontalLayout = QHBoxLayout()

		rightFrame = self.PIN_Diagram.getPIN_Digram()

		self.stackWidget.addWidget(rightFrame)
		print(self.stackWidget.currentWidget())

		horizontalSplitter = QSplitter(Qt.Horizontal)
		horizontalLayout.addWidget(splitter)
		horizontalSplitter.addWidget(self.stackWidget)
		horizontalSplitter.setSizes([80,320])
		horizontalSplitter.adjustSize()

		titleFont =  QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
		Title = QtWidgets.QLabel(self)
		Title.setText("ATMega328p Simulator")
		Title.setFont(titleFont)
		Title.setAlignment(Qt.AlignCenter)

		backButton = QtWidgets.QPushButton("Back")
		backButton.clicked.connect(lambda : self.backClicked())


		horizontalLayout.addWidget(horizontalSplitter)


		StatusFont =  QtGui.QFont("Helvetica", 10, QtGui.QFont.Bold)
		Status = QtWidgets.QLabel(self)
		Status.setText(self.getConnectionStatus())
		Status.setFont(StatusFont)
		Status.setStyleSheet('color : green')
		Status.setAlignment(Qt.AlignCenter)

		verticalLayout = QVBoxLayout()
		verticalLayout.addWidget(Title)
		verticalLayout.addWidget(Status)
		verticalLayout.addWidget(backButton, 0, Qt.AlignRight)
		verticalLayout.addLayout(horizontalLayout)

		self.setLayout(verticalLayout)

	def getConnectionStatus(self):  # Function returns status (Connected / Disconnected)
		return "Connected to Simulavr"

	def backClicked(self):
		topWidget = Components.stackedWidget.stackWidget.top
		if topWidget != 0 :
			print("TOP")
			widgetToRemove = Components.stackedWidget.stackWidget.StackWidget.widget(topWidget)
			Components.stackedWidget.stackWidget.decrementTopCount()
			Components.stackedWidget.stackWidget.removeWidget(widgetToRemove)

	def updateUI(self, valueMap):
		self.valueMap = valueMap

		for key, value in valueMap.items():

			if key == 'PORTB':
				self.PIN_Diagram.setPinStatus("PD0", value)


class threadExample(QThread):
	def __init__(self, ui, sim):
		QThread.__init__(self)
		self.sim = sim
		self.ui = ui
		self.start()

	def run(self):
		self.sim.runProgram(self.ui)


if __name__ == '__main__':

	app = QApplication(sys.argv)
	obj = Landing()
	sim = SimulavrAdaptor.SimulavrAdapter()
	thread = threadExample(obj, sim)
	app.exec_()





