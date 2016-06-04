'''
Created on

@author: Yanqing
'''
import unittest
from src.Helpers.Helpers import *
from src.Helpers.ApproxMaxMI import *
from src.MINE import MINE


class TestMINE(unittest.TestCase):
    #############################################################################
    #test line relationship, the result should be 1
    def test_MINE1(self):
        D = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)]
        n = len(D)
        B = int(n**0.9)
        c = 1.6
        M = MINE(D)
        result = M.ApproxCharacteristicMatrix(B, c)
        self.assertAlmostEqual(result, 1.0, 2, "TestMINE testcase 1")
            
    def test_MINE2(self):
        x = np.linspace(-1,1,21)
        D = [(x[i], 1 - x[i]**2) for i in range(0,len(x))]
        n = len(D)
        B = int(n**0.6)
        c = 1.6
        M = MINE(D)
        result = M.ApproxCharacteristicMatrix(B, c)
        print result
        self.assertAlmostEqual(result, 1.0, 2, "TestMINE testcase 2")
        
    def test_MINE3(self):
        x = np.linspace(-1,1,100)
        D = [(x[i], 1 - x[i]**3) for i in range(0,len(x))]
        n = len(D)
        B = int(n**0.6)
        c = 1.6
        M = MINE(D)
        result = M.ApproxCharacteristicMatrix(B, c)
        print result
        self.assertAlmostEqual(result, 1.0, 2, "TestMINE testcase 3")    
if __name__ == '__main__':
    unittest.main()