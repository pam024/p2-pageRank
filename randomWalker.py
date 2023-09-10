import networkx as nx
import random

class RandomWalker:
    def __init__(self, graph, restart_prob=0.15):
        self.graph = graph
        self.restart_prob = restart_prob

    def random_walk_with_restart(self, start_node, num_steps):
        current_node = start_node
        pagerank = {node: 0 for node in self.graph.nodes}
        pagerank[current_node] = 1  # Inicializar el PageRank en el nodo de inicio

        for _ in range(num_steps):
            neighbors = list(self.graph.neighbors(current_node))
            
            if random.random() < self.restart_prob:
                # Reiniciar al nodo de inicio con probabilidad restart_prob
                current_node = start_node
            else:
                if len(neighbors) == 0:
                    # Si el nodo actual no tiene vecinos, reiniciar al nodo de inicio
                    current_node = start_node
                else:
                    # Moverse aleatoriamente a un vecino
                    current_node = random.choice(neighbors)
                
            # Actualizar el PageRank del nodo visitado
            pagerank[current_node] += 1

        # Normalizar el PageRank
        total_visits = sum(pagerank.values())
        pagerank = {node: visits / total_visits for node, visits in pagerank.items()}

        return pagerank

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear un grafo de ejemplo
    G = nx.DiGraph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 1)])

    # Crear un objeto RandomWalker
    walker = RandomWalker(G)

    # Realizar un "random walk with restart" desde el nodo 1 durante 1000 pasos
    start_node = 1
    num_steps = 1000
    pagerank = walker.random_walk_with_restart(start_node, num_steps)

    print("PageRank resultante:")
    for node, pr in sorted(pagerank.items(), key=lambda x: x[1], reverse=True):
        print(f"Nodo {node}: PageRank = {pr}")
