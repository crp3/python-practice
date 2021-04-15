def zero_matrix(matrix):
    zero_initial_column = False
    zero_initial_row = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
                if i == 0: zero_initial_row = True
                if j == 0: zero_initial_column = True
                    
    for index, row in enumerate(matrix):
        if row[0] == 0 and index != 0:
            clear_row(matrix, index)

    for index, column in enumerate(matrix[0]):
        if column == 0 and index != 0:
            clear_column(matrix, index)

    if zero_initial_column:
        clear_column(matrix, 0)

    if zero_initial_row:
        clear_row(matrix, 0)

    return matrix


def clear_row(matrix, index):
    for i in range(len(matrix[index])):
        matrix[index][i] = 0

def clear_column(matrix, index):
    for i in range(len(matrix)):
        matrix[i][index] = 0

def create_matrix():
    return [
        [1,2,3,0,5],
        [5,4,3,2,1],
        [1,1,0,1,1],
        [4,3,2,1,5],
        [3,2,1,5,4]
    ]


if __name__ == '__main__':
    matrix = create_matrix()
    zero_matrix(matrix)
    for row in matrix:
        print(row)
    
    expected_result = [
        [0,0,0,0,0],
        [5,4,0,0,1],
        [0,0,0,0,0],
        [4,3,0,0,5],
        [3,2,0,0,4]
    ]

    assert matrix == expected_result
    