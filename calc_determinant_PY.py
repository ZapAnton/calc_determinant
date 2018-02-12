def calc_determinant(matrix):
    matrix_size = len(matrix)

    if matrix_size == 1:
        return matrix[0]
    elif matrix_size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif matrix_size == 3:
        return   matrix[0][0] * matrix[1][1] * matrix[2][2] \
               + matrix[0][1] * matrix[1][2] * matrix[2][0] \
               + matrix[0][2] * matrix[1][0] * matrix[2][1] \
               - matrix[0][0] * matrix[1][2] * matrix[2][1] \
               - matrix[0][1] * matrix[1][0] * matrix[2][2] \
               - matrix[0][2] * matrix[1][1] * matrix[2][0]

    return 0
