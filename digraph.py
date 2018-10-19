import networkx as nx
import matplotlib.pyplot as plt

DG = nx.DiGraph()

# Your graph param (1-st node, 2-nd node, weight).
DG.add_weighted_edges_from([(1, 2, 6), (1, 3, 96), (1, 4, 5), (2, 3, 5), (2, 4, 3), (2, 5, 7),
                            (2, 6, 6), (3, 6, 4), (4, 5, 4), (4, 7, 5), (5, 8, 3), (5, 7, 3),
                            (5, 9, 6), (5, 10, 3), (6, 5, 8), (6, 8, 6), (7, 10, 6), (8, 11, 6),
                            (8, 13, 5), (9, 8, 4), (9, 10, 4), (9, 11, 5), (10, 12, 6), (10, 11, 3),
                            (11, 12, 6), (11, 14, 7), (12, 14, 8), (13, 11, 3), (13, 14, 4)])


def find_shortest_way(DG):
    return nx.shortest_path(G=DG, source=1, target=14, weight=True)


def get_weight_sum(DG):
    shortest_way = find_shortest_way(DG)

    edges_list = []

    n_c = 0
    while n_c < len(shortest_way) - 1:
        edges_list.append((shortest_way[n_c], shortest_way[n_c + 1]))
        print(edges_list)
        n_c += 1

    weight_list = []
    for d in DG.edges.data(True):
        for e in edges_list:
            if e[0] == d[0] and e[1] == d[1]:
                weight_list.append(d[2]['weight'])

    return sum(weight_list)


def draw_graph(DG):

    edge_labels = dict([((u, v,), d['weight']) for u, v, d in DG.edges.data(True)])
    pos=nx.spring_layout(DG)

    nx.draw_networkx_edge_labels(DG, pos, edge_labels=edge_labels)
    nx.draw(DG,pos=pos, with_labels=True, edge_labels=edge_labels)

    plt.draw()
    plt.show()


print(find_shortest_way(DG))

draw_graph(DG)
get_weight_sum(DG)
