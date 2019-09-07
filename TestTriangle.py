#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsocelesTriangle(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 should be Isoceles')

    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be Scalene')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1,1,2),'NotATriangle','1,1,2 should be NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1,3,1),'NotATriangle','1,3,1 should be NotATriangle')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testInvalidA(self): 
        self.assertEqual(classifyTriangle(5.1,3.1,4.1),'InvalidInput','5.1,3.1,4.1 is InvalidInput')

    def testInvlaidB(self):
        self.assertEqual(classifyTriangle(-3,-4,-5),'InvalidInput','-3,-4,-5 should be InvalidInput')

    def testInvlaidC(self):
        self.assertEqual(classifyTriangle(300,400,500),'InvalidInput','300,400,500 should be InvalidInput')

    def testInvalidD(self):
        self.assertEqual(classifyTriangle(0,1,2),'InvalidInput','0,1,2 should be InvalidInput')

    def testInvalidE(self):
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 should be InvalidInput')


        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

