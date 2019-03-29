# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget


class Map():    # Used to switch between multiple layout


    map = {}
    port_address_map = {"PORTD":0X2B, 'PORTC':0X28, 'PORTB':0X23}
    port_register_map = {"PORTD": "PD", "PORTB": "PB", "PORTC": "PC"}
    ddr_address_map = {"DDRD": 0X2A, 'DDRC': 0X27, 'DDRB': 0X24}

    def __init__(self):
        """ Virtually private constructor. """
        super().__init__()
        if Map.map != None:
            raise Exception("This class is a singleton!")
        else:
            Map.map = {}


    @staticmethod
    def getInstance():
        """ Static access method. """
        if Map.map == None:
            Map()
        return Map.map

    @staticmethod
    def getValue(key):
        """ Static access method. """
        if key in Map.map:
            return Map.map[key]
        else:
            return None

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

