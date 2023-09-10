import networkx as nx
import matplotlib.pyplot as plt
from method_iterator import PowerIterator
# from randomWalker import RandomWalker
import numpy as np

if __name__ == "__main__":
    G = nx.DiGraph()

    # nodes = ["A", "B", "C"]
    # edges_and_weights = [
    #     ("A", "C", 1/2), ("A", "B", 1/2),
    #     ("B", "C", 1)
    # ]
    

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

    print('Write 0 to continue, Write 1 to teletransport --- ')


    # power_iterator.calculate_pagerank(damping_factor=0.85)
    Flag = True
    while Flag:
        try:
            User_inp = int(input())
            if User_inp == 0:
                #sigue normal
                power_iterator.calculate_pagerank(damping_factor=1)
            elif User_inp == 1:
                #teletransporte
                power_iterator.calculate_pagerank(damping_factor=0.85)
        except:
            print("Loco OE")
            # break


    # pos = nx.spring_layout(G)  
    # nx.draw(G, pos, with_labels=True, node_size=800, node_color="skyblue",
    #         font_size=12, font_color="black", font_weight="bold")
    # plt.title("Grafo")

    # plt.figure(1)
    # plt.matshow(adyacent_matrix)
    # plt.set_cmap('Blues')
    # plt.colorbar()
    # plt.xticks(np.arange(0, len(nodes)), nodes)
    # plt.yticks(np.arange(0, len(nodes)), nodes)
    # plt.show()


    # plt.show()





    # walker = RandomWalker(G)

    # # Realizar un "random walk with restart" desde el nodo 1 durante 1000 pasos
    # start_node = 1
    # num_steps = 1000
    # pagerank = walker.random_walk_with_restart(start_node, num_steps)

    # print("PageRank resultante:")
    # for node, pr in sorted(pagerank.items(), key=lambda x: x[1], reverse=True):
    #     print(f"Nodo {node}: PageRank = {pr}")



