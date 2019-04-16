from PyQt5.QtCore import QThread

class simulavrThread(QThread):
	def __init__(self, ui, sim):
		QThread.__init__(self)
		self.sim = sim
		self.ui = ui
		self.start()

	def run(self):
		self.sim.runProgram(self.ui, self)
