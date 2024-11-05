import math
import networkx as nx
import matplotlib.pyplot as plt

def floyd(graph, V):
    # Initialize distance matrix
    dist = [[math.inf] * V for _ in range(V)]

    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0:
                dist[i][j] = graph[i][j]
            if i == j:
                dist[i][j] = 0  # Distance to self is 0

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def visualize_graph(graph, V):
    G = nx.DiGraph()  # Create a directed graph

    # Add edges to the graph with weights
    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])

    pos = nx.spring_layout(G)  # Layout for visualization

    edge_labels = {(i, j): graph[i][j] for i in range(V) for j in range(V) if graph[i][j] != 0}
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Original Graph")
    plt.show()

def shortest_paths(graph, V, dist):
    G = nx.DiGraph()  # Create a directed graph

    # Add edges to the graph with weights
    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])

    pos = nx.spring_layout(G)  # Layout for visualization
    edge_labels = {(i, j): graph[i][j] for i in range(V) for j in range(V) if graph[i][j] != 0}

    # Draw the graph with all edges
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    for start in range(V):
        for end in range(V):
            if start != end and dist[start][end] != math.inf:
                path = get_path(graph, start, end, dist)
                if path:
                    path_edges = list(zip(path, path[1:]))
                    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
                    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="orange")

    plt.title("Shortest Paths (Floyd-Warshall)")
    plt.show()

def get_path(graph, start, end, dist):
    path = []
    current = start
    path.append(current)
    while current != end:
        for next_node in range(len(graph)):
            if graph[current][next_node] != 0 and dist[start][end] == dist[start][current] + graph[current][next_node]:
                current = next_node
                path.append(current)
                break
        else:
            return None  
    return path

# User input for the graph in adjacency matrix form 
m = int(input("Enter the number of vertices (m): "))

graph = []
print("Enter the adjacency matrix values row by row (type 'inf' for non-reachable nodes):")
for i in range(m):
    row = input(f"Enter row {i} (space-separated values): ").split()
    graph_row = []
    for value in row:
        if value.lower() == 'inf':
            graph_row.append(0)  
        else:
            graph_row.append(int(value))
    graph.append(graph_row)

dist = floyd(graph, m)

print("\nShortest path distance matrix:")
for row in dist:
    print(row)

visualize_graph(graph, m)

shortest_paths(graph, m, dist)
