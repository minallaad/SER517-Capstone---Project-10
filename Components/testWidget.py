# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(170, 128)
        self.testLabel = QtWidgets.QLabel(Form)
        self.testLabel.setGeometry(QtCore.QRect(40, 50, 81, 17))
        self.testLabel.setObjectName("testLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.testLabel.setText(_translate("Form", "Test Label"))

