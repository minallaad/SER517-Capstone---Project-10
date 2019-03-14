# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QLabel, QSplitter,QApplication, QHBoxLayout, QStackedWidget,QFrame,QVBoxLayout,QScrollArea,QListWidget,  QMessageBox,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QPainter, QPen , QPixmap
from PyQt5.QtCore import Qt

import Components.stackedWidget
import Components.Register_Values
import Components.List_of_Registers
import Components.ATMega_PIN_Diagram


class Landing(QtWidgets.QWidget): 


	def __init__(self):
	    super(Landing, self).__init__()
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
		self.setGeometry(self.top ,self.left,self.width ,self.height)

		self.show()


	def window(self):

		Register_Values = Components.Register_Values.Register_Values().getInstance()  # Object of Class Register Values
		List_of_Registers = Components.List_of_Registers.List_of_Registers().getInstance() # Object of Class List of Registers

		PIN_Diagram = Components.ATMega_PIN_Diagram.PIN_Diagram() # Object of Class PIN Diagram

		stackWidget = Components.stackedWidget.stackWidget().getInstance();



		splitter = QSplitter(Qt.Vertical);

		splitter.addWidget(List_of_Registers)
		splitter.addWidget(Register_Values)
		splitter.setSizes([300,150])

		horizontalLayout = QHBoxLayout()

		rightFrame = PIN_Diagram.getPIN_Digram();

		stackWidget.addWidget(rightFrame);
		print(stackWidget.currentWidget())

		horizontalSplitter = QSplitter(Qt.Horizontal)
		horizontalLayout.addWidget(splitter)
		horizontalSplitter.addWidget(stackWidget)
		horizontalSplitter.setSizes([80,320])
		horizontalSplitter.adjustSize()

		titleFont =  QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
		Title = QtWidgets.QLabel(self)
		Title.setText("ATMega328p Simulator")
		Title.setFont(titleFont)
		Title.setAlignment(Qt.AlignCenter)
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
		verticalLayout.addLayout(horizontalLayout);

		self.setLayout(verticalLayout)

	def getConnectionStatus(self):  # Function returns status (Connected / Disconnected)
		return "Connected to Simulavr"


		
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Landing()
    sys.exit(app.exec_())

