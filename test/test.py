import unittest


#module to be developed further

class TestGUI(unittest.TestCase):
	
	def test_gui(self):
		pass

	def test_log(self): 
		log = open("logs.log")
		pass
		
	def test_eeprom(self): 
		pass

	def test_flash(self): 
		pass
	
	def test_watch(self): 
		pass
	
	def test_tc_0_8bit(self): 
		pass

	def test_tc_1_8bit(self): 
		pass
	
	def test_16bit(self): 
		pass

	def test_flash(self): 
		pass
	
	def test_usart_8bit(self): 
		pass
	
	def test_spi(self): 
		pass

class TestGDB(unittest.TestCase):
	
	def test_gdb_connection(self):
		pass

class TestMem(unittest.TestCase):
	
	def test_mem(self):
		pass

	




if __name__ == '__main__':
        unittest.main()
