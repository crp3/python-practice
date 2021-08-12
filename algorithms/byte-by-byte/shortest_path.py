sample_graph = {
    '1': {'2', '3'},
    '2': {'5'},
    '3': {},
    '4': {'1', '3'},    
    '5': {'4'}
}

def shortest_path(graph, start, target):
  visited = set(start)
  queue = list(graph[start])
  result = [start]

  while queue != []:
    current = queue.pop(0)
    result.append(current)

    visited.add(current)
    for item in graph[current]:
      if item == target:
        result.append(item)
        return result
      if item not in visited:
        queue.append(item)
    
  return False

if __name__ == '__main__':
  print(sample_graph)
  print(shortest_path(sample_graph, '2', '3'))
    
