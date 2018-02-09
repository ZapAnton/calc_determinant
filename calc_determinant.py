if __name__ == '__main__':
    try:
        matrix_size = int(input('Enter matrix size: '))

        matrix = []

        print('Enter matrix elements:\n')

        for i in range(matrix_size):
            matrix_row = []

            for j in range(matrix_size):
                matrix_element = int(input())

                matrix_row.append(matrix_element)

            matrix.append(matrix_row)

        print(matrix)
    except ValueError:
        print('You should enter integer value for matrix size!')
