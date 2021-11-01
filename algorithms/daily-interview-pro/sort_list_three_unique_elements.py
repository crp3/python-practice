def sort_list(array):
  count_ones = 0
  count_twos = 0
  count_threes = 0

  for item in array:
    if item == 1:
      count_ones += 1
    if item == 2:
      count_twos += 1
    if item == 3:
      count_threes += 1
  
  second_index = fill_array(array, 0, count_ones, 1)
  third_index = fill_array(array, second_index, count_twos, 2)
  fill_array(array, third_index, count_threes, 3)
  
def fill_array(array, starting_index, count_elements, element):
  index = starting_index
  current_count = count_elements

  while current_count:
    array[index] = element
    index += 1
    current_count -= 1
  
  return index
    
if __name__ == '__main__':
  a = [3, 3, 2, 1, 3, 2, 1]
  sort_list(a)
  print(a)
