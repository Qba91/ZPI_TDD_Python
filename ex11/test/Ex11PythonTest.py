# -*- coding: UTF-8 -*-
'''
Created on 28-05-2015

@author: user
'''
import unittest
from ex11.Ex11Python import next_number 

class Ex11PythonTest(unittest.TestCase):
    
    def TestRulesForTheEvenNumber(self):
        self.assertEqual(next_number(2), 1)  
    
    def TestRulesForTheOddNumber(self):
        self.assertEqual(next_number(3), 10)
        

if __name__ == '__main__':
    unittest.main()