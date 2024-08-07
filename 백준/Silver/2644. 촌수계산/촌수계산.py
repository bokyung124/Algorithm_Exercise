from collections import defaultdict
from sys import stdin, stdout

def dfs(graph, start, end, visited, distance):
    visited[start] = True
    
    if start == end:
        return distance
    
    for neighbor in graph[start]:
        if not visited[neighbor]:
            result = dfs(graph, neighbor, end, visited, distance + 1)
            if result != -1:
                return result
    
    return -1

n = int(stdin.readline())
start, end = map(int, stdin.readline().split())
m = int(stdin.readline())
relationships = [tuple(map(int, stdin.readline().split())) for _ in range(m)]

graph = defaultdict(list)

for parent, child in relationships:
    graph[parent].append(child)
    graph[child].append(parent)

visited = [False] * (n + 1)

stdout.write(str(dfs(graph, start, end, visited, 0)))