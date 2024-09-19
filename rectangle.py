'''
This is a file with realisations for geometric functions for a rectangle
'''

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