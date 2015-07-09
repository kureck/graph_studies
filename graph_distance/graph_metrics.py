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


def get_neighbor(graph, source):
    return graph.get(source)


# The number of trips starting at C and ending at C with a maximum of 3 stops
def trips_C_to_C_3_stops(graph, start, objective, n_stops_cycle, stops=0):
        """
        Recursive function. Finds all paths through the specified
        graph from start node to end node. For cyclical paths, this stops
        at the end of the first cycle.
        """

        stops += 1
        for node in graph[start]:

            if node == objective:
                n_stops_cycle.append(stops)
            else:
                trips_C_to_C_3_stops(graph, node, objective, n_stops_cycle, stops)
        return sum([1 for x in n_stops_cycle if x <= 3])


# Has some problem here!
# If the keys are not sorted the behavior is inconstant. The answer depends on the order which the neighbor
# is visited. 
# For example: 
#   when the node D is visited the two possibles neighbors are C and E
#   if we first visit C it marks C as visited then the recursion goes to
#   the next D neighbor (E). When it gets there, C somehow has been marked as visited
#   then the recursion stops when the next C is found.
#   This doesn't happen when the order is the opposite.
def trips_A_to_C_4_stops(graph, start, objective, n_stops_cycle, stops=0, visited=False):
        stops += 1
        for node in sorted(graph[start]):
            if node == objective and visited is True:
                n_stops_cycle.append(stops)
            else:
                if node == objective:
                    visited = True
                trips_A_to_C_4_stops(graph, node, objective, n_stops_cycle, stops, visited)
        return sum([1 for x in n_stops_cycle if x == 5])


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
    graph = {"A": {"B": 5, "D": 5, "E": 7},
             "B": {"C": 4},
             "C": {"D": 8, "E": 2},
             "D": {"C": 8, "E": 6},
             "E": {"B": 3}}
    paths = []
    trips_A_to_C_4_stops(graph, "A", "C", paths)
    print(paths)
    print([x for x in paths if len(x) == 5])
