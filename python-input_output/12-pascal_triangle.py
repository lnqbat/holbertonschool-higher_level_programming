#!/usr/bin/python3
"""
Defines function to return Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns list representing Pascal's triangle.
    """
    pascal_triangle = []
    if n <= 0:
        return pascal_triangle

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                left = pascal_triangle[i - 1][j - 1]
                right = pascal_triangle[i - 1][j]
                row.append(left + right)
        pascal_triangle.append(row)
    return pascal_triangle
