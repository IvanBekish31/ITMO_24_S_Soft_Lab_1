'''
This is a file with realisations for geometric functions for a triangle
'''

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