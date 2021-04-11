from graph import sample

def dfs(graph, target, start='1', visited = None):
    if visited is None:
        visited = set()
    visited.add(start)

    if start == target:
        return True
    else:
        result = False
        for i in graph[start] - visited:
            result = result or dfs(graph, target, i, visited) 
        return result

if __name__ == '__main__':
    print(dfs(sample, '1000', '5'))