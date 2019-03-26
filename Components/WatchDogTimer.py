# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Watchdog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from Resources import imageResource_rc

class Ui_watchDogFrame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(820, 631)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(290, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(140, 100, 511, 431))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "WatchDog Timer"))
        self.label_2.setText(_translate("Frame", "<html><head/><body><p><img src=\":/image/Images/WatchDogTimer.png\"/></p></body></html>"))

