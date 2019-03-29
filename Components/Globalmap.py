# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget


class Map():    # Used to switch between multiple layout


    map = None
    port_address_map = {0X2B: "PORTD", 0X28: 'PORTC', 0X23: 'PORTB'}
    port_register_map = {"PORTD": "PD", "PORTB": "PB", "PORTC": "PC"}


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

