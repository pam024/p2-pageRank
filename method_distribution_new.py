import networkx as nx
import random

class Distributor:
    def __init__(self, graph, amort_prob=0.85):
        self.graph = graph
        self.amort_prob = amort_prob
        self.node_list = list(self.graph.nodes())

    def random_walk_with_restart(self, start_node=None):
        teleport = False
        position = 1
        current_node = start_node
        pagerank = {node: 1/len(list(self.node_list))
                    for node in self.node_list}

        attempts = 10000

        while attempts > 0:

            neighbors = list(self.graph.neighbors(current_node))
            pagerank[current_node] = (1 - self.amort_prob) / len(self.node_list) + self.amort_prob * sum(
                pagerank[neighbor] / len(neighbors) for neighbor in neighbors)

            next_node = self.node_list[position]

            total_pagerank = sum(pagerank.values())
            pagerank = {node: pr / total_pagerank for node,
                        pr in pagerank.items()}
            position = (position + 1) % len(list(self.node_list))
            attempts -= 1
        return pagerank



if __name__ == "__main__":

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


    walker = Distributor(G)
    pagerank = walker.random_walk_with_restart("A")

    print("Final PageRank:")
    for node, pr in sorted(pagerank.items(), key=lambda x: x[1], reverse=True):
        print(f"Node {node}: PageRank = {pr}")
