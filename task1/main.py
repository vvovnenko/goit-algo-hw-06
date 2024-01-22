import matplotlib.pyplot as plt
import networkx as nx

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'E'],
    'D': ['B', 'E'],
    'E': ['B', 'C', 'F', 'D'],
    'F': ['C', 'E']
}

G = nx.Graph(graph)

print('Кількість вершин: ', G.number_of_nodes())
print('Кількість ребер: ', G.number_of_edges())
print('Ступені вершин:')
for node, degree in G.degree:
    print(f'\t{node}: {degree}')

plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=16, font_weight="bold")

plt.show()
