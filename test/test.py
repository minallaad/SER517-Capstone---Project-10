import unittest


#module to be developed further

class TestGUI(unittest.TestCase):
	def test_gui(self):
		pass
        
        def test_slider(self):

            log = open("logs.log")

            print(log.readlines())

class TestGDB(unittest.TestCase):
        def test_gdb_connection(self):
                pass


if __name__ == '__main__':
	unittest.main()
