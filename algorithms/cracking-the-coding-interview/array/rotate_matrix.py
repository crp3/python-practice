def rotate(matrix):
  m, n = len(matrix), len(matrix[0])
  for j in range(n//2):
    for i in range(j, n-1-j):
      a = matrix[j][i]
      b = matrix[i][n-1-j]
      c = matrix[m-1-j][n-1-i]
      d = matrix[m-1-i][j]
      matrix[j][i] = d
      matrix[i][n-1-j] = a
      matrix[m-1-j][n-1-i] = b
      matrix[m-1-i][j] = c
    
def create_matrix():
    return [
      [10, 11, 12, 13],
      [14, 15, 16, 17],
      [18, 19, 20, 21],
      [22, 23, 24, 25]
    ]

if __name__ == '__main__':
  matrix = create_matrix()
  rotate(matrix)
  for row in matrix:
    print(row)

  expected_result = [
    [22, 18, 14, 10],
    [23, 19, 15, 11],
    [24, 20, 16, 12],
    [25, 21, 17, 13]
  ]

  assert matrix == expected_result
