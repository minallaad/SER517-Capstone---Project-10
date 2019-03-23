# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ATMega_Block_Diagram.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QSplitter, QApplication, QHBoxLayout, QGroupBox, QFrame, QVBoxLayout, QStackedLayout

class Ui_microcontrollerBlock():

    rightFrame = None

    def __init__(self):
        super(Ui_microcontrollerBlock, self).__init__()

        if Ui_microcontrollerBlock.rightFrame == None:
            Ui_microcontrollerBlock.rightFrame = QFrame()

            font = QtGui.QFont("Arial", 12, QtGui.QFont.Bold);
            TitleFont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)

            BlockDiagramTitle = QLabel()
            BlockDiagramTitle.setText("ATMega328p Block Diagram")
            BlockDiagramTitle.setStyleSheet('color : Black')
            BlockDiagramTitle.setAlignment(Qt.AlignCenter)
            BlockDiagramTitle.setFont(TitleFont)

            self.watchdogFrame = QFrame()
            self.watchdogFrame.setGeometry(QtCore.QRect(40, 170, 120, 80))
            self.watchdogFrame.setFrameShape(QtWidgets.QFrame.Panel)
            self.watchdogFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.watchdogFrame.setStyleSheet("QWidget { background-color: #14aaff }")
            self.watchdogFrame.setLineWidth(2)
            self.watchdogFrame.setObjectName("watchdogFrame")
            self.watchdogLabel = QtWidgets.QLabel(self.watchdogFrame)
            self.watchdogLabel.setGeometry(QtCore.QRect(16, 20, 91, 41))
            self.watchdogLabel.setScaledContents(False)
            self.watchdogLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.watchdogLabel.setWordWrap(True)
            self.watchdogLabel.setObjectName("watchdogLabel")
            self.watchdogLabel.setText("Watchdog timer")
            self.watchdogLabel.setFont(font);

            self.tc1Frame =QFrame()
            self.tc1Frame.setGeometry(QtCore.QRect(40, 300, 120, 80))
            self.tc1Frame.setFrameShape(QtWidgets.QFrame.Panel)
            self.tc1Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.tc1Frame.setStyleSheet("QWidget { background-color: #14aaff }")
            self.tc1Frame.setLineWidth(2)
            self.tc1Frame.setObjectName("tc1Frame")
            self.tc1Label = QtWidgets.QLabel(self.tc1Frame)
            self.tc1Label.setGeometry(QtCore.QRect(30, 20, 67, 41))
            self.tc1Label.setScaledContents(False)
            self.tc1Label.setAlignment(QtCore.Qt.AlignCenter)
            self.tc1Label.setWordWrap(True)
            self.tc1Label.setObjectName("tc1Label")
            self.tc1Label.setText("TC 1            (8-bit)")
            self.tc1Label.setFont(font);

            self.tc2Frame = QFrame()
            self.tc2Frame.setGeometry(QtCore.QRect(40, 420, 120, 80))
            self.tc2Frame.setFrameShape(QtWidgets.QFrame.Panel)
            self.tc2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.tc2Frame.setStyleSheet("QWidget { background-color: #14aaff }")
            self.tc2Frame.setLineWidth(2)
            self.tc2Frame.setObjectName("tc2Frame")
            self.tc2Label = QtWidgets.QLabel(self.tc2Frame)
            self.tc2Label.setGeometry(QtCore.QRect(30, 20, 67, 41))
            self.tc2Label.setScaledContents(False)
            self.tc2Label.setAlignment(QtCore.Qt.AlignCenter)
            self.tc2Label.setWordWrap(True)
            self.tc2Label.setObjectName("tc2Label")
            self.tc2Label.setText("TC 2            (8-bit)")
            self.tc2Label.setFont(font);


            verticalFrame1 = QFrame()
            verticalFrame1.layout = QVBoxLayout()
            verticalFrame1.layout.setAlignment(Qt.AlignLeft)
            # verticalFrame1.layout.setSpacing(20)
            verticalFrame1.layout.addWidget(self.watchdogFrame)
            # verticalFrame1.layout.setSpacing(20)
            # verticalFrame1.layout.addWidget(self.tc1Frame)
            # verticalFrame1.layout.setSpacing(20)
            # verticalFrame1.layout.addWidget(self.tc2Frame)
            # verticalFrame1.layout.setSpacing(20)

            verticalFrame1.layout.addStretch()
            verticalFrame1.setLayout(verticalFrame1.layout)



            Ui_microcontrollerBlock.rightFrame.setFrameShape(QFrame.StyledPanel)
            Ui_microcontrollerBlock.rightFrame.layout = QVBoxLayout()
            Ui_microcontrollerBlock.rightFrame.layout.addWidget(BlockDiagramTitle)
            Ui_microcontrollerBlock.rightFrame.layout.addWidget(verticalFrame1)
            Ui_microcontrollerBlock.rightFrame.setLayout(Ui_microcontrollerBlock.rightFrame.layout)

            # microcontrollerBlock.setObjectName("microcontrollerBlock")
            # microcontrollerBlock.resize(578, 540)
            #
            #
            # self.flashFrame = QtWidgets.QFrame(microcontrollerBlock)
            # self.flashFrame.setGeometry(QtCore.QRect(210, 110, 120, 80))
            # self.flashFrame.setFrameShape(QtWidgets.QFrame.Panel)
            # self.flashFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            # self.flashFrame.setStyleSheet("QWidget { background-color: #14aaff }")
            # self.flashFrame.setLineWidth(2)
            # self.flashFrame.setObjectName("flashFrame")
            # self.flashLabel = QtWidgets.QLabel(self.flashFrame)
            # self.flashLabel.setGeometry(QtCore.QRect(20, 30, 67, 17))
            # self.flashLabel.setAlignment(QtCore.Qt.AlignCenter)
            # self.flashLabel.setObjectName("flashLabel")
            # self.flashLabel.setText("Flash")
            # self.flashLabel.setFont(font);
            #
            #
            # self.eepromFrame = QtWidgets.QFrame(microcontrollerBlock)
            # self.eepromFrame.setGeometry(QtCore.QRect(210, 230, 120, 80))
            # self.eepromFrame.setFrameShape(QtWidgets.QFrame.Panel)
            # self.eepromFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            # self.eepromFrame.setStyleSheet("QWidget { background-color: #14aaff }")
            # self.eepromFrame.setLineWidth(2)
            # self.eepromFrame.setObjectName("eepromFrame")
            # self.eepromLabel = QtWidgets.QLabel(self.eepromFrame)
            # self.eepromLabel.setGeometry(QtCore.QRect(30, 30, 67, 17))
            # self.eepromLabel.setAlignment(QtCore.Qt.AlignCenter)
            # self.eepromLabel.setObjectName("eepromLabel")
            # self.eepromLabel.setText("EEPROM")
            # self.eepromLabel.setFont(font);
            #
            # self.gpiorFrame = QtWidgets.QFrame(microcontrollerBlock)
            # self.gpiorFrame.setGeometry(QtCore.QRect(390, 150, 120, 80))
            # self.gpiorFrame.setFrameShape(QtWidgets.QFrame.Panel)
            # self.gpiorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            # self.gpiorFrame.setLineWidth(2)
            # self.gpiorFrame.setStyleSheet("QWidget { background-color: #14aaff }")
            # self.gpiorFrame.setObjectName("gpiorFrame")
            # self.gpiorLabel = QtWidgets.QLabel(self.gpiorFrame)
            # self.gpiorLabel.setGeometry(QtCore.QRect(20, 20, 67, 41))
            # self.gpiorLabel.setScaledContents(False)
            # self.gpiorLabel.setAlignment(QtCore.Qt.AlignCenter)
            # self.gpiorLabel.setWordWrap(True)
            # self.gpiorLabel.setObjectName("gpiorLabel")
            # self.gpiorLabel.setText("GPIOR [2:0]")
            # self.gpiorLabel.setFont(font);
            #
            #
            # self.tc0Frame = QtWidgets.QFrame(microcontrollerBlock)
            # self.tc0Frame.setGeometry(QtCore.QRect(390, 260, 120, 80))
            # self.tc0Frame.setFrameShape(QtWidgets.QFrame.Panel)
            # self.tc0Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            # self.tc0Frame.setStyleSheet("QWidget { background-color: #14aaff }")
            # self.tc0Frame.setLineWidth(2)
            # self.tc0Frame.setObjectName("tc0Frame")
            # self.tc0Label = QtWidgets.QLabel(self.tc0Frame)
            # self.tc0Label.setGeometry(QtCore.QRect(30, 20, 67, 41))
            # self.tc0Label.setScaledContents(False)
            # self.tc0Label.setAlignment(QtCore.Qt.AlignCenter)
            # self.tc0Label.setWordWrap(True)
            # self.tc0Label.setObjectName("tc0Label")
            # self.tc0Label.setText("TC 0            (8-bit)")
            # self.tc0Label.setFont(font);
            #
            #
            # self.spiFrame = QtWidgets.QFrame(microcontrollerBlock)
            # self.spiFrame.setGeometry(QtCore.QRect(390, 410, 120, 80))
            # self.spiFrame.setFrameShape(QtWidgets.QFrame.Panel)
            # self.spiFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            # self.spiFrame.setStyleSheet("QWidget { background-color: #14aaff }")
            # self.spiFrame.setLineWidth(2)
            # self.spiFrame.setObjectName("spiFrame")
            # self.spiLabel = QtWidgets.QLabel(self.spiFrame)
            # self.spiLabel.setGeometry(QtCore.QRect(30, 20, 67, 41))
            # self.spiLabel.setScaledContents(False)
            # self.spiLabel.setAlignment(QtCore.Qt.AlignCenter)
            # self.spiLabel.setWordWrap(True)
            # self.spiLabel.setObjectName("spiLabel")
            # self.spiLabel.setText("SPI 0            (8-bit)")
            # self.spiLabel.setFont(font);
            #
            #
            #
            # self.usartFrame = QtWidgets.QFrame(microcontrollerBlock)
            # self.usartFrame.setGeometry(QtCore.QRect(210, 380, 120, 80))
            # self.usartFrame.setFrameShape(QtWidgets.QFrame.Panel)
            # self.usartFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            # self.usartFrame.setStyleSheet("QWidget { background-color: #14aaff }")
            # self.usartFrame.setLineWidth(2)
            # self.usartFrame.setObjectName("usartFrame")
            # self.usartLabel = QtWidgets.QLabel(self.usartFrame)
            # self.usartLabel.setGeometry(QtCore.QRect(30, 30, 67, 17))
            # self.usartLabel.setAlignment(QtCore.Qt.AlignCenter)
            # self.usartLabel.setObjectName("usartLabel")
            # self.usartLabel.setText("USART 0")
            # self.usartLabel.setFont(font);

        # self.backNavigationButton = QtWidgets.QPushButton(microcontrollerBlock)
        # self.backNavigationButton.setGeometry(QtCore.QRect(460, 20, 89, 25))
        # self.backNavigationButton.setObjectName("backNavigationButton")

            # self.retranslateUi(microcontrollerBlock)
            # QtCore.QMetaObject.connectSlotsByName(microcontrollerBlock)

            # Ui_microcontrollerBlock.rightFrame.layout.addWidget(microcontrollerBlock)

    # def retranslateUi(self, microcontrollerBlock):
    #     _translate = QtCore.QCoreApplication.translate
    #     microcontrollerBlock.setWindowTitle(_translate("microcontrollerBlock", "Form"))
    #     self.flashLabel.setText(_translate("microcontrollerBlock", "Flash"))
    #     self.eepromLabel.setText(_translate("microcontrollerBlock", "EEPROM"))
    #     self.tc1Label.setText(_translate("microcontrollerBlock", "TC 1            (8-bit)"))
    #     self.tc2Label.setText(_translate("microcontrollerBlock", "TC 2            (8-bit)"))
    #     self.gpiorLabel.setText(_translate("microcontrollerBlock", "GPIOR [2:0]"))
    #     self.tc0Label.setText(_translate("microcontrollerBlock", "TC 0            (8-bit)"))
    #     self.spiLabel.setText(_translate("microcontrollerBlock", "SPI 0            (8-bit)"))
    #     self.watchdogLabel.setText(_translate("microcontrollerBlock", "Watchdog timer"))
    #     self.usartLabel.setText(_translate("microcontrollerBlock", "USART 0"))
    #     # self.backNavigationButton.setText(_translate("microcontrollerBlock", "Back"))

    @staticmethod
    def getInstance():
        return  Ui_microcontrollerBlock.rightFrame;

