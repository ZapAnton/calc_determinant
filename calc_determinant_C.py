import ctypes
from ctypes import POINTER

def calc_determinant(matrix):
    detlib = ctypes.CDLL('./calc_determinant.so')

    matrix_size = len(matrix)

    c_matrix = (POINTER(ctypes.c_int) * matrix_size)()

    for i in range(matrix_size):
        c_matrix[i] = (ctypes.c_int * matrix_size)()

        for j in range(matrix_size):
            c_matrix[i][j] = matrix[i][j]

    detlib.calc_determinant(matrix_size, c_matrix)

    return 0
