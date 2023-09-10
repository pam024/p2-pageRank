import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class PowerIterator:


    def __init__(self, graph):
        self.graph = graph
        self.teleport = False
        self.nodes = list(self.graph.nodes)
        self.num_nodes = len(self.nodes)
        self.adjacency_matrix = nx.adjacency_matrix(self.graph, nodelist=self.nodes).toarray()
        
        # Inicializar el vector de PageRank de manera uniforme
        self.pagerank_vector = np.ones(self.num_nodes) / self.num_nodes
        
    def calculate_pagerank(self, damping_factor):
        column_sums = self.adjacency_matrix.sum(axis=0, keepdims=True)
        column_sums[column_sums == 0] = 1  # Evita la división por cero
        normalized_adjacency_matrix = self.adjacency_matrix / column_sums

        self.walker_print()

        new_pagerank_vector = np.dot(
            (1 - damping_factor) * np.full((self.num_nodes, self.num_nodes), 1/self.num_nodes) 
            + damping_factor * normalized_adjacency_matrix,
            self.pagerank_vector)

        if np.allclose(new_pagerank_vector, self.pagerank_vector, rtol=1e-2):
            print("You reached convergence")
            return True

        self.pagerank_vector = new_pagerank_vector
        return False
    
    def walker_print(self):
        for node, pr in sorted(dict(zip(self.nodes, self.pagerank_vector)).items(), key=lambda x: x[1], reverse=True):
            print(f"Nodo {node}: PageRank = {pr}")




if __name__ == "__main__":

    G = nx.DiGraph()

    nodes = ["A", "B", "C", "D", "E", "F", "G",
             "H", "I", "J", "K", "L", "M", "N", "O"]
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

    G.add_nodes_from(nodes)

    for init_node, end_node, weight in edges_and_weights:
        G.add_edge(init_node, end_node, weight=weight)

    adyacent_matrix = nx.attr_matrix(G, edge_attr='weight', rc_order=nodes)

    power_iterator = PowerIterator(G)


    converged = False
    while converged == False:
        input_key = input("Press 1 to make a teleport or Enter to continue: ")

        if input_key == '1':
            converged = power_iterator.calculate_pagerank(damping_factor=0.85)
            print("Teleporting...")
        else:
            converged = power_iterator.calculate_pagerank(damping_factor=1)


    ##################### Graph

    pos = nx.spring_layout(G)  
    nx.draw(G, pos, with_labels=True, node_size=800, node_color="skyblue",
            font_size=12, font_color="black", font_weight="bold")
    plt.title("Grafo")

    plt.figure(1)
    plt.matshow(adyacent_matrix)
    plt.set_cmap('Blues')
    plt.colorbar()
    plt.xticks(np.arange(0, len(nodes)), nodes)
    plt.yticks(np.arange(0, len(nodes)), nodes)
    plt.show()


    plt.show()
