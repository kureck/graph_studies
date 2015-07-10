def get_route(route):
    return route.split("-")


def path_distance(graph, route):
    nodes = get_route(route)
    total_distance = 0
    for i, node in enumerate(nodes[:-1]):
        distance = graph.get(nodes[i]).get(nodes[i+1])
        if distance is None:
            return distance
        total_distance += distance
    return total_distance


# The distance of the route A-B-C
def distance_A_B_C(graph):
    return path_distance(graph, "A-B-C")


# The distance of the route A-D
def distance_A_D(graph):
    return path_distance(graph, "A-D")


# The distance of the route A-D-C
def distance_A_D_C(graph):
    return path_distance(graph, "A-D-C")


# The distance of the route A-E-B-C-D
def distance_A_E_B_C_D(graph):
    return path_distance(graph, "A-E-B-C-D")


# The distance of the route A-E-D
def distance_A_E_D(graph):
    return path_distance(graph, "A-E-D")


def get_neighbor(graph, source):
    return graph.get(source)


# The number of trips starting at C and ending at C with a maximum of 3 stops
def trips_C_to_C_3_stops(graph, start, objective, n_stops_cycle, stops=0):

        stops += 1
        for node in graph[start]:

            if node == objective:
                n_stops_cycle.append(stops)
            else:
                trips_C_to_C_3_stops(graph, node, objective, n_stops_cycle, stops)
        return sum([1 for x in n_stops_cycle if x <= 3])


# Has some problem here!
# If the keys are not sorted the behavior is inconstant.
# The answer depends on the order which the neighbor is visited.
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


def get_smallest(nodes):
    smallest = min(nodes, key=nodes.get)
    del nodes[smallest]
    return smallest, nodes


def dijkstra(graph, start, objective):
    inf = float('inf')
    distances = {key: inf for key in graph.keys()}
    parent = {key: None for key in graph.keys()}
    nodes = {key: inf for key in graph.keys()}

    distances[start] = 0
    nodes[start] = 0

    while nodes:
        smallest, nodes = get_smallest(nodes)

        if smallest is None or distances[smallest] == inf:
            break

        for neighbor in graph[smallest]:
            alt = distances[smallest] + graph[smallest][neighbor]
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                parent[neighbor] = smallest
                nodes[neighbor] = alt
    return {"distances": distances}


# The length of the shortest route (in terms of distance to travel) from A to C
def shortest_path_A_C(graph):
    return dijkstra(graph, "A", "C")['distances']['C']


# The length of the shortest route (in terms of distance to travel) from B to B
def shortest_path_B_B(graph):
    BC = dijkstra(graph, "B", "C")["distances"]["C"]
    CB = dijkstra(graph, "C", "B")["distances"]["B"]

    return (BC + CB)


# The number of different routes from C to C with a distance of less than 30
def different_routes_C_C_30(graph, start, objective, max_distance, curr_dist=0, path=[]):
    path = path + [start]

    if curr_dist > max_distance:
        path.pop()
        return [path]

    paths = []

    for node in graph[start]:
        distance = graph.get(start).get(node)
        new_paths = different_routes_C_C_30(graph, node, objective, max_distance, curr_dist + distance, path)
        for new_path in new_paths:
            paths.append(new_path)
    return paths


def num_routes(graph, start, objective, distance):
    all_routes = different_routes_C_C_30(graph, start, objective, distance)
    num_routes = 0

    for route in all_routes:
        if route[0] == start and route[-1] == objective:
            num_routes += 1
    return num_routes


if __name__ == "__main__":
    graph = {"A": {"B": 5, "D": 5, "E": 7},
             "B": {"C": 4},
             "C": {"D": 8, "E": 2},
             "D": {"C": 8, "E": 6},
             "E": {"B": 3}}

    #import ipdb; ipdb.set_trace()
    # print(num_routes(graph, "C", "C", 30))
    paths = different_routes_C_C_30(graph, "C", "C", 30)
    print("End")
