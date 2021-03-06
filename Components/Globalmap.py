'''
This class is used to store global maps for various components to access them from UI and Simulavr Adaptor.
Ui can access these map's for specific components to retrieve the value and display it on the UI.
Adaptor helps in updating these maps when the values are fetched from specific memory addresses.
'''

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget


class Map():
    '''
    Description: map for tracking the currently clicked port
    '''
    port_clicked = None

    '''
    Description: global variable to hold currently clicked register value
    '''
    register_clicked = None

    '''
    Description: global variable to hold currently clicked register value
    '''
    register_clicked_type = None

    '''
    Description: global map which consists the values of various components.
    '''
    map = {}

    refresh_ui_flag = False

    '''refresh flag to check if the refresh is clicked.'''
    refresh_flag = False

    '''EEPROM address variable used to fetch the data from. It gets updated by the EEPROM UI.'''
    eeprom_address = 0
    port_address_map = {"PORTD": 0X2B, 'PORTC': 0X28, 'PORTB': 0X23}
    port_register_map = {"PORTD": "PD", "PORTB": "PB", "PORTC": "PC"}
    pin_portRegisterValue_map = {"PD0": 0, "PD1": 0, "PD2": 0, "PD3": 0, "PD4": 0, "PD5": 0, "PD6": 0, "PD7": 0,
                                 "PC0": 0, "PC1": 0, "PC2": 0, "PC3": 0, "PC3": 0,
                                 "PC5": 0, "PC6": 0, "PC7": 0, "PB0": 0, "PB1": 0, "PB2": 0, "PB3": 0, "PB4": 0,
                                 "PB5": 0, "PB6": 0, "PB7": 0, }
    pin_ddrRegisterValue_map = {"PD0": 0, "PD1": 0, "PD2": 0, "PD3": 0, "PD4": 0, "PD5": 0, "PD6": 0, "PD7": 0,
                                "PC0": 0, "PC1": 0, "PC2": 0, "PC3": 0, "PC3": 0,
                                "PC5": 0, "PC6": 0, "PC7": 0, "PB0": 0, "PB1": 0, "PB2": 0, "PB3": 0, "PB4": 0,
                                "PB5": 0, "PB6": 0, "PB7": 0, }
    pin_pinRegisterValue_map = {"PD0": 0, "PD1": 0, "PD2": 0, "PD3": 0, "PD4": 0, "PD5": 0, "PD6": 0, "PD7": 0,
                                "PC0": 0, "PC1": 0, "PC2": 0, "PC3": 0, "PC3": 0,
                                "PC5": 0, "PC6": 0, "PC7": 0, "PB0": 0, "PB1": 0, "PB2": 0, "PB3": 0, "PB4": 0,
                                "PB5": 0, "PB6": 0, "PB7": 0, }

    registerAddressMap = {'CORE.SREG': 0x5F, 'CORE.GTCCR': 0x43, 'CORE.ASSR': 0xB6, 'CORE.CLKPR': 0x61,
                          'CORE.OSCCAL': 0x66,
                          'CORE.EICRA': 0x69, 'CORE.EIMSK': 0x3D, 'CORE.EIFR': 0x3C, 'CORE.PCICR': 0x68,
                          'CORE.PCIFR': 0x3B,
                          'CORE.PCMSK0': 0x6B, 'CORE.PCMSK1': 0x6C, 'CORE.PCMSK2': 0x6D, 'CORE.GPIOR0': 0x3E,
                          'CORE.GPIOR1': 0x4A,
                          'CORE.GPIOR2': 0x4B, 'PORTB.PORT': 0x25, 'PORTB.PIN': 0x23, 'PORTB.DDR': 0x24,
                          'PORTC.PORT': 0x28,
                          'PORTC.PIN': 0x26, 'PORTC.DDR': 0x27, 'PORTD.PORT': 0x2B, 'PORTD.PIN': 0x29,
                          'PORTD.DDR': 0x2A,
                          'ACOMP.ACSR': 0x50, 'EEPROM.EEARH': 0x42, 'EEPROM.EEARL': 0x41, 'EEPROM.EEDR': 0x40,
                          'EEPROM.EECR': 0x3F,
                          'TMRIRQ0.TIMSK0': 0x6E, 'TMRIRQ0.TIFR0': 0x35, 'TIMER0.Counter': 0x43, 'TIMER0.TCNT': 0x46,
                          'TIMER0.OCRA': 0x47,
                          'TIMER0.OCRB': 0x47, 'TIMER0.TCCRA': 0x44, 'TIMER0.TCCRB': 0x45, 'TMRIRQ1.TIMSK1': 0x6F,
                          'TMRIRQ1.TIFR1': 0x36,
                          'TIMER1.TCNTH': 0x85, 'TIMER1.TCNTL': 0x84, 'TIMER1.OCRAH': 0x89, 'TIMER1.OCRAL': 0x88,
                          'TIMER1.OCRBH': 0x8B,
                          'TIMER1.OCRBL': 0x8A, 'TIMER1.ICRH': 0x87, 'TIMER1.ICRL': 0x86, 'TIMER1.TCCRA': 0x80,
                          'TIMER1.TCCRB': 0x81,
                          'TIMER1.TCCRC': 0x82, 'TMRIRQ2.TIMSK2': 0x70, 'TMRIRQ2.TIFR2': 0x37, 'TIMER2.TCNT': 0xB2,
                          'TIMER2.OCRA': 0xB3,
                          'TIMER2.OCRB': 0xB4, 'TIMER2.TCCRA': 0xB0, 'TIMER2.TCCRB': 0xB1, 'AD.ADCH': 0x79,
                          'AD.ADCL': 0x78,
                          'AD.ADCSRA': 0x7A, 'AD.ADCSRB': 0x7B, 'AD.ADMUX': 0x7C, 'SPI.SPDR': 0x4E, 'SPI.SPSR': 0x4D,
                          'SPI.SPCR': 0x4C,
                          'UART0.UDR': 0xC6, 'UART0.UBRR0H': 0xC5, 'UART0.UBRR0L': 0xC4, 'UART0.UCSRA': 0xC0,
                          'UART0.UCSRB': 0xC1}

    memory_map = {}

    def __init__(self):
        """ Virtually private constructor. """
        super().__init__()
        if Map.map != None:
            raise Exception("This class is a singleton!")
        else:
            Map.map = {}

    '''
    Description: Method to get the already existing instance of the map. If not, then create a new one.
    '''

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Map.map == None:
            Map()
        return Map.map

    '''
    Description: Function to access a specific value from the map. The key here is the component name for which
                 the value needs to be accessed.
    '''

    @staticmethod
    def getValue(key):
        """ Static access method. """
        if key in Map.map:
            return Map.map[key]
        else:
            return None

    '''
    Description: Function to update global map values.
    '''

    @staticmethod
    def setGlobalMap(valueMap):
        """ Static access method. """
        Map.map = valueMap

    @staticmethod
    def getPortAddressMap():
        """ Static access method. """
        return Map.port_address_map

    @staticmethod
    def getPortRegisterMap():
        """ Static access method. """
        return Map.port_register_map

    '''
    Description: Function to access the address of specific register.
    @param key: The name of the register for which the value needs to be accessed.
    '''

    @staticmethod
    def getRegisterAddress(key):
        if key in Map.registerAddressMap:
            return Map.registerAddressMap[key]
        else:
            return None

    @staticmethod
    def getMemoryDumpMap():
        """ Static access method. """
        return Map.memory_map
