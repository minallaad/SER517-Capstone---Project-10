import sys
import os

from PyQt5.QtWidgets import QApplication

from Landing import Landing
from simulavr.adaptor import SimulavrAdaptor
from thread.UiThread import UiThread
from multiprocessing import Process, Manager


def runGui(sharedMap, sharedMemoryMap):
    app = QApplication(sys.argv)
    obj = Landing()
    uiThread = UiThread(obj, sharedMap, sharedMemoryMap)
    uiThread.start()
    app.exec_()
    
    del obj
    del app
    os.system("kill -9 `ps -ef | grep main.py | grep -v grep | awk '{print $2}'`")
            
if __name__ == '__main__':

    manager = Manager()
    sharedMap = manager.dict()
    sharedMemoryMap = manager.dict()

    p = Process(target=runGui, args=[sharedMap, sharedMemoryMap])
    p.start()

    try:
        sim = SimulavrAdaptor.SimulavrAdapter()
        sim.runProgram(sharedMap, sharedMemoryMap)
    except:
        p.terminate()
