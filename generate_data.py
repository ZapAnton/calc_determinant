import sys
import random

def generate_matrix(matrix_size: int):
    try:
        with open('data/matrix_elements', 'w') as file:
            file.write(str(matrix_size) + '\n')

            for i in range(matrix_size):
                for j in range(matrix_size):
                    file.write(str(random.randint(-100, 100)))

                    if j != (matrix_size - 1):
                        file.write(' ')
                    else:
                        file.write('\n')

    except Exception as err:
        print('Error generating matrix elements:', err)

if __name__ == '__main__':
    matrix_size = 100

    if len(sys.argv) > 1:
        matrix_size = int(sys.argv[1])

    generate_matrix(matrix_size)
