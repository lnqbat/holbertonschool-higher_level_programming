#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = row[:]
        for i in range(len(new_row)):
            new_row[i] = new_row[i] ** 2
        new_matrix.append(new_row)
    return new_matrix
