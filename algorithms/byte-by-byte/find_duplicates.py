def find_duplicates(array):
  seen = set()
  solution = set()
  for item in array:
    if item in seen:
      solution.add(item)
    seen.add(item)
  return list(solution)

if __name__ == '__main__':
  assert find_duplicates([1, 2, 3]) == []
  assert find_duplicates([1, 2, 2]) == [2]
  assert find_duplicates([3, 3, 3]) == [3]
  assert find_duplicates([2, 1, 2, 1]) == [1, 2]
