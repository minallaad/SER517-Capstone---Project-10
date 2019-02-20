import sys
from PyQt5 import QtWidgets, QtGui

def window():

	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()

	w.setWindowTitle("ATMega Simulator")

	label1 =  QtWidgets.QLabel(w)
	label2 =  QtWidgets.QLabel(w)
	label3 =  QtWidgets.QLabel(w)
	label4 =  QtWidgets.QLabel(w)
	label5 =  QtWidgets.QLabel(w)
	label6 =  QtWidgets.QLabel(w)

	label1.setText("ATMega328p Simulator")
	label2.setText("ATMega328p")
	label3.setText("Connected to Simulavr  ")
	label4.setText("In Debugging Mode    ")
	label5.setText("Disconnected  ")
	label6.setText("Program Loading")

	
	

	w.show()

	#to let us know if the process ended successfully or not
	sys.exit(app.exec_())

window()

