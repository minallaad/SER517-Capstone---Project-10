# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QListWidget, QMessageBox, QTableWidget, QTableWidgetItem



class Register_Values():

    List = None
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
            Register_Values.List = []

            Register_Values.tableWidget.setItem(0, 0, QTableWidgetItem("Name"))
            Register_Values.tableWidget.setItem(0, 1, QTableWidgetItem("Address"))
            Register_Values.tableWidget.setItem(0, 2, QTableWidgetItem("Value"))


    @staticmethod
    def getInstance():
        """ Static access method. """
        if Register_Values.tableWidget == None:
            Register_Values()
        return Register_Values.tableWidget

    @staticmethod
    def clearList():
        Register_Values.List = []

    @staticmethod
    def updateTable():
        i = 0
        j = 0
        print(len(Register_Values.List))
        Register_Values.tableWidget.setRowCount(len(Register_Values.List)+1)

        while( i<len(Register_Values.List) ):
            print(type(Register_Values.List[0]))
            j = 0
            Register_Values.tableWidget.setItem(i+1, j, QTableWidgetItem(str(Register_Values.List[i].name)))
            j = j+1
            Register_Values.tableWidget.setItem(i+1, j, QTableWidgetItem(str(Register_Values.List[i].address)))
            j = j+1
            Register_Values.tableWidget.setItem(i+1, j, QTableWidgetItem(str(Register_Values.List[i].value)))
            i = i+1

        Register_Values.tableWidget.repaint()

    @staticmethod
    def addRegister(name,address,value):
        print(name,address,value)
        rowObj =row(name,address,value)
        print(rowObj.name)
        print(rowObj.address)
        print(rowObj.value)
        Register_Values.List.append(rowObj)
        Register_Values.updateTable()



class row():
    name = None
    address = None
    value = None

    def __init__(self,name,address,value):
        self.name =  name
        self.address= address
        self.value = value









