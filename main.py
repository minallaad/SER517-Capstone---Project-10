import sys

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication

from landing import Landing
from simulavr.adaptor import SimulavrAdaptor

class Main():
    obj = None

    def runCode(self, obj):
        sim = SimulavrAdaptor.SimulavrAdapter()
        sim.runProgram(obj)

class UIThread(QThread):
    def __init__(self, app):
        QThread.__init__(self)
        self.obj = Landing()
        self.app = app

    #def run(self):
        #self.app.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    thread = UIThread(app)
    thread.start()
    Main().runCode(thread.obj)
    # thread = SimulavrThread.simulavrThread(obj, sim)
    # thread.start()
    app.exec_()
