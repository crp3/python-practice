def length_longest_substring(string):
  char_last_index = {}
  max_length = left = 0

  for right in range(len(string)):
    char = string[right]
    
    if char not in char_last_index:
      max_length = max(max_length, right-left+1)
    else:
      if char_last_index[char] >= left:
        left = char_last_index[char]+1
      else:
        max_length = max(max_length, right-left+1)
    
    char_last_index[char] = right

  return max_length

if __name__ == '__main__':
  assert length_longest_substring('abcad') == 4
  assert length_longest_substring('abrkaabcdefghijjxxx') == 10        
      
