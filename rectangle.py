'''
This is a file with realisations for geometric functions for a rectangle
'''

import unittest

def area(a, b):  
    '''
    Returns area of a rectangle by given lengths of its 2 neighbour edges.
        
        Parameters:
            a (int / float): Length of 1st edge of a rectangle.
            b (int / float): Length of 2nd edge of a rectangle, having a common vertex with 1st edge.

        Return value:
            area (int / float): Area of a rectangle with edges of length a and b. Formula is "area = a * b".
            Value may be imprecise to insignificant extent, as floating point calculations / Python string math can be used when passing floating point values.

        Usage example:
            area(5, 6)
            function returns 30
    '''
    return a * b  

def perimeter(a, b):  
    '''
    Returns perimeter of a rectangle by given lengths of its 2 neighbour edges.
    
        Parameters:
            a (int / float): Length of 1st edge of a rectangle.
            b (int / float): Length of 2nd edge of a rectangle, having a common vertex with 1st edge.

        Return value:
            perimeter (int / float): Perimeter of a rectangle with edges of length a and b. Formula is "perimeter = 2a + 2b".
            Value may be imprecise to insignificant extent, as floating point calculations / Python string math can be used when passing floating point values.

        Usage example:
            perimeter(4.5, 1)
             function returns 11
    '''
    return 2 * a + 2 * b 

class RectangleTestCase(unittest.TestCase):
    # Area tests 
    def test_area_zero(self):
        for x in [-1, 0, 1, 7, 1000000]:
            with self.subTest(x=x):
                self.assertEqual(area(x, 0), 0)
                self.assertEqual(area(0, x), 0)

    def test_area_float(self):
        self.assertEqual(area(0.5, 0.5), 0.25)
        self.assertEqual(area(111.1, 222.2), 24686.42)

    def test_area_edge(self):
        self.assertEqual(area(1000000, 999999), 999999000000)

    # Perimeter tests
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_float(self):
        self.assertEqual(perimeter(0.6, 1.4), 4)
        self.assertEqual(perimeter(20, 1.5), 43)
        self.assertEqual(perimeter(0.001, 2), 4.002)

    def test_perimeter_edge(self):
        self.assertEqual(perimeter(1000000, 555555), 3111110)