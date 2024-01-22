from dijkstra import dijkstra

graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'D': 9, 'E': 1},
    'C': {'A': 5, 'F': 3, 'E': 8},
    'D': {'B': 9, 'E': 5},
    'E': {'B': 1, 'C': 8, 'F': 7, 'D': 5},
    'F': {'C': 3, 'E': 7}
}

min_distances = dict()
for source in graph.keys():
    distances = dijkstra(graph, source)
    for target, distance in distances.items():
        if target == source:
            continue
        path = tuple(sorted([source, target]))
        if path not in min_distances:
            min_distances[path] = distance

print('Min distances between nodes:')
for path, distance in min_distances.items():
    print(f'{path}: {distance}')