# -*- coding: UTF-8 -*-
'''
Created on 28-05-2015

@author: user
'''
import unittest
from ex11.Ex11Python import next_number 
from ex11.Ex11Python import sequence
from ex11.Ex11Python import longestCollatzSequence

class Ex11PythonTest(unittest.TestCase):
    
    def TestRulesForTheEvenNumber(self):
        self.assertEqual(next_number(2), 1)  
    
    def TestRulesForTheOddNumber(self):
        self.assertEqual(next_number(3), 10)
    
    def TestDequence(self):
        result = sequence(13)
        self.assertEqual(result, 10)

    def TestSequenceLongestCollatzSequence(self):
        result = longestCollatzSequence()
        self.assertEqual(result, 837799)   

if __name__ == '__main__':
    unittest.main()