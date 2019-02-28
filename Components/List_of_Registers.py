# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import  QMessageBox , QListWidget
from PyQt5 import  QtCore

class List_of_Registers(QListWidget):


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

            self.listWidget = QListWidget()
            self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            self.listWidget.move(90, 195)

            for i in pins:
                self.listWidget.addItem(i)

    def getListOfRegisters(self):   # Returns Single Instance of Register List Widget
        return self.listWidget

