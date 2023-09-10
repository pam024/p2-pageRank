import numpy as np
import networkx as nx
import random

class RandomWalker:
    def __init__(self, graph):
        self.graph = graph
        self.amort_prob = 1
        self.visits = 0
        self.teleports = 0
        self.node_list = list(self.graph.nodes())
        self.node_visits = {node: 0 for node in self.node_list}
        self.start_node = random.choice(self.node_list)
        self.current_node = self.start_node

    def random_walk(self, teleport=False):

        # print(self.node_visits)
        # print(f"Current Node: %s, Amort Prob: %d", self.current_node, self.amort_prob)

        self.node_visits[self.current_node[0]] += 1
        self.visits += 1
        neighbors = list(self.graph.neighbors(self.current_node[0]))

        if teleport or len(neighbors) == 0:             
            self.teleports += 1
            self.current_node = random.choice(self.node_list)
        else:
            next_node = random.choices(neighbors)
            if self.current_node == next_node:
                next_node = random.choice(self.node_list)
            current_node = next_node
            self.current_node = next_node

        self.amort_prob = self.teleports/self.visits

    def walker_print(self):
        for node, pr in sorted(self.node_visits.items(), key=lambda x: x[1], reverse=True):
            print(f"Node {node}: PageRank = {pr/self.visits}")
        print()


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

    walker = RandomWalker(G)

    for _ in range(10000):
        if (random.random() < 0.15):
            teleport = True
            walker.random_walk(teleport)
        else:
            walker.random_walk()

    walker.walker_print()
    # while True:
    #     input_key = input(
    #         "Press 1 to make a teleport or Enter to continue: ")
    #     if input_key == '1':
    #         teleport = True
    #         walker.random_walk(teleport)
    #     else:
    #         walker.random_walk()
