# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainWindowFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainWindowFrame.setGeometry(QtCore.QRect(0, 0, 801, 641))
        self.mainWindowFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.mainWindowFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mainWindowFrame.setLineWidth(0)
        self.mainWindowFrame.setMidLineWidth(0)
        self.mainWindowFrame.setObjectName("mainWindowFrame")
        self.registerListFrame = QtWidgets.QFrame(self.mainWindowFrame)
        self.registerListFrame.setGeometry(QtCore.QRect(0, 40, 221, 371))
        self.registerListFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.registerListFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.registerListFrame.setObjectName("registerListFrame")
        self.registerValuesFrame = QtWidgets.QFrame(self.mainWindowFrame)
        self.registerValuesFrame.setGeometry(QtCore.QRect(0, 410, 221, 231))
        self.registerValuesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.registerValuesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.registerValuesFrame.setObjectName("registerValuesFrame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

