import networkx as nx
import graph_distance.paths_setup as ps
import graph_distance.load_graph as lg

# The distance of the route A-B-C
def distance_A_B_C(graph):
    AB = graph.get_edge_data("A", "B")['weight']
    BC = graph.get_edge_data("B", "C")['weight']
    return AB + BC