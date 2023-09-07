import numpy as np
import networkx as nx

class PowerIterator:
    def __init__(self, graph):
        self.graph = graph

    def calculate_pagerank(self, num_iterations=100, damping_factor=0.85):
        nodes = list(self.graph.nodes)
        num_nodes = len(nodes)
        adjacency_matrix = nx.adjacency_matrix(self.graph, nodelist=nodes).toarray()
        adjacency_matrix = adjacency_matrix / adjacency_matrix.sum(axis=0, keepdims=True)  # Normalize rows
        
        # Inicializar el vector de PageRank de manera uniforme
        pagerank_vector = np.ones(num_nodes) / num_nodes

        for _ in range(num_iterations):
            new_pagerank_vector = (1 - damping_factor) / num_nodes + damping_factor * np.dot(adjacency_matrix, pagerank_vector)
            if np.allclose(new_pagerank_vector, pagerank_vector, rtol=1e-6):
                break
            pagerank_vector = new_pagerank_vector

        return dict(zip(nodes, pagerank_vector))
    
    def __init__(self, graph):
        self.graph = graph

