import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from networkx import dfs_edges


def check_if_graph_is_traversable_from_node(node_num, graph_size):
    dfs_route_generator = dfs_edges(G, source=node_num)
    routes_from_node = list(dfs_route_generator)
    print(routes_from_node)  #print example route to traverse all graph
    return True if len(routes_from_node) == graph_size-1 else False

def check_which_node_is_good_CL(G):
    graph_size = G.number_of_nodes()
    print(graph_size)
    values = {}
    for node in range(graph_size):
        res = check_if_graph_is_traversable_from_node(node, graph_size)
        values[node] = res
    return values

#Adjacency matix
if __name__ == '__main__':
    print("-------------------------------------")
    print("To input graph modify input.txt file.")
    print("-------------------------------------")

    # adjacency_matrix = np.loadtxt('input.txt', dtype=int)
    adjacency_matrix = np.loadtxt('input_assignment1.txt', dtype=int)

    print("Graph:")
    print(adjacency_matrix)

    G = nx.DiGraph()
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[1])):
            if adjacency_matrix[i][j] == 1:
                G.add_edge(i, j)

    nx.draw(G, with_labels = True)
    plt.show()

    print("-------------------------------------")
    print("Task 1.1")
    print("Please input number of node to check if it's good to be first node to traverse all the nodes")
    print("Nodes range: <0: {}> (integer value)".format(len(adjacency_matrix)-1))
    node_num = int(input("Enter number  "))

    # for k in kosaraju_strongly_connected_components(G, source=None):
        # print(k)

    # for k in dfs_edges(G, source=3):
        # print(k)

    res = check_if_graph_is_traversable_from_node(node_num, len(adjacency_matrix))
    print("All graph can be traversed from node {}: {}".format(node_num, res))

    p = check_which_node_is_good_CL(G)
    print(p)