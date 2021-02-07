# -*- coding: utf-8 -*-
"""
Created on Sun Feb 7 2021

This file shows some simple (and buggy) python code to solve the Triangles assignment.
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: Diaeddin Motan
"""

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """

    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'


    """
    # This determines whether the three parameters can form a triangle or not
    if (a + b > c) and (a + c > b) and (b + c > a):
        if (pow(a, 2) + pow(b, 2)) == pow(c, 2):
            return 'Right'
        elif a == b and b == c:
            return 'Equilateral'
        elif a == b or a == c or b == c:
            return 'Isosceles'
        elif a != b and a != c and b != c:
            return 'Scalene'
    else:
        return 'NotATriangle'



def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(15,20,25),'Right','15,20,25 is a Right triangle')
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 is NotATriangle')
        self.assertEqual(classifyTriangle(3,2,2),'Isosceles','3,2,2 is isosceles')
        self.assertNotEqual(classifyTriangle(4,3,5),'Isosceles','4,3,5 is not isosceles')
        self.assertNotEqual(classifyTriangle(5,6,7),'Isosceles','5,6,7 is not isosceles')
        self.assertEqual(classifyTriangle(5,6,7),'Scalene','5,6,7 is a scalene')

    def testMyTestSet2(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isosceles','Should be isosceles')
        self.assertEqual(classifyTriangle(10,15,30),'NotATriangle','Should be NotATriangle')


if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(3,2,2)
    runClassifyTriangle(4,3,5)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(1,1,10)
    runClassifyTriangle(2,2,2)
    runClassifyTriangle(5,6,7)
    runClassifyTriangle(10,15,30)
    runClassifyTriangle(15,20,35)

    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line



