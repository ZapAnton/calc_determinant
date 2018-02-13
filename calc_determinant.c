#include <stdio.h>

double calc_determinant(int matrix_size, int** matrix) {
	for (int i = 0; i < matrix_size; ++i) {
		for (int j = 0; j < matrix_size; ++j) {
			printf("%d", matrix[i][j]);

			if (j == matrix_size - 1) {
				printf("\n");
			} else {
				printf(" ");
			}
		}
	}
}
