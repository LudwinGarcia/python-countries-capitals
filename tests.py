import os
import nose
import unittest
from application import ProgramControl


APPLICATION_DIR = 'application.py'

class TestApplication(unittest.TestCase):
	
	def test_has_numbers(self):
		Test = ProgramControl()
		assert (Test.has_numbers('Hola') == False)
		assert (Test.has_numbers('H1') == True)
		
	def test_lint(self):
		resultado = os.system('pylint' + " " +APPLICATION_DIR)
		return resultado


if __name__ == '__main__':
    unittest.main()

