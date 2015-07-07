import networkx as nx
import graph_distance.paths_setup as ps
import graph_distance.load_graph as lg


# The distance of the route A-B-C
def distance_A_B_C(graph):
    AB = graph.get_edge_data("A", "B")['weight']
    BC = graph.get_edge_data("B", "C")['weight']
    return AB + BC


# The distance of the route A-D
def distance_A_D(graph):
    AD = graph.get_edge_data("A", "D")['weight']
    return AD


# The distance of the route A-D-C
def distance_A_D_C(graph):
    AD = graph.get_edge_data("A", "D")['weight']
    DC = graph.get_edge_data("D", "C")['weight']
    return AD + DC


# The distance of the route A-E-B-C-D
def distance_A_E_B_C_D(graph):
    AE = graph.get_edge_data("A", "E")['weight']
    EB = graph.get_edge_data("E", "B")['weight']
    BC = graph.get_edge_data("B", "C")['weight']
    CD = graph.get_edge_data("C", "D")['weight']
    return sum([AE, EB, BC, CD])


# The distance of the route A-E-D
def distance_A_E_D(graph):
    if None in (graph.get_edge_data("E", "D"), graph.get_edge_data("A", "E")):
        return None
    else:
        AE = graph.get_edge_data("A", "E")['weight']
        ED = graph.get_edge_data("E", "D")['weight']
    return AE + ED


# The number of trips starting at C and ending at C with a maximum of 3 stops
def trips_C_to_C_3_stops(graph):
    count = 0
    for path in nx.all_simple_paths(graph, "C", "C"):
        if len(path) <= 4:
            count += 1
    return count

# The number of trips starting at A and ending at C with exactly 4 stops

# nx.bfs_successors(graph, origin)
# returns {'A': ['D', 'B', 'E'], 'D': ['C']}

# graph.neighbors(node)
# return ['D', 'B', 'E']

# Maybe I must use recursion here.
# 1) Get neighbours
# 2) Mount a dict with the path e number of stop and edges visited
#   * { "path": ['A', 'B', 'C', 'D', 'C'],
#        "edges_visited": [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'C')],
#        "stops": 4}
# 3) Get edge
# 4) Mount path
# 5) Count stop
# 6) Add visited edge into edges_visited

# Explore the edges
# graph.edges()
# returns [('A', 'D'), ('A', 'B'), ('A', 'E'), ('D', 'E'), ('D', 'C'), ('B', 'C'), ('E', 'B'), ('C', 'D'), ('C', 'E')]


def trips_A_to_C_4_stops(graph, source):
    pass

# The length of the shortest route (in terms of distance to travel) from A to C
def shortest_path_A_C(graph):
    return nx.shortest_path_length(graph,source="A",target="C", weight='weight')


# The length of the shortest route (in terms of distance to travel) from B to B
def shortest_path_B_B(graph):
    min_dist = float('inf')
    for path in nx.all_simple_paths(graph, "B", "B"):
        path1 = path[0:2]
        path2 = path[2:]
        path_dist1 = nx.shortest_path_length(graph,source=path1[0],target=path1[1], weight='weight')
        path_dist2 = nx.shortest_path_length(graph,source=path1[1],target=path2[-1], weight='weight')
        if (path_dist1 + path_dist2) < min_dist:
            min_dist = path_dist1 + path_dist2

    return min_dist


# The number of different routes from C to C with a distance of less than 30
def different_routes_C_C_30(graph):
    pass
