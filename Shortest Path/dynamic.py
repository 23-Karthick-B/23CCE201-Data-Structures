import math
import networkx as nx
import matplotlib.pyplot as plt
import heapq

def dynamic(graph, V, destination):
    # Initialize shortest path cost array
    shortest_paths = [math.inf] * V
    shortest_paths[destination] = 0  # Cost to reach destination from itself is 0

    queue = [(0, destination)]  
    
    while queue:
        current_cost, u = heapq.heappop(queue)
        
        if current_cost > shortest_paths[u]:
            continue
        
        # Update shortest paths for neighbors of u
        for v in range(V):
            weight = graph[v][u] 
            if weight != math.inf and shortest_paths[v] > current_cost + weight:
                shortest_paths[v] = current_cost + weight
                heapq.heappush(queue, (shortest_paths[v], v))

    return shortest_paths

def plot_graph(graph, V):
    G = nx.DiGraph()  # Create a directed graph

    # Add edges to the graph with weights
    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0 and graph[i][j] != math.inf:  
                G.add_edge(i, j, weight=graph[i][j])

    edge_labels = {(i, j): graph[i][j] for i in range(V) for j in range(V) if graph[i][j] != 0 and graph[i][j] != math.inf}

    pos = nx.spring_layout(G)  # Layout for visualization

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Original Graph")
    plt.show()

def plot_shortest_paths(graph, V, destination, shortest_paths):
    G = nx.DiGraph()  # Create a directed graph

    # Add edges to the graph with weights
    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0 and graph[i][j] != math.inf:  
                G.add_edge(i, j, weight=graph[i][j])

    edge_labels = {(i, j): graph[i][j] for i in range(V) for j in range(V) if graph[i][j] != 0 and graph[i][j] != math.inf}

    pos = nx.spring_layout(G)  # Layout for visualization

    # Draw the full graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    for i in range(V):
        if shortest_paths[i] != math.inf and i != destination:
            for j in range(V):
                if graph[i][j] != 0 and graph[i][j] != math.inf and shortest_paths[j] + graph[i][j] == shortest_paths[i]:
                    nx.draw_networkx_edges(G, pos, edgelist=[(i, j)], edge_color='red', width=2)

    plt.title("Shortest Paths to Vertex " + str(destination))
    plt.show()

# Input section
m = int(input("Enter the number of vertices (m): "))

graph = [[math.inf for _ in range(m)] for _ in range(m)]  # Initialize an m x m matrix with inf
print("Enter the adjacency matrix values (type '0' for non-reachable edges):")
for i in range(m):
    for j in range(m):
        value = int(input(f"Enter value for edge from {i} to {j}: "))
        graph[i][j] = value if value != 0 else math.inf  # Set non-reachable edges as 'inf'

plot_graph(graph, m)

while True:
    dest_input = input("Enter the destination vertex (or type 'stop' to exit): ")
    if dest_input.lower() == 'stop':
        break

    try:
        destination = int(dest_input)
        if 0 <= destination < m:
            shortest_paths = dynamic(graph, m, destination)

            print("\nShortest paths to destination vertex", destination)
            for i in range(m):
                if shortest_paths[i] != math.inf:
                    print(f"From vertex {i} to vertex {destination}: Cost = {shortest_paths[i]}")
                else:
                    print(f"From vertex {i} to vertex {destination}: No path exists")

            plot_shortest_paths(graph, m, destination, shortest_paths)
        else:
            print("Invalid destination vertex. Please enter a valid vertex between 0 and", m-1)
    except ValueError:
        print("Invalid input. Please enter a valid vertex number or 'stop' to exit.")
