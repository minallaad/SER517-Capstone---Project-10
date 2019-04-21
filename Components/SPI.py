# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SPI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Resources import spi_rc

class Ui_SPIFrame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(771, 640)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(240, 30, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("Title")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(90, 90, 671, 501))
        self.label_2.setObjectName("Image")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Serial Peripheral Interface"))
        self.label_2.setText(_translate("Frame", "<html><head/><body><p><img src=\":/SPI/Images/SPI.png\"/></p></body></html>"))


