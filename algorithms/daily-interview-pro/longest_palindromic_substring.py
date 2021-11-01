def longest_palindromic_substring(string):
  best_i, best_j = 0, 0

  for index in range(len(string)-1):
    i, j = expandCenter(string, index, index)
    k, l = expandCenter(string, index, index+1)
    
    if l - k > j - i:
      if l - k > best_j - best_i:
        best_i, best_j = k, l
    else:
      if j - i > best_j - best_i:
        best_i, best_j = i, j
  
  return string[best_i:best_j+1]
  

def expandCenter(string, i, j):
  k, l = i, j
  while k >= 0 and l < len(string) and string[k] == string[l]:
    k -= 1
    l += 1

  return k+1, l-1 


if __name__ == '__main__':
  assert longest_palindromic_substring('million') == 'illi'
  assert longest_palindromic_substring('tracecars') == 'racecar'
  assert longest_palindromic_substring('banana') == 'anana'
