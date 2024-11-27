'''
This is a file with realisations for geometric functions for a square
'''

import unittest

def area(a):
    '''
    Returns area of a square by given length of its edge.
        
        Parameters:
            a (int / float): Length of any of the edges of a square.

        Return value:
            area (int / float): Area of a square with edges of length a. Formula is "area = a * a".
            Value may be imprecise to insignificant extent, as floating point calculations / Python string math can be used when passing floating point values.

        Usage example:
            area(3.2)
            function returns 10.24
    '''
    return a * a


def perimeter(a):
    '''
    Returns perimeter of a square by given length of its edge.
        
        Parameters:
            a (int / float): Length of any of the edges of a square.

        Return value:
            area (int / float): Perimeter of a square with edges of length a. Formula is "perimeter = 4 * a".
            Value may be imprecise to insignificant extent, as floating point calculations / Python string math can be used when passing floating point values.

        Usage example:
            area(11)
            function returns 44
    '''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    # Area tests 
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_float(self):
        self.assertEqual(area(0.5), 0.25)
        self.assertEqual(area(2.5), 6.25)
        self.assertEqual(area(1.0), 1.0)

    def test_area_edge(self):
        self.assertEqual(area(1000000), 1000000000000)
        

    # Perimeter tests
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)


    def test_perimeter_float(self):
        self.assertEqual(perimeter(0.5), 2)
        self.assertEqual(perimeter(2.5), 10)
        self.assertEqual(perimeter(10.01), 40.04)
    
    def test_perimeter_edge(self):
        self.assertEqual(perimeter(1000000000000), 4000000000000)
