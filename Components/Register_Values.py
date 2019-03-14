# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QListWidget, QMessageBox, QTableWidget, QTableWidgetItem



class Register_Values():

    List = []
    tableWidget = None

    def __init__(self):
        """ Virtually private constructor. """
        super().__init__()
        if Register_Values.tableWidget != None:
            raise Exception("This class is a singleton!")
        else:
            Register_Values.tableWidget = QTableWidget()
            Register_Values.tableWidget.setRowCount(1)
            Register_Values.tableWidget.setColumnCount(3)

            Register_Values.tableWidget.setItem(0, 0, QTableWidgetItem("Name"))
            Register_Values.tableWidget.setItem(0, 1, QTableWidgetItem("Address"))
            Register_Values.tableWidget.setItem(0, 2, QTableWidgetItem("Value"))


    @staticmethod
    def getInstance():
        """ Static access method. """
        if Register_Values.tableWidget == None:
            Register_Values()
        return Register_Values.tableWidget









