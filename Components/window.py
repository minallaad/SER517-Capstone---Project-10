import sys
from PyQt5 import QtWidgets

def window():

	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()

	w.setWindowTitle("Atmega Simulator")

	w.show()

	#to let us know if the process ended successfully or not
	sys.exit(app.exec_())

window()

