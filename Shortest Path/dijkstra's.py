import math
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, src, V):
    dist = [math.inf] * V  # Initialize distances to infinity
    dist[src] = 0  # Distance to the source is 0
    spt_set = [False] * V 
    prev = [None] * V  

    for _ in range(V):
        mini = math.inf
        u = -1
        for v in range(V):
            if dist[v] < mini and not spt_set[v]:
                mini = dist[v]
                u = v

        if u == -1:  # All reachable nodes are processed
            break

        spt_set[u] = True  

        for v in range(V):
            if graph[u][v] and not spt_set[v] and dist[u] != math.inf and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                prev[v] = u  # Update the previous node 

    return dist, prev

def spath(prev, target):
    path = []
    while target is not None:
        path.insert(0, target)
        target = prev[target]
    return path

def visualize_graph(graph, V):
    G = nx.DiGraph()  # Create a directed graph

    # Add edges to the graph
    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0:  
                G.add_edge(i, j, weight=graph[i][j])

    edge_labels = {(i, j): graph[i][j] for i in range(V) for j in range(V) if graph[i][j] != 0}

    pos = nx.spring_layout(G)  # Layout for visualization

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Original Graph")
    plt.show()

def visualize_graph_highlight(graph, V, src, dist, prev):
    G = nx.DiGraph()  # Create a directed graph

    # Add edges to the graph with weights
    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0:  
                G.add_edge(i, j, weight=graph[i][j])

    edge_labels = {(i, j): graph[i][j] for i in range(V) for j in range(V) if graph[i][j] != 0}

    pos = nx.spring_layout(G)  # Layout for visualization

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    for i in range(V):
        if dist[i] != math.inf and i != src:
            path = spath(prev, i)
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
            nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="orange")

            print(f"Shortest path from vertex {src} to vertex {i}: Cost = {dist[i]}, Path = {path}")
        elif i != src:
            print(f"No path exists from vertex {src} to vertex {i}")
 
    # Show plot
    plt.title(f"Shortest Paths from Vertex {src}")
    plt.show()

# User input for the graph in matrix form (one by one)
m = int(input("Enter the number of vertices (m): "))
graph = [[0 for _ in range(m)] for _ in range(m)]  
print("Input adjacency matrix with 0 indicating no edge:")

for i in range(m):
    for j in range(m):
        try:
            graph[i][j] = int(input(f"Enter value for edge from {i} to {j} (0 for no edge): "))
            if graph[i][j] < 0:
                raise ValueError("Weight should be non-negative.")
        except ValueError as e:
            print(e)
            graph[i][j] = 0  # Default to 0 if invalid input

visualize_graph(graph, m)

while True:
    src_input = input("Enter the source vertex (or type 'stop' to exit): ")
    if src_input.lower() == 'stop':
        break

    try:
        src = int(src_input)
        if 0 <= src < m:
            dist, prev = dijkstra(graph, src, m)
            visualize_graph_highlight(graph, m, src, dist, prev)
        else:
            print("Invalid source vertex. Please enter a valid vertex between 0 and", m-1)
    except ValueError:
        print("Invalid input. Please enter a valid vertex number or 'stop' to exit.")  
