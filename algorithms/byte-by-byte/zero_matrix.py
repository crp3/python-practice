def zero_matrix(matrix):
    zero_first_column = False
    zero_first_row = False

    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if item:
                matrix[0][j] = True
                matrix[i][0] = True
                if i == 0: zero_first_row = True
                if j == 0: zero_first_column = True
    
    for i, row in enumerate(matrix):
        if row[0] and i != 0:
            zero_row(matrix, i)
    
    for j, item in enumerate(matrix[0]):
        if item and j != 0:
            zero_column(matrix, j)

    if zero_first_column:
        zero_column(matrix, 0)
    
    if zero_first_row:
        zero_row(matrix, 0)

def zero_column(matrix, column):
    for i in range(len(matrix)):
        matrix[i][column] = True

def zero_row(matrix, row):
    for i in range(len(matrix[row])):
        matrix[row][i] = True

sample_matrix = [
    [True, False, False],
    [False, False, False],
    [False, False, False]
]

second_matrix = [
    [False, False, False],
    [False, True, False],
    [False, False, True]
]

def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == '__main__':
    zero_matrix(second_matrix)
    print_matrix(second_matrix)