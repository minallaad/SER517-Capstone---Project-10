import sys
from PyQt5.QtCore import Qt

from PyQt5 import QtGui , QtWidgets
from PyQt5.QtWidgets import QApplication ,QFrame, QHBoxLayout, QMainWindow, QAction, QDialog, QGridLayout, QSpacerItem, QVBoxLayout, QLabel, QLineEdit, QTextEdit , QSplitter, QWidget


class Window(QWidget):

        def __init__(self):    # Constructor for Class Window
            super().__init__()

            self.title = "ATMega Simulator"
            self.top = 100
            self.left = 100
            self.width = 1000
            self.height = 800

            self.InitWindow()

        def InitWindow(self):     # Initalize Window
            self.setWindowTitle(self.title)
            self.setStyleSheet("background-color: white")
           # self.getToolBar()
            #self.getConnectionStatus()

            hbox = QHBoxLayout(self)


            left = QFrame()
            left.setFrameShape(QFrame.StyledPanel)
            left.setStyleSheet("background-color: white")



            bottomLeft = QFrame()
            bottomLeft.setFrameShape(QFrame.StyledPanel)

            splitter =  QSplitter(Qt.Vertical)
            splitter.addWidget(left)
            splitter.addWidget(bottomLeft)
            splitter.setSizes([300,150])

            right = QFrame()
            right.setFrameShape(QFrame.StyledPanel)

            splitter1 = QSplitter(Qt.Horizontal)
            splitter1.addWidget(splitter)
            splitter1.addWidget(right)
            splitter1.setSizes([100,300])

            hbox.addWidget(splitter1)

            self.setLayout(hbox)


            self.setGeometry(self.top, self.left, self.width, self.height)

            self.show()





        def getToolBar(self):

             backAction = QAction(QtGui.QIcon('Resources/Icons/back-to-back-png-5.png'),'&Back',self)
             backAction.setEnabled(False)
             backAction.setShortcut('Ctrl+S')

             self.toolbar = self.addToolBar('Save')
             self.toolbar.addAction(backAction)


        def getConnectionStatus(self):   # Function returns status (Connected / Disconnected
            self.statusBar().showMessage('Disconnected.')



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())


main()  #### Start of Application ###

