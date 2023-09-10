import numpy as np
import networkx as nx

class PowerIterator:


    def __init__(self, graph):
        self.graph = graph
        self.teleport = False
        self.nodes = list(self.graph.nodes)
        self.num_nodes = len(self.nodes)
        self.adjacency_matrix = nx.adjacency_matrix(self.graph, nodelist=self.nodes).toarray()
        self.adjacency_matrix = self.adjacency_matrix / self.adjacency_matrix.sum(axis=0, keepdims=True)  # Normalize rows
        # Inicializar el vector de PageRank de manera uniforme
        self.pagerank_vector = np.ones(self.num_nodes) / self.num_nodes
        
    def calculate_pagerank(self, damping_factor):
        for node, pr in sorted(dict(zip(self.nodes, self.pagerank_vector)).items(), key=lambda x: x[1], reverse=True):
                print(f"Nodo {node}: PageRank = {pr}")
                
        new_pagerank_vector = np.dot(
            (1 - damping_factor) * np.full((self.num_nodes, self.num_nodes), 1/self.num_nodes) 
            + damping_factor * self.adjacency_matrix,
            self.pagerank_vector)
        
        #Condicion que verifica si el vector PageRank ha convergido
        if np.allclose(new_pagerank_vector, self.pagerank_vector, rtol=1e-6):
            print("You reached convergence")
        self.pagerank_vector = new_pagerank_vector


        # return 
    

