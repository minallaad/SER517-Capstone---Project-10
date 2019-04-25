from PyQt5.QtCore import QThread


class UiThread(QThread):

    def __init__(self, ui, sharedMap, sharedMemoryMap):
        QThread.__init__(self)
        self.ui = ui
        self.sharedMap = sharedMap
        self.sharedMemoryMap = sharedMemoryMap

    def run(self):
        self.ui.updateUI(self.sharedMap, self.sharedMemoryMap)