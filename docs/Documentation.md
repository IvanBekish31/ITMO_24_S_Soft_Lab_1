# Algorithmic realisation
## Area
- Circle: S = πR<sup>2</sup>
- Rectangle: S = ab
- Square: S = a<sup>2</sup>
- Triangle: S = ah

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Functions

## Circle
From [circle.py](../circle.py)

### area(r)
Returns area of a circle by its given radius.

Parameters:
- r (int / float): Radius of a circle.

Return value:
- area (float): Area of a circle with radius r.

Usage example:
- area(8)

### perimeter(r)
Returns perimeter of a circle by its given radius.

Parameters:
- r (int / float): Radius of a circle.

Return value:
- perimeter (float): Perimeter of a circle with radius r.

Usage example:
- perimeter(6.3)


## Square
From [square.py](../square.py)

### area(a)
Returns area of a square by given length of its edge.

Parameters:
- a (int / float): Length of any of the edges of a square.

Return value:
- area (int / float): Area of a square with edges of length a.

Usage example:
- area(3.2) - function returns 10.24


### perimeter(a)
Returns perimeter of a square by given length of its edge.

Parameters:
- a (int / float): Length of any of the edges of a square.

Return value:
- area (int / float): Perimeter of a square with edges of length a.

Usage example:
- area(11) - function returns 44

## Triangle
From [triangle.py](../triangle.py)

### area(a, h)  
Returns area of a triangle by given lengths of its 2 height and length of edge, to which height is drawn.

Parameters:
- a (int / float): Length of an edge of a triangle, to which height is drawn.
- h (int / float): Length of a height of a triangle.

Return value:
- area (int / float): Area of a triangle with height h and length of edge (to which height drawn) a.

Usage example:
- area(5, 3) - function returns 7.5

### perimeter(a, b, c)
Returns perimeter of a triangle by given lengths of its edges.

Parameters:
- a (int / float): Length of 1st edge of a triangle.
- b (int / float): Length of 2nd edge of a triangle.
- c (int / float): Length of 3rd edge of a triangle.

Return value:
- perimeter (int / float): Perimeter of a triangle with edges of length a, b, c. 
Usage example:
- area(2.5, 5, 6.5) - function returns 14

## Rectangle
From [rectangle.py](../rectangle.py)

### area(a, b)
Returns area of a rectangle by given lengths of its 2 neighbour edges.

Parameters:
- a (int / float): Length of 1st edge of a rectangle.
- b (int / float): Length of 2nd edge of a rectangle, having a common vertex with 1st edge.

Return value:
- area (int / float): Area of a rectangle with edges of length a and b.

Usage example:
- area(5, 6) - function returns 30

### perimeter(a, b)
Returns perimeter of a rectangle by given lengths of its 2 neighbour edges.

Parameters:
- a (int / float): Length of 1st edge of a rectangle.
- b (int / float): Length of 2nd edge of a rectangle, having a common vertex with 1st edge.

Return value:
- perimeter (int / float): Perimeter of a rectangle with edges of length a and b.

Usage example:
- perimeter(4.5, 1) - function returns 11

# Version history
### 2024-09-2024
Current version.
- Updated [Documentation](../docs/Documentation.md) with full version history.

### 2024-09-19 (7452861)
- Added function descriptions to every file.
- Added [Documentation](../docs/Documentation.md).
- Deleted [file](../docs/README.md) with algorithmic realizations, its content is now merged into [Documentation](../docs/Documentation.md).

### 2024-09-17 (c845b8e)
- Added [triangle.py](../triangle.py) with functions area(a, h) and perimeter(a, b, c).
- Fixed minor bug in function perimeter(a, b) in [rectangle.py](../rectangle.py).

### 2024-09-17 (de7e882)
- Added [rectangle.py](../rectangle.py) with functions area(a, b) and perimeter(a, b).

### 2024-09-05 (2a81fb1)
Non-feature release.
- Creation of a new branch for future development.

### 2021-04-19 (86edb1c)
- Updated [README.md](../docs/README.md) with info for user agreement.

### 2021-04-19 (438b89a)
- Added [User agreement](../user_agreement.txt).

### 2021-03-04 (6adb962) (from 8ba9aeb)
- Added [README.md](../docs/README.md) with documentation for circle, square and rectangle

### 2021-03-30 (3049431) (from d078c8d)
- Added [rectangle.py](../rectangle.py) with functions area(a, b) and perimeter(a, b)

### 2021-03-30 (b5b0fae)
- Updated [README.md](../docs/README.md) with documentation for calculate.py library.

### 2021-03-30 (d76db2a)
- Added [calculate.py](../calculate.py) with functions for circle and square

### 2021-03-26 (51c40eb)
- Updated [README.md](../docs/README.md) with documentation for triangle.

### 2021-03-26 (d080c78)
- Added [triangle.py](../triangle.py) with functions area(a, b, c) and perimeter(a, b, c)

### 2021-03-04 (d078c8d)
- Added [folder](../docs/) for documentation, including [file](../docs/README.md) with formulas for functions.

### 2021-03-04 (8ba9aeb)
Initial release.
- Added [circle.py](../circle.py) with functions area(r) and perimeter(r).
- Added [square.py](../square.py) with functions area(a) and perimeter(a).
