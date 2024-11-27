'''
This is a file with realisations for geometric functions for a triangle
'''

import unittest

def area(a, h):  
    '''
    Returns area of a triangle by given lengths of its 2 height and length of edge, to which height is drawn.
        
        Parameters:
            a (int / float): Length of an edge of a triangle, to which height is drawn.
            h (int / float): Length of a height of a triangle.

        Return value:
            area (int / float): Area of a triangle with height h and length of edge (to which height drawn) a. Formula is "area = a * h / 2".
            Value may be imprecise to insignificant extent, as floating point calculations / Python string math can be used when passing floating point values.

        Usage example:
            area(5, 3)
            function returns 7.5
    '''
    return a * h / 2  

def perimeter(a, b, c):  
    '''
    Returns perimeter of a triangle by given lengths of its edges.
        
        Parameters:
            a (int / float): Length of 1st edge of a triangle.
            b (int / float): Length of 2nd edge of a triangle.
            c (int / float): Length of 3rd edge of a triangle.

        Return value:
            perimeter (int / float): Perimeter of a triangle with edges of length a, b, c. Formula is "perimeter = a + b + c".
            Value may be imprecise to insignificant extent, as floating point calculations / Python string math can be used when passing floating point values.

        Usage example:
            area(2.5, 5, 6.5)
            function returns 14
    '''
    return a + b + c  


class TriangleTestCase(unittest.TestCase):
    # Area tests 
    def test_area_zero(self):
        for x in [-1, 0, 1, 7, 1000000]:
            with self.subTest(x=x):
                self.assertEqual(area(x, 0), 0)
                self.assertEqual(area(0, x), 0)

    def test_area_float(self):
        self.assertEqual(area(0.5, 0.5), 0.125)
        self.assertEqual(area(111.1, 222.2), 12343.21)

    def test_area_edge(self):
        self.assertEqual(area(1000000, 999999), 499999500000)

    # Perimeter tests
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_float(self):
        self.assertEqual(perimeter(0.6, 1.4, 2.5), 4.5)
        self.assertEqual(perimeter(20, 1.5, 40.6), 62.1)

    def test_perimeter_edge(self):
        self.assertEqual(perimeter(1000000, 555555, 995), 1556550)