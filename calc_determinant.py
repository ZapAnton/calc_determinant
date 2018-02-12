import argparse

def get_matrix_from_file(filename: str):
    matrix = []

    try:
        with open(filename, 'r') as file:
           file_lines = file.readlines()

           matrix_size = int(file_lines[0])

           for i in range(1, len(file_lines)):
               matrix_row_str = file_lines[i].strip().split()

               matrix.append(list(map(int, matrix_row_str)))

    except Exception as err:
        print('Error opening matrix file:\n', err)

    return matrix

def get_matrix_from_user_input():
    matrix = []

    try:
        matrix_size = int(input('Enter matrix size: '))

        print('Enter matrix elements:\n')

        if matrix_size == 1:
            matrix.append(int(input()))

            return matrix

        for i in range(matrix_size):
            matrix_row = []

            for j in range(matrix_size):
                matrix_element = int(input())

                matrix_row.append(matrix_element)

            matrix.append(matrix_row)
    except ValueError:
        print('You must provide integer value for matrix size!')

    return matrix

def get_arguments_dict():
    parser = argparse.ArgumentParser()

    parser.add_argument('--matrix-file', help='Path to file that contains matrix elements')

    args = parser.parse_args()

    args_dict = vars(args)

    return args_dict

def check_for_C_implementation():
    return False

def calc_determinant(matrix):
    C_implementation_present = check_for_C_implementation()

    calc_determinant_function = None

    if not C_implementation_present:
        import calc_determinant_PY

        calc_determinant_function = calc_determinant_PY.calc_determinant
    else:
        import calc_determinant_C

        calc_determinant_function = calc_determinant_C.calc_determinant

    return calc_determinant_function(matrix)

if __name__ == '__main__':
    args_dict = get_arguments_dict()

    if args_dict.get('matrix_file'):
        matrix = get_matrix_from_file(args_dict['matrix_file'])
    else:
        matrix = get_matrix_from_user_input()

    determinant = calc_determinant(matrix)

    print('Determinant =', determinant)

