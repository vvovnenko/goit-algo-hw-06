from dfs_iterative import dfs_iterative
from bfs_iterative import bfs_iterative

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'E'],
    'D': ['B', 'E'],
    'E': ['B', 'C', 'F', 'D'],
    'F': ['C', 'E']
}


print('DFS path: ')
dfs_iterative(graph, 'A')
print('')
print('BFS path: ')
bfs_iterative(graph, 'A')