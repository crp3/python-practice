from graph import sample

def bfs(graph, start, target):
  visited = set([start])
  queue = list(graph[start])

  while queue != []:
    current = queue.pop(0)
    if current == target:
      return True

    visited.add(current)
    for item in graph[current]:
      if item not in visited:
        queue.append(item)
    
  return False

if __name__ == '__main__':
  print(sample)
  print(bfs(sample, '1', '6'))
  print(bfs(sample, '3', '10'))
  print(bfs(sample, '3', '7'))
  print(bfs(sample, '7', '3'))

