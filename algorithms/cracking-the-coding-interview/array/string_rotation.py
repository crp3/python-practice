def string_rotation(string1, string2):
  return string2 in (string1 + string1)

if __name__ == '__main__':
  assert string_rotation('erbottlewat', 'waterbottle')
  assert string_rotation('', '')
  assert string_rotation('behumblesitdown', 'sitdownbehumble')
