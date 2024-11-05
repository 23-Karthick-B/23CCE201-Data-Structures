import networkx as nx
import matplotlib.pyplot as plt

def plot_graph(graph, V, title="Graph"):
    G = nx.Graph()
    for i in range(V):
        for j in range(i + 1, V):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.show()

def kruskal(graph, V):
    G = nx.Graph()
    for i in range(V):
        G.add_node(i)
    for i in range(V):
        for j in range(i + 1, V):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])

    mst = nx.minimum_spanning_tree(G, algorithm="kruskal")

    # Plot the MST
    pos = nx.spring_layout(mst)
    nx.draw(mst, pos, with_labels=True, node_color='orange', node_size=1500, font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(mst, 'weight')
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels)
    plt.title("Minimum Spanning Tree using Kruskal's Algorithm")
    plt.show()

V = int(input("Enter the number of vertices (V): "))
graph = [[0 for _ in range(V)] for _ in range(V)]
print("Enter the adjacency matrix values one by one:")
for i in range(V):
    for j in range(V):
        graph[i][j] = int(input(f"Enter weight for edge from {i} to {j} (0 if no edge): "))

plot_graph(graph, V, title="Original Graph")

kruskal(graph, V)
