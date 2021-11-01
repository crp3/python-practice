def validate_parentheses(string):
  counterparts = {
    '}': '{',
    ')': '(',
    ']': '['
  }

  stack = []

  for char in string:
    if char in counterparts:
      if stack.pop() != counterparts[char]:
        return False
    else:
      stack.append(char)
  
  return True

if __name__ == '__main__':
  assert validate_parentheses('((()))')
  assert validate_parentheses('[()]{}')
  assert not validate_parentheses('({[)]')
