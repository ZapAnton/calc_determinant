#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double calc_determinant(int, int**);

double calc_determinant_through_decomposition(int, int**);

double calc_minor_determinant(int**, int, int, int);

double calc_determinant(int matrix_size, int** matrix) {
	switch (matrix_size) {
		case 0:
			return 0;
		case 1:
			return matrix[0][0];
		case 2:
			return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
		case 3:
			return matrix[0][0] * matrix[1][1] * matrix[2][2] + 
				matrix[2][0] * matrix[0][1] * matrix[1][2] +
				matrix[1][0] * matrix[2][1] * matrix[0][2] -
				matrix[0][0] * matrix[2][1] * matrix[1][2] - 
				matrix[2][0] * matrix[1][1] * matrix[0][2] - 
				matrix[1][0] * matrix[0][1] * matrix[2][2];
		default:
			return calc_determinant_through_decomposition(matrix_size, matrix);
	}

	return 0.0;
}

double calc_minor_determinant(int** matrix, int minor_size, int m_i, int m_j) {
	int** minor = malloc(minor_size * sizeof(int*));

	for (int i = 0; i < minor_size; ++i) {
		minor[i] = malloc(minor_size * sizeof(int));
	}

	int k = 0;

	for (int i = 0; i < minor_size + 1; ++i) {
		if (i == m_i) {
			continue;
		}

		int m = 0;

		for (int j = 0; j < minor_size + 1; ++j) {
			if (j == m_j) {
				continue;
			}

			minor[k][m] = matrix[i][j];

			m++;
		}

		k++;
	}

	double minor_determinant = calc_determinant(minor_size, minor);

	for (int i = 0; i < minor_size; ++i) {
		free(minor[i]);
	}
	
	free(minor);

	return minor_determinant;
}

double calc_determinant_through_decomposition(int matrix_size, int** matrix) {
	double determinant = 0.0;

	for (int i = 0; i < matrix_size; ++i) {
		double minor_determinant = calc_minor_determinant(matrix, matrix_size - 1, 0, i);

		int	first_row_element = matrix[0][i];

		determinant += pow(-1.0, i) * first_row_element * minor_determinant;
	}

	return determinant;
}
