class TSTNode: 
  def __init__(self, value=None, left=None, bottom=None, right=None):
    self.value = value
    self.left = left
    self.bottom = bottom
    self.right = right

  def print_tree(self):
    current = self
    while current:
      print(current.value)
      if current.left:
        print('left')
        current.left.print_tree()
      if current.right:
        print('right')
        current.right.print_tree()
      if current.bottom:
        current = current.bottom
      else:
        return

  def insert(self, word):
    index = 0
    current = self
    while index < len(word):
      character = word[index]
      if character == current.value:
        index += 1
        if not current.bottom:
          current.bottom = from_word(word[index:])
          index = len(word)
        current = current.bottom
      elif character < current.value:
        if not current.left:
          current.left = from_word(word[index:])
          index = len(word)
        current = current.left
      elif character > current.value:
        if not current.right:
          current.right = from_word(word[index:])
          index = len(word)
        current = current.right

  def search(self, word):
    index = 0
    character = word[index]
    current = self
    while current:
      if character == current.value:
        index += 1
        if index == len(word):
          return True
        character = word[index]
        current = current.bottom
      elif character < current.value:
        current = current.left
      elif character > current.value:
        current = current.right
    return False
    
def from_word(word):
  tst_nodes = [TSTNode(char) for char in word] + [None]
  for index in range(len(word)):
    tst_nodes[index].bottom = tst_nodes[index+1]
  return tst_nodes[0]

def create_default_tst():
  n1 = TSTNode('c')
  n2 = TSTNode('o')
  n3 = TSTNode('d')
  n4 = TSTNode('e')
  n5 = TSTNode('b')
  n1.bottom = n2
  n2.bottom = n3
  n3.bottom = n4
  n3.left = n5
  return n1
    
if __name__ == '__main__':
  print('###### TESTING SEARCH METHOD ONLY ######')
  t = create_default_tst()
  assert t.search('code')
  assert t.search('cob')
  assert not t.search('aba')
  assert not t.search('colo')
  assert not t.search('cobo')

  print('###### TESTING SEARCH ON TREE GENERATED BY INSERT METHOD ######')

  t = from_word('code')
  t.insert('cob')
  t.insert('be')
  t.insert('ax')
  t.insert('war')
  t.insert('we')

  assert t.search('code')
  assert t.search('cob')
  assert t.search('be')
  assert t.search('ax')
  assert t.search('war')
  assert t.search('we')
  assert not t.search('rw')
  assert not t.search('axa')
  assert not t.search('waxa')

