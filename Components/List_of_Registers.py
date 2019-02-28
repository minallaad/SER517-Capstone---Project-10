# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import  QMessageBox , QListWidget
from PyQt5 import  QtCore

class List_of_Registers():


    listWidget = None

    def __init__(self):
        if self.listWidget == None:
            pins = ['CORE.GPIOR2', 'PORTB.PORT', 'PORTB.PIN', 'PORTB.DDR', 'PORTB.B0-Out', 'IRQ.VECTOR0', 'EEPROM.EEDR',
                    'TMRIRQ0.TIMSKO', 'TIMER0.Counter', 'TIMER0.TCNT', 'SPI.SPDR', 'UART0.UDR', 'CORE.GPIOR2', 'PORTB.PORT',
                    'PORTB.PIN', 'PORTB.DDR', 'PORTB.B0-Out', 'IRQ.VECTOR0', 'EEPROM.EEDR',
                    'TMRIRQ0.TIMSKO', 'TIMER0.Counter', 'TIMER0.TCNT', 'SPI.SPDR', 'UART0.UDR', 'CORE.GPIOR2', 'PORTB.PORT',
                    'PORTB.PIN', 'PORTB.DDR', 'PORTB.B0-Out', 'IRQ.VECTOR0', 'EEPROM.EEDR',
                    'TMRIRQ0.TIMSKO', 'TIMER0.Counter',
                    'TIMER0.TCNT', 'SPI.SPDR',
                    'UART0.UDR']  # Add the correct register values from tracelist and update this comment

            listWidget = myListWidget()
            listWidget.itemClicked.connect(listWidget.Clicked)
            listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            listWidget.move(90, 195)

            for i in pins:
                listWidget.addItem(i)

    def getListOfRegisters(self):
        return self.listWidget

class myListWidget(QListWidget):

        def Clicked(self, item):
            QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())

