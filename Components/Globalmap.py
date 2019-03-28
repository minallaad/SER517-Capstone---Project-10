# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget


class Map():    # Used to switch between multiple layout


    map = None


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
        Map.map = valueMap;



