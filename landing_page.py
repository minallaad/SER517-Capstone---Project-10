# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QGroupBox,QFrame,QVBoxLayout,QScrollArea,QListWidget,  QMessageBox
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class Landing(QtWidgets.QWidget): 


	def __init__(self):

	    super(Landing, self).__init__()
	    
	    self.initUI()
	    
	    
	def initUI(self):

		self.setWindowTitle("ATMega Simulator")
		self.setGeometry(100, 100, 300 ,200)
		self.window()
		self.show()


 		
	def paintEvent(self, event): 
		qp = QtGui.QPainter() 
		qp.begin(self) 

		qp.setPen(QtGui.QPen(Qt.blue, 2, join = Qt.MiterJoin)) 
		qp.drawRect(550,260,200,480) 
		qp.drawRect(00,90,1800,40) 
		qp.drawRect(90,590,300,300)
		qp.drawLine(190, 590, 190, 890)
		qp.drawLine(300, 590, 300, 890)
		qp.drawLine(90, 630, 390, 630)

		qp.end() 
 		


	def window(self):

		
		
		label1 =  QtWidgets.QLabel(self)
		label2 =  QtWidgets.QLabel(self)
		label3 =  QtWidgets.QLabel(self)
		label4 =  QtWidgets.QLabel(self)
		label5 =  QtWidgets.QLabel(self)
		label6 =  QtWidgets.QLabel(self)
		label7 =  QtWidgets.QLabel(self)

		

		


		label1.setText("ATMega328p Simulator")
		label2.setText("Connected to Simulavr  ")
		label3.setText("In Debugging Mode    ")
		label4.setText("Disconnected  ")
		label5.setText("Program Loading")
		label6.setText("ATMega328p")
		label7.setText("ATMega328p")

		label1.move(540 , 45)

		label2.move(330 , 105)
		label3.move(530 , 105)
		label4.move(730 , 105)
		label5.move(930 , 105)

		label6.move(606 , 195)

		label7.move(606 , 515)


		

		

		label1font = QtGui.QFont("Times", 25, QtGui.QFont.Bold)
		label_2_4_font = QtGui.QFont("Times", 15, QtGui.QFont.Bold)
		label6font = QtGui.QFont("Times", 20, QtGui.QFont.Bold)


		label_name =  QtWidgets.QLabel(self)
		label_address =  QtWidgets.QLabel(self)
		label_value =  QtWidgets.QLabel(self)
		label_name.setText("Name")
		label_address.setText("Address")
		label_value.setText("Value")
		label_name.setFont(label_2_4_font)
		label_address.setFont(label_2_4_font)
		label_value.setFont(label_2_4_font)

		label_name.move(100 , 605)
		label_address.move(220 , 605)
		label_value.move(340 , 605)


		label_name.setStyleSheet('color : green')
		label_address.setStyleSheet('color : green')
		label_value.setStyleSheet('color : green')


		label1.setFont(label1font)
		label2.setFont(label_2_4_font)
		label3.setFont(label_2_4_font)
		label4.setFont(label_2_4_font)
		label5.setFont(label_2_4_font)
		label6.setFont(label6font)
		label7.setFont(label6font)

		label6.setStyleSheet('color : brown')
		label7.setStyleSheet('color : brown')

		
		pins = ['CORE.GPIOR2', 'PORTB.PORT', 'PORTB.PIN', 'PORTB.DDR', 'PORTB.B0-Out', 'IRQ.VECTOR0','EEPROM.EEDR', 'TMRIRQ0.TIMSKO','TIMER0.Counter',
		'TIMER0.TCNT','SPI.SPDR','UART0.UDR']

		pin_dict = {}
		vert_space = 195

		listWidget = myListWidget(self)
	
		listWidget.resize(190,150)
		listWidget.itemClicked.connect(listWidget.Clicked)
		listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		listWidget.move(90,195)
  		 

		for i in pins:

			#pin_dict[i] = QtWidgets.QLabel(self)

			#pin_dict[i].setText(i)
			#pin_dict[i].move(90, vert_space)
			#pin_dict[i].setFont(label_2_4_font)
			listWidget.addItem(i)
			
  		

			#vert_space += 30

		pinsl = ['PD0', 'PD1', 'PD2', 'PD3', 'PD4', 'PD5' , 'PD6', 'PB3', 'PB4', 'PB5', 'PB6']
		pinsr = ['PC6', 'PC5', 'PC4', 'PC3', 'PC2', 'PC1' , 'PC0', 'PB1', 'PB2', 'PF2', 'PF1']

		
		pinl_dict = {}
		vert_space = 325
		
		

		for i in pinsl:

			pinl_dict[i] = QtWidgets.QLabel(self)

			pinl_dict[i].setText(i)
			pinl_dict[i].move(515, vert_space)
			pinl_dict[i].setFont(label_2_4_font)
			pinl_dict[i].setStyleSheet('color : grey')
			
			vert_space += 30

		pinr_dict = {}
		vert_space = 325

		for i in pinsr:

			pinr_dict[i] = QtWidgets.QLabel(self)

			pinr_dict[i].setText(i)
			pinr_dict[i].move(760, vert_space)
			pinr_dict[i].setFont(label_2_4_font)
			pinr_dict[i].setStyleSheet('color : grey')
			
			vert_space += 30

		pinl_dict['PD0'].setStyleSheet('color : red')
		pinl_dict['PD1'].setStyleSheet('color : red')
		pinl_dict['PD2'].setStyleSheet('color : red')

		pinr_dict['PC6'].setStyleSheet('color : green')
		pinr_dict['PC5'].setStyleSheet('color : green')
		pinr_dict['PC4'].setStyleSheet('color : green')

		
		
class myListWidget(QListWidget):

	def Clicked(self,item):
		QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())
		

   
   
		

	 
		
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Landing()
    sys.exit(app.exec_())

