import ctypes
from ctypes import POINTER

def calc_determinant(matrix):
    detlib = ctypes.CDLL('./calc_determinant.so')

    detlib.restype = ctypes.c_double

    matrix_size = len(matrix)

    c_matrix = (POINTER(ctypes.c_int) * matrix_size)()

    for i in range(matrix_size):
        c_matrix[i] = (ctypes.c_int * matrix_size)()

        for j in range(matrix_size):
            c_matrix[i][j] = matrix[i][j]

    determinant = detlib.calc_determinant(matrix_size, c_matrix)

    return determinant
