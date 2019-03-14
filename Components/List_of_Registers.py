# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import  QMessageBox , QListWidget
from PyQt5 import  QtCore

class List_of_Registers(QListWidget):


    listWidget = None

    def __init__(self):
        """ Virtually private constructor. """
        super().__init__()
        if List_of_Registers.listWidget != None:
            raise Exception("This class is a singleton!")
        else:
            # Add the correct register values from tracelist and update this comment
            pins = ['CORE.GPIOR2', 'PORTB.PORT', 'PORTB.PIN', 'PORTB.DDR', 'PORTB.B0-Out', 'IRQ.VECTOR0', 'EEPROM.EEDR',
                    'TMRIRQ0.TIMSKO', 'TIMER0.Counter', 'TIMER0.TCNT', 'SPI.SPDR', 'UART0.UDR', 'CORE.GPIOR2',
                    'PORTB.PORT',
                    'PORTB.PIN', 'PORTB.DDR', 'PORTB.B0-Out', 'IRQ.VECTOR0', 'EEPROM.EEDR',
                    'TMRIRQ0.TIMSKO', 'TIMER0.Counter', 'TIMER0.TCNT', 'SPI.SPDR', 'UART0.UDR', 'CORE.GPIOR2',
                    'PORTB.PORT',
                    'PORTB.PIN', 'PORTB.DDR', 'PORTB.B0-Out', 'IRQ.VECTOR0', 'EEPROM.EEDR',
                    'TMRIRQ0.TIMSKO', 'TIMER0.Counter',
                    'TIMER0.TCNT', 'SPI.SPDR',
                    'UART0.UDR']
            List_of_Registers.listWidget = QListWidget()
            List_of_Registers.listWidget = QListWidget()
            List_of_Registers.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            List_of_Registers.listWidget.itemClicked.connect(List_of_Registers.Clicked)
            List_of_Registers.listWidget.move(90, 195)

            for i in pins:
                List_of_Registers.listWidget.addItem(i)





    @staticmethod
    def getInstance():
        """ Static access method. """
        if List_of_Registers.listWidget == None:
            List_of_Registers()
        return List_of_Registers.listWidget


    @staticmethod
    def Clicked(self, item):  # On Click Register name calls this function
        QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())


