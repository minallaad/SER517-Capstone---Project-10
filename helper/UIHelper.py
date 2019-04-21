import Components.Globalmap

class UIHelper():

    #convert a value to binary of length 8
    @staticmethod
    def convertValueToBin(value):
        binVal = bin(value)[2:]
        if len(binVal) < 8:
            binVal = '0' * (8 - len(binVal)) + binVal
        return binVal

    @staticmethod
    def refreshItems():
        Components.Globalmap.Map.port_clicked = None

    #update the specific port values
    @staticmethod
    def setPortValues(key, value):
        binVal = UIHelper.convertValueToBin(value)
        for i in range(len(binVal) - 1, -1, -1):
            update = Components.Globalmap.Map.port_register_map[key] + str(len(binVal) - i - 1)
            value = int(binVal[i])
            Components.Globalmap.Map.pin_portRegisterValue_map[update] = value

    #setting the DDR values as per ports
    @staticmethod
    def setDdrValues(key, value):
        binVal = UIHelper.convertValueToBin(value)
        for i in range(len(binVal) - 1, -1, -1):
            update = Components.Globalmap.Map.port_register_map[key] + str(len(binVal) - i - 1)
            value = int(binVal[i])
            Components.Globalmap.Map.pin_ddrRegisterValue_map[update] = value

    #set the pin values to high or low
    @staticmethod
    def setPinValues(key, value, pin):
        binVal = UIHelper.convertValueToBin(value)
        for i in range(len(binVal) - 1, -1, -1):
            update = Components.Globalmap.Map.port_register_map[key] + str(len(binVal) - i - 1)
            value = int(binVal[i])
            Components.Globalmap.Map.pin_pinRegisterValue_map[update] = value
            pin.setPinStatus(update, value)
