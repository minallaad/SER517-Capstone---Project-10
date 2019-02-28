# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QListWidget, QMessageBox, QTableWidget, QTableWidgetItem



class Register_Values():

    List = []
    tableWidget = None

    def __init__(self):
        if self.tableWidget == None:
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(1)
            self.tableWidget.setColumnCount(3)

            self.tableWidget.setItem(0, 0, QTableWidgetItem("Name"))
            self.tableWidget.setItem(0, 1, QTableWidgetItem("Address"))
            self.tableWidget.setItem(0, 2, QTableWidgetItem("Value"))


    def getTable(self): # Return Single Instance of Register Value Table Widget
        return self.tableWidget

    def addRegisterValues(self,name,address,value):   # Function to add Register details in Register Value Table
        return self.List






