import networkx as nx
import random

class RandomWalker:
    def __init__(self, graph, amort_prob=0.85):
        self.graph = graph
        self.amort_prob = amort_prob
        self.node_list = list(self.graph.nodes())
        self.visited = set()

    def random_walk_with_restart(self, start_node=None):
        teleport = False

        if start_node is None:
            start_node = random.choice(self.node_list)

        current_node = start_node
        pagerank = {node: 1/len(list(self.node_list))
                    for node in self.node_list}

        while True:
            input_key = input(
                "Press 1 to make a teleport or Enter to continue: ")

            if input_key == '1':
                teleport = True
                print("Teleporting...")

            print(self.visited)
            neighbors = list(self.graph.neighbors(current_node))

            self.visited.add(current_node)

            if teleport or len(neighbors) == 0 or random.random() < 0.1:
                pagerank[current_node] += (
                    1 - self.amort_prob) / len(self.node_list)
                current_node = random.choice(self.node_list)
            else:
                pagerank[current_node] = (1 - self.amort_prob) / len(self.node_list) + self.amort_prob * sum(
                    pagerank[neighbor] / len(neighbors) for neighbor in neighbors)

                next_node = random.choice(neighbors)
                if current_node == next_node:
                    next_node = random.choice(self.node_list)
                current_node = next_node

            if len(self.visited) == len(self.node_list):
                break
            total_pagerank = sum(pagerank.values())
            pagerank = {node: pr / total_pagerank for node,
                        pr in pagerank.items()}

            for node, pr in sorted(pagerank.items(), key=lambda x: x[1], reverse=True):
                print(f"Node {node}: PageRank = {pr}")
            print()
        return pagerank


# Ejemplo de uso:
if __name__ == "__main__":
    # Crear un grafo de ejemplo
    G = nx.DiGraph()
    G.add_edges_from([("A", "C"), ("A", "N"), ("A", "K"),
                      ("C", "D"), ("C", "K"),
                      ("E", "E"),
                      ("F", "M"), ("F", "G"),
                      ("G", "I"), ("G", "J"),
                      ("H", "G"), ("H", "F"),
                      ("I", "H"), ("I", "E"),
                      ("J", "I"), ("J", "L"),
                      ("K", "F"),
                      ("M", "B"), ("M", "A"),
                      ("N", "O"), ("O", "N")])

    # Crear un objeto RandomWalker
    walker = RandomWalker(G)

    # Realizar un "random walk with restart" desde el nodo 1 durante 1000 pasos

    num_steps = 20
    pagerank = walker.random_walk_with_restart("A")

    print("Final PageRank:")
    for node, pr in sorted(pagerank.items(), key=lambda x: x[1], reverse=True):
        print(f"Node {node}: PageRank = {pr}")
