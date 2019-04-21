'''
Description: This class is used to create a thread for simulavr for running it seperately from main thread.
			 The run function of this thread invokes a method call which is reponsible for running of the program.
'''
from PyQt5.QtCore import QThread

class simulavrThread(QThread):
	def __init__(self, ui, sim):
		QThread.__init__(self)
		self.sim = sim
		self.ui = ui

	def run(self):
		self.sim.runProgram(self.ui, self)
