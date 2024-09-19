'''
This is a file with realisations for geometric functions for a square
'''

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
