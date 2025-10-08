# Алгоритм Дейкстры
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

weighted_graph = {
   'A': {'B': 5, 'C': 2, 'G': 1},
   'B': {'A': 5, 'D': 4, 'E': 3, 'G': 1},
   'C': {'A': 2, 'F': 7, 'G': 1},
   'D': {'B': 4},
   'E': {'B': 3, 'F': 6, 'G': 2},
   'F': {'C': 7, 'E': 6, 'G': 2},
   'G': {'A': 1, 'B': 1, 'C': 1, 'E': 2, 'F': 2}
}

# Создаем направленный граф
G = nx.DiGraph()

# Добавляем узлы и ребра в граф
for node, edges in weighted_graph.items():
   G.add_node(node)
   for neighbor, weight in edges.items():
       G.add_edge(node, neighbor, weight=weight)


pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

def Dijkstra(graph, start_node):
    # expected result: list of nodes from the starting graph with paths and path_lengths to them from start_node
    distances = defaultdict(lambda: float('inf'))
    previous = {}
    unvisited_nodes = set(graph.keys()) 
    distances[start_node] = 0
    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances.get(node, float(
            'inf')))
        unvisited_nodes.remove(current_node)
        for neighbor, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance 
                previous[neighbor] = current_node 
    return distances, previous

def get_shortest_path(previous, source, target):
    path = [target]  # Начинаем с целевой вершины
    while path[-1] != source:  # Пока не достигнем начальной вершины
        path.append(previous[path[-1]])  # Добавляем предыдущую вершину на путь к текущей вершине
    path.reverse()  # Переворачиваем список, чтобы путь был от начальной вершины к целевой
    return path

print(Dijkstra(weighted_graph, 'A'))

distances, previous = Dijkstra(weighted_graph, 'A')
# Выводим кратчайший путь от 'D' до 'F'
path = get_shortest_path(previous, 'A', 'F')
print(f"Кратчайший путь от A до F: {path}")
# Кратчайший путь от A до F: ['A', 'G', 'F']