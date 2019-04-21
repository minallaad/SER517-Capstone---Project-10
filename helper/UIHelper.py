'''
Description: This class provides functionalities for updating the value on UI. It also provide basic helper
             functions which are required for common tasks.

'''

import Components.Globalmap


class UIHelper():
    '''
    Description: Function to convert an string value to binary representation of 8 bits.
    @param value: Value that needs to be converted in binary.
    '''

    @staticmethod
    def convertValueToBin(value):
        binVal = bin(value)[2:]
        if len(binVal) < 8:
            binVal = '0' * (8 - len(binVal)) + binVal
        return binVal

    '''
    Description: Function to referesh the clicked values of the port.
    '''

    @staticmethod
    def refreshItems():
        Components.Globalmap.Map.port_clicked = None

    '''
    Description: Function to set the port values for each port based on the name of the port.
    @param key: name of the port for which the value needs to be updated.
    @param value: value of the port. It is converted to 8 bit binary representation.
    '''

    @staticmethod
    def setPortValues(key, value):
        binVal = UIHelper.convertValueToBin(value)
        for i in range(len(binVal) - 1, -1, -1):
            update = Components.Globalmap.Map.port_register_map[key] + str(len(binVal) - i - 1)
            value = int(binVal[i])
            Components.Globalmap.Map.pin_portRegisterValue_map[update] = value

    '''
    Description: Function to set the DDR values for each DDR based on the name of the DDR.
    @param key: name of the DDR for which the value needs to be updated.
    @param value: value of the DDR. It is converted to 8 bit binary representation.
    '''

    @staticmethod
    def setDdrValues(key, value):
        binVal = UIHelper.convertValueToBin(value)
        for i in range(len(binVal) - 1, -1, -1):
            update = Components.Globalmap.Map.port_register_map[key] + str(len(binVal) - i - 1)
            value = int(binVal[i])
            Components.Globalmap.Map.pin_ddrRegisterValue_map[update] = value

    '''
    Description: Function to set the PIN values for each PIN based on the name of the PIN.
                 It also updates the color of the pin.
    @param key: name of the PIN for which the value needs to be updated.
    @param value: value of the PIN. It is converted to 8 bit binary representation.
    '''

    @staticmethod
    def setPinValues(key, value, pin):
        binVal = UIHelper.convertValueToBin(value)
        for i in range(len(binVal) - 1, -1, -1):
            update = Components.Globalmap.Map.port_register_map[key] + str(len(binVal) - i - 1)
            value = int(binVal[i])
            Components.Globalmap.Map.pin_pinRegisterValue_map[update] = value
            pin.setPinStatus(update, value)
