# The distance of the route A-B-C
def distance_A_B_C(graph, path=None):
    A = graph.get("A")
    AB = A.get("B")
    B = graph.get("B")
    BC = B.get("C")
    return AB + BC


# The distance of the route A-D
def distance_A_D(graph):
    AD = graph.get("A").get("D")
    return AD


# The distance of the route A-D-C
def distance_A_D_C(graph):
    A = graph.get("A")
    AD = A.get("D")
    D = graph.get("D")
    DC = D.get("C")
    return AD + DC


# The distance of the route A-E-B-C-D
def distance_A_E_B_C_D(graph):
    AE = graph.get("A").get("E")
    EB = graph.get("E").get("B")
    BC = graph.get("B").get("C")
    CD = graph.get("C").get("D")
    return sum([AE, EB, BC, CD])


# The distance of the route A-E-D
def distance_A_E_D(graph):
    AE = graph.get("A").get("E")
    ED = graph.get("E").get("D")
    has_path = None if None in [AE, ED] else sum([AE, ED])
    return has_path


# The number of trips starting at C and ending at C with a maximum of 3 stops
def trips_C_to_C_3_stops(graph, node):
    count = 0
    node = graph.get(node)
    for path in node:
        trips_C_to_C_3_stops(graph.get(path), path)

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
    return 0


# The length of the shortest route (in terms of distance to travel) from B to B
def shortest_path_B_B(graph):
    min_dist = float('inf')

    return min_dist


# The number of different routes from C to C with a distance of less than 30
def different_routes_C_C_30(graph):
    pass

if __name__ == "__main__":
    graph = { "A": { "B": 5, "D": 5, "E": 7},
              "B": { "C": 4},
              "C": { "D": 8, "E": 2},
              "D": { "C": 8, "E": 6},
              "E": { "B": 3}}
    import ipdb; ipdb.set_trace()
    print(trips_C_to_C_3_stops(graph, "C"))