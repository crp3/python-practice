def matrix_product(matrix):
	return matrix_product_recursive(matrix, 0, 0)

def matrix_product_recursive(matrix, i, j):
	if i == len(matrix)-1 and j == len(matrix[0])-1:
		return matrix[i][j]
	if i == len(matrix)-1:
		return matrix[i][j] * matrix_product_recursive(matrix, i, j+1)
	if j == len(matrix[1])-1:
		return matrix[i][j] * matrix_product_recursive(matrix, i+1, j)
	
	return max(
		matrix[i][j] * matrix_product_recursive(matrix, i, j+1),
		matrix[i][j] * matrix_product_recursive(matrix, i+1, j)
	)

sample_matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

second_matrix = [
	[-1, 2, 3],
	[4, 5, -6],
	[7, 8, 9]
]

if __name__ == '__main__':
	print(matrix_product(sample_matrix))
	print(matrix_product(second_matrix))
