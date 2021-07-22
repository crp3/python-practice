def is_shifted(a, b):
  if len(a) != len(b):
    return False
  
  # search for the first character of a in b

  first_character = a[0]
  saved_index = -1
  for index, char in enumerate(b):
    if char == first_character:
      saved_index = index

  # if not found, return false

  if saved_index == -1:
    return False
  
  # now check if every character is equal from each index

  len_b = len(b)
  for index, a_char in enumerate(a):
    b_char = b[(saved_index+index)%len_b]
    if a_char != b_char:
      return False
    
  return True


if __name__ == '__main__':
  assert is_shifted('abcd', 'dabc')
  assert is_shifted('abcde', 'deabc')
  assert is_shifted('abcdef', 'defabc')
  assert not is_shifted('abcd', 'cabd')
  assert not is_shifted('abcd', 'abc')
  assert not is_shifted('abcd', 'debc')
