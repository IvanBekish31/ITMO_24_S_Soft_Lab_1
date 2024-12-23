import math
import unittest

'''
This is a file with realisations for geometric functions for a circle
'''


def area(r):
    '''
    Returns area of a circle by its given radius.
        
        Parameters:
            r (int / float): Radius of a circle.

        Return value:
            area (float): Area of a circle with radius r. Formula is "area = pi * r^2".
            Value is imprecise, as floating point calculations / python string math is used.
            Value for pi is taken from standard "math" library.

        Usage example:
            area(8)
    '''
    return math.pi * r * r


def perimeter(r):
    '''
        Returns perimeter of a circle by its given radius.
        
        Parameters:
            r (int / float): Radius of a circle.

        Return value:
            perimeter (float): Perimeter of a circle with radius r. Formula is "perimeter = 2 * pi * r".
            Value is imprecise, as floating point calculations / python string math is used.
            Value for pi is taken from standard "math" library.

        Usage example:
            perimeter(6.3)
    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    # Area tests 
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_float(self):
        self.assertEqual(area(1 / math.pi), 1 / math.pi)

    def test_area_edge(self):
        self.assertEqual(area(1000000), 1000000000000  * math.pi)
        
    # Perimeter tests
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)


    def test_perimeter_float(self):
        self.assertEqual(perimeter(4.4), 8.8 * math.pi)
    
    def test_perimeter_edge(self):
        self.assertEqual(perimeter(1000000000000000), 6283185307179586)
