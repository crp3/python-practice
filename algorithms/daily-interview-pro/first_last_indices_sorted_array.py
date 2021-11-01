def first_last_indices(array, target):
  first = bs_first_index(array, target)
  last = bs_last_index(array, target)
  return [first, last]


def bs_first_index(array, target):
  i, j = 0, len(array)-1
  while i <= j:
    mid = (i + j)// 2

    if array[mid] == target and array[mid+1] >= target and array[mid-1] < target:
      return mid

    if array[mid] < target:
      i, j = mid+1, j

    if array[mid] > target or (mid-1 >= 0 and array[mid-1] == target):
      i, j = i, mid-1 

  return -1

def bs_last_index(array, target):
  i, j = 0, len(array)-1
  while i <= j:
    mid = (i + j)// 2

    if array[mid] == target and array[mid+1] > target and array[mid-1] <= target:
      return mid

    if array[mid] < target or (mid+1 < len(array) and array[mid+1] == target):
      i, j = mid+1, j

    if array[mid] > target:
      i, j = i, mid-1 

  return -1

if __name__ == '__main__':
  assert first_last_indices([1, 3, 3, 5, 7, 8, 9, 9, 9, 15], 9) == [6, 8]
  assert first_last_indices([100, 150, 150, 153], 150) == [1, 2]
  assert first_last_indices([1, 2, 3, 4, 5, 6, 10], 9) == [-1, -1]
