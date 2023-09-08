import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import string

if __name__ == "__main__":
    G = nx.DiGraph()

    nodes = ["A", "B", "C", "D", "E", "F", "G",
             "H", "I", "J", "K", "L", "M", "N", "O"]
    G.add_nodes_from(nodes)

    edges_and_weights = [
        ("A", "C", 1/3), ("A", "N", 1/3), ("A", "K", 1/3),
        ("C", "D", 1/2), ("C", "K", 1/2),
        ("E", "E", 1),
        ("F", "M", 1/2), ("F", "G", 1/2),
        ("G", "I", 1/2), ("G", "J", 1/2),
        ("H", "G", 1/2), ("H", "F", 1/2),
        ("I", "H", 1/2), ("I", "E", 1/2),
        ("J", "I", 1/2), ("J", "L", 1/2),
        ("K", "F", 1),
        ("M", "B", 1/2), ("M", "A", 1/2),
        ("N", "O", 1), ("O", "N", 1)
    ]

    for init_node, end_node, weight in edges_and_weights:
        G.add_edge(init_node, end_node, weight=weight)

    adyacent_matrix = nx.attr_matrix(G, edge_attr='weight', rc_order=nodes)

    pos = nx.spring_layout(G)  # Layout para la visualización`


    plt.figure(0)
    nx.draw(G, pos, with_labels=True, node_size=800, node_color="skyblue",
        font_size=12, font_color="black", font_weight="bold")

    
    plt.figure(1)
    plt.matshow(adyacent_matrix)
    plt.set_cmap('Blues')
    plt.colorbar()
    plt.xticks(np.arange(0, len(nodes)), nodes)
    plt.yticks(np.arange(0, len(nodes)), nodes)


    plt.show()
