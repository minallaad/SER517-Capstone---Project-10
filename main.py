# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QLabel, QSplitter,QApplication, QHBoxLayout, QGroupBox,QFrame,QVBoxLayout,QScrollArea,QListWidget,  QMessageBox,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QPainter, QPen , QPixmap
from PyQt5.QtCore import Qt


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

		splitter = QSplitter(Qt.Vertical);

		pins = ['CORE.GPIOR2', 'PORTB.PORT', 'PORTB.PIN', 'PORTB.DDR', 'PORTB.B0-Out', 'IRQ.VECTOR0', 'EEPROM.EEDR',
				'TMRIRQ0.TIMSKO', 'TIMER0.Counter', 'TIMER0.TCNT', 'SPI.SPDR', 'UART0.UDR' , 'CORE.GPIOR2', 'PORTB.PORT', 'PORTB.PIN', 'PORTB.DDR', 'PORTB.B0-Out', 'IRQ.VECTOR0', 'EEPROM.EEDR',
				'TMRIRQ0.TIMSKO', 'TIMER0.Counter','TIMER0.TCNT', 'SPI.SPDR', 'UART0.UDR' ,'CORE.GPIOR2', 'PORTB.PORT', 'PORTB.PIN', 'PORTB.DDR', 'PORTB.B0-Out', 'IRQ.VECTOR0', 'EEPROM.EEDR',
				'TMRIRQ0.TIMSKO', 'TIMER0.Counter',
				'TIMER0.TCNT', 'SPI.SPDR', 'UART0.UDR' ]   # Add the correct register values from tracelist and update this comment

		listWidget = myListWidget(self)
		listWidget.itemClicked.connect(listWidget.Clicked)
		listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		listWidget.move(90, 195)

		for i in pins:
			listWidget.addItem(i)

		self.tableWidget = QTableWidget()
		self.tableWidget.setRowCount(1)
		self.tableWidget.setColumnCount(3)


		self.tableWidget.setItem(0, 0, QTableWidgetItem("Name"))
		self.tableWidget.setItem(0, 1, QTableWidgetItem("Address"))
		self.tableWidget.setItem(0, 2, QTableWidgetItem("Value"))
		self.tableWidget.resize(4,4)

		splitter.addWidget(listWidget)
		splitter.addWidget(self.tableWidget)
		splitter.setSizes([300,150])

		horizontalLayout = QHBoxLayout()


		imgLabel = QLabel(self)
		pixmap = QPixmap('Resources/Images/atmega328p.png')
		pixmap1 = pixmap.scaled(250, 400)
		imgLabel.setPixmap(pixmap1)
		imgLabel.setAlignment(Qt.AlignCenter)
		imgLabel.setFrameStyle(QFrame.Box)



		horizontalSplitter = QSplitter(Qt.Horizontal)
		horizontalLayout.addWidget(splitter)
		horizontalSplitter.addWidget(imgLabel)
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



		# pins = ['CORE.GPIOR2', 'PORTB.PORT', 'PORTB.PIN', 'PORTB.DDR', 'PORTB.B0-Out', 'IRQ.VECTOR0','EEPROM.EEDR', 'TMRIRQ0.TIMSKO','TIMER0.Counter',
		# 'TIMER0.TCNT','SPI.SPDR','UART0.UDR']
        #
		# pin_dict = {}
		# vert_space = 195
        #
		# listWidget = myListWidget(self)
        #
		# listWidget.resize(190,150)
		# listWidget.itemClicked.connect(listWidget.Clicked)
		# listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		# listWidget.move(90,195)
  		#
        #
		# for i in pins:
        #
		# 	#pin_dict[i] = QtWidgets.QLabel(self)
        #
		# 	#pin_dict[i].setText(i)
		# 	#pin_dict[i].move(90, vert_space)
		# 	#pin_dict[i].setFont(label_2_4_font)
		# 	listWidget.addItem(i)
		#
  		

			#vert_space += 30
        #
		# pinsl = ['PD0', 'PD1', 'PD2', 'PD3', 'PD4', 'PD5' , 'PD6', 'PB3', 'PB4', 'PB5', 'PB6']
		# pinsr = ['PC6', 'PC5', 'PC4', 'PC3', 'PC2', 'PC1' , 'PC0', 'PB1', 'PB2', 'PF2', 'PF1']
        #
		#
		# pinl_dict = {}
		# vert_space = 325
		#
		#
        #
		# for i in pinsl:
        #
		# 	pinl_dict[i] = QtWidgets.QLabel(self)
        #
		# 	pinl_dict[i].setText(i)
		# 	pinl_dict[i].move(515, vert_space)
		# 	pinl_dict[i].setFont(label_2_4_font)
		# 	pinl_dict[i].setStyleSheet('color : grey')
		#
		# 	vert_space += 30
        #
		# pinr_dict = {}
		# vert_space = 325
        #
		# for i in pinsr:
        #
		# 	pinr_dict[i] = QtWidgets.QLabel(self)
        #
		# 	pinr_dict[i].setText(i)
		# 	pinr_dict[i].move(760, vert_space)
		# 	pinr_dict[i].setFont(label_2_4_font)
		# 	pinr_dict[i].setStyleSheet('color : grey')
		#
		# 	vert_space += 30
        #
		# pinl_dict['PD0'].setStyleSheet('color : red')
		# pinl_dict['PD1'].setStyleSheet('color : red')
		# pinl_dict['PD2'].setStyleSheet('color : red')
        #
		# pinr_dict['PC6'].setStyleSheet('color : green')
		# pinr_dict['PC5'].setStyleSheet('color : green')
		# pinr_dict['PC4'].setStyleSheet('color : green')
        #
		#
		
class myListWidget(QListWidget):   # On Click Register name calls this function

	def Clicked(self,item):
		QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())
		


		
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Landing()
    sys.exit(app.exec_())

