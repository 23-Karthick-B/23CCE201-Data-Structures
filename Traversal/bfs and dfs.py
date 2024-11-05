import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, src, V):
    visited = [False] * V
    queue = deque([src])  # Initialize the queue with the source vertex
    visited[src] = True

    print("\nBFS Traversal starting from vertex", src, ": ", end="")
    steps = []  

    while queue:
        u = queue.popleft()
        print(u, end=" ")
        steps.append(u)  

        for v in range(V):
            if graph[u][v] != 0 and not visited[v]:  
                queue.append(v)
                visited[v] = True

    print()  
    plot_graph_path(graph, V, steps, traversal_type="BFS")

def dfs(graph, src, V):
    visited = [False] * V  
    steps = []  

    def dfs_util(v):
        visited[v] = True
        print(v, end=" ")
        steps.append(v)  

        for i in range(V):
            if graph[v][i] != 0 and not visited[i]:
                dfs_util(i)

    print("\nDFS Traversal starting from vertex", src, ": ", end="")
    dfs_util(src)

    print()  
    plot_graph_path(graph, V, steps, traversal_type="DFS")

def plot_graph(graph, V):
    G = nx.DiGraph()  # Create a directed graph

    # Add edges based on the adjacency matrix
    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])  # Add edge with weight

    # Draw the original graph
    pos = nx.spring_layout(G)  # Position nodes using the spring layout algorithm
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold', arrows=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Show the plot
    plt.title("Original Graph")
    plt.show()

def plot_graph_path(graph, V, visited_nodes, traversal_type):
    G = nx.DiGraph()  # Create a directed graph

    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])  

    pos = nx.spring_layout(G)  
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold', arrows=True)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if visited_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color='orange')
        
        edges_in_path = [(visited_nodes[i], visited_nodes[i + 1]) for i in range(len(visited_nodes) - 1) if G.has_edge(visited_nodes[i], visited_nodes[i + 1])]
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=2)

    plt.title(f"{traversal_type} Traversal Visualization")
    plt.show()

# User input for the graph in matrix form (one by one)
m = int(input("Enter the number of vertices (m): "))
graph = [[0 for _ in range(m)] for _ in range(m)]  
print("Enter the adjacency matrix values one by one:")
for i in range(m):
    for j in range(m):
        graph[i][j] = int(input(f"Enter value for edge from {i} to {j}: "))

plot_graph(graph, m)

while True:
    src_input = input("Enter the source vertex for traversal (or type 'stop' to exit): ")
    if src_input.lower() == 'stop':
        break

    try:
        src = int(src_input)
        if 0 <= src < m:
            bfs(graph, src, m)
            dfs(graph, src, m)
        else:
            print("Invalid source vertex. Please enter a valid vertex between 0 and", m-1)
    except ValueError:
        print("Invalid input. Please enter a valid vertex number or 'stop' to exit.")
