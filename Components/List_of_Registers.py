'''
This class is used to fetch the list of registers available in various components of microcontroller.
'''

from PyQt5.QtWidgets import  QMessageBox , QListWidget
from PyQt5 import  QtCore

import Components.Register_Values
import Components.Globalmap

class List_of_Registers(QListWidget):

    pins = ['CORE.SREG', 'CORE.GTCCR', 'CORE.ASSR', 'CORE.CLKPR',
                          'CORE.OSCCAL', 'CORE.EICRA', 'CORE.EIMSK', 'CORE.EIFR', 'CORE.PCICR',
                          'CORE.PCIFR', 'CORE.PCMSK0',
                          'CORE.PCMSK1', 'CORE.PCMSK2', 'CORE.GPIOR0', 'CORE.GPIOR1',
                          'CORE.GPIOR2', 'PORTB.PORT',
                          'PORTB.PIN', 'PORTB.DDR', 'PORTC.PORT', 'PORTC.PIN',
                          'PORTC.DDR', 'PORTD.PORT',
                          'PORTD.PIN', 'PORTD.DDR', 'ACOMP.ACSR', 'EEPROM.EEARH',
                          'EEPROM.EEARL', 'EEPROM.EEDR',
                          'EEPROM.EECR', 'TMRIRQ0.TIMSK0', 'TMRIRQ0.TIFR0',
                          'TIMER0.Counter', 'TIMER0.TCNT', 'TIMER0.OCRA', 'TIMER0.OCRB',
                          'TIMER0.TCCRA', 'TIMER0.TCCRB', 'TMRIRQ1.TIMSK1', 'TMRIRQ1.TIFR1', 'TIMER1.TCNTH',
                          'TIMER1.TCNTL', 'TIMER1.OCRAH', 'TIMER1.OCRAL', 'TIMER1.OCRBH', 'TIMER1.OCRBL',
                          'TIMER1.ICRH', 'TIMER1.ICRL', 'TIMER1.TCCRA', 'TIMER1.TCCRB', 'TIMER1.TCCRC',
                          'TMRIRQ2.TIMSK2', 'TMRIRQ2.TIFR2', 'TIMER2.TCNT', 'TIMER2.OCRA', 'TIMER2.OCRB',
                          'TIMER2.TCCRA', 'TIMER2.TCCRB', 'AD.ADCH', 'AD.ADCL',
                          'AD.ADCSRA', 'AD.ADCSRB', 'AD.ADMUX', 'SPI.SPDR', 'SPI.SPSR', 'SPI.SPCR',
                          'UART0.UDR', 'UART0.UBRR0H', 'UART0.UBRR0L', 'UART0.UCSRA', 'UART0.UCSRB']

    listWidget = None

    def __init__(self):
        """ Virtually private constructor. """
        super().__init__()
        if List_of_Registers.listWidget != None:
            raise Exception("This class is a singleton!")
        else:
            # Add the correct register values from tracelist and update this comment

            List_of_Registers.listWidget = QListWidget()
            List_of_Registers.listWidget = QListWidget()
            List_of_Registers.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            List_of_Registers.listWidget.move(90, 195)

            for i in self.pins:
                List_of_Registers.listWidget.addItem(i)

            List_of_Registers.listWidget.itemClicked.connect(List_of_Registers.Clicked)



    @staticmethod
    def getInstance():
        """ Static access method. """
        if List_of_Registers.listWidget == None:
            List_of_Registers()
        return List_of_Registers.listWidget

    '''
    Description: to fetch the value of the register clicked
    '''
    def Clicked(self):
        value = Components.Globalmap.Map.getValue(self.text())
        Components.Globalmap.Map.register_clicked = self.text()
        Components.Globalmap.Map.register_clicked_type = 'r'
        address = Components.Globalmap.Map.getRegisterAddress(self.text())
        Components.Register_Values.Register_Values.clearList()

        if value !=None and address!= None:
            Components.Register_Values.Register_Values.addRegister(self.text(), hex(address), hex(value))
        else:
            Components.Register_Values.Register_Values.addRegister(self.text(), "NA", "NA")



