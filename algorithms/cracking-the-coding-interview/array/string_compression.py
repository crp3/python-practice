def string_compression(string):
  if string == '':
    return ''
  new_str = ''
  count = 0
  previous = string[0]
  for i, char in enumerate(string):
    if char != previous:
      new_str += previous
      new_str += str(count)
      count = 1
    else:
      count += 1
    previous = char
  
  new_str += previous
  new_str += str(count)

  return new_str if len(new_str) < len(string) else string

if __name__ == '__main__':
  assert string_compression('aaaaaabbbccc') == 'a6b3c3'
  assert string_compression('abc') == 'abc'
  assert string_compression('aabbcc') == 'aabbcc'
  assert string_compression('') == ''
  assert string_compression('aaaaaaaaabbbbbbbbbcccccccc') == 'a9b9c8'
