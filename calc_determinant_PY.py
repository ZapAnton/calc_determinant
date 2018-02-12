import threading

class MinorDeterminantCalcThread(threading.Thread):

    def __init__(self, minor):
        threading.Thread.__init__(self)

        self.minor = minor

        self.determinant = 0

    def run(self):
        self.determinant = calc_determinant(self.minor)

    def get_determinant(self):
        return self.determinant

def get_minor(matrix, i, j):
    minor = []

    matrix_size = len(matrix)

    for k in range(matrix_size):
        if k == i:
            continue

        matrix_row = matrix[k]

        minor_row = [matrix_row[l] for l in range(matrix_size) if l != j]

        minor.append(minor_row)

    return minor


def calc_determinant_through_decomposition(matrix):
    determinant = 0

    first_row = matrix[0]

    minor_threads = []

    for i, row_element in enumerate(first_row):
        minor = get_minor(matrix, 0, i)

        minor_threads.append(MinorDeterminantCalcThread(minor))

        minor_threads[i].start()

    for minor_thread in minor_threads:
        minor_thread.join()

    for i, row_element in enumerate(first_row):
        determinant += (-1) ** i * row_element * minor_threads[i].get_determinant()

    return determinant

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
    elif matrix_size > 3:
        return calc_determinant_through_decomposition(matrix)

    return 0
