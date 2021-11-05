import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from networkx import dfs_edges


def check_if_graph_is_traversable_from_node(G, node_num):
    graph_size = G.number_of_nodes()
    dfs_route_generator = dfs_edges(G, source=node_num)
    routes_from_node = list(dfs_route_generator)
    # print(routes_from_node)  #print example route to traverse all graph
    return True if len(routes_from_node) == graph_size-1 else False

#list key:value list dictionary
#key = number of node
#value = True/False - if you can traverse all nodes from given node
def list_initiator_nodes_CL(G):
    graph_size = G.number_of_nodes()
    values = {}
    for node in range(graph_size):
        res = check_if_graph_is_traversable_from_node(G, node)
        values[node] = res
    return values

#program uses ajacency matix as an input
if __name__ == '__main__':
    print("-------------------------------------")
    print("To input graph modify input.txt file.")
    print("-------------------------------------")

    # load ajacency matrix from file
    adjacency_matrix = np.loadtxt('input.txt', dtype=int)

    #initate graph and fill it with values
    G = nx.DiGraph()
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[1])):
            if adjacency_matrix[i][j] == 1:
                G.add_edge(i, j)

    graph_size = G.number_of_nodes()

    #graw graph - just for visualization purposes
    nx.draw(G, with_labels = True)
    plt.savefig("graph.png", format="PNG")
    plt.show(block=False)

    print("Task 1.1")
    print("Please input number of node to check if it's good to be first node to traverse all the nodes")
    print("Nodes range: <0: {}> (integer value)".format(graph_size-1))
    node_num = int(input("Enter node number  "))

    res = check_if_graph_is_traversable_from_node(G, node_num)
    print("All graph can be traversed from node {}: {}".format(node_num, res))


    print("-------------------------------------")
    print("Task 1.2")
    print("-------------------------------------")
    p = list_initiator_nodes_CL(G)

    print("From which verticle all other grapch vericles are reachable:")
    for k, v in p.items():
        print("Node {}: {}".format(k, v))
