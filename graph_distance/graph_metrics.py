"""
    graph_distance.graph_metrics
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Creates a structure to calculate graph metrics.
    This class is used to calculate the following metrics:
        path_distance: distance from between vertices
        trips_with_max_stops: at maximum stops between vertices
        trips_with_exact_stops: at exact stops between vertices
        shortest_path: shortest path between vertices

"""

from graph_distance.load_graph import Graph


class GraphMetrics:

    def __init__(self, file_name):
        """ Initialize with a graph structure which will be evaluated

            :param file_name: a text file with the routes and its weights
        """
        self._graph = Graph(file_name).graph()

    def _get_route(self, route):
        """ Gets the route vertices in the "A-D-C-E" format
            and splits it into a list of route vertices.

            :param route: String with a sequence of vertices separated
                          by a '-' character

            :returns: a list of vertices
        """
        return route.split("-")

    def path_distance(self, route):
        """ Evaluates the distance between vertices passing
            by specific vertices.

            :param route: String with a sequence of vertices separated
                          by a '-' character

            :returns: a int representing the total distance between
                      vertices. If the vertice is unreachable a
                      "NO SUCH ROUTE" message is presented
        """
        nodes = self._get_route(route)
        total_distance = 0
        for i, node in enumerate(nodes[:-1]):
            distance = self._graph.get(nodes[i]).get(nodes[i+1])
            if distance is None:
                return "NO SUCH ROUTE"
            total_distance += distance
        return total_distance

    # The number of trips starting at C and
    # ending at C with a maximum of 3 stops
    def trips_with_max_stops(self, start, objective, max_stops, n_stops_cycle, stops=0):
        """ Evaluates stops between vertices limited by a maximum value

            :param start: A string vertice where the trip starts
            :param objective: A string vertice where the trip ends
            :param max_stops: A int value representing the upper bound of stops
                              made between start and objective
            :param n_stops_cycle: A list with all numbers of stops
                                  between start and end.
            :param stops: a counter to control how many stops has been made so far

            :returns: a sum of all stops that is less than or equal to max_stops
        """
        # counts the stops so far
        stops += 1

        # for each node adjacent to start, check if it's the objective
        # if it is, adds to a list the value of stops made until then
        # else, accesses recursively the adjacent nodes.
        # In the end, returns the sum of all stops that are more
        # than or equal to max_stops
        for node in self._graph[start]:

            if node == objective:
                n_stops_cycle.append(stops)
            else:
                self.trips_with_max_stops(node, objective, max_stops, n_stops_cycle, stops)
        return sum([1 for x in n_stops_cycle if x <= max_stops])

    # Has one problem here!
    # If the keys are not sorted the behavior is inconstant.
    # The answer depends on the order which the neighbor is visited.
    # For example:
    #   when the node D is visited the two possibles neighbors are C and E
    #   if we first visit C it marks C as visited then the recursion goes to
    #   the next D neighbor (E). When it gets there,
    #   C somehow has been marked as visited
    #   then the recursion stops when the next C is found.
    #   This doesn't happen when the order is the opposite.
    def trips_with_exact_stops(self, start, objective, max_stops, n_stops_cycle, stops=0, visited=False):
        """ Evaluates stops between vertices limited with an exact value

            :param start: A string vertice where the trip starts
            :param objective: A string vertice where the trip ends
            :param max_stops: A int value representing the exact value of stops
                              made between start and objective that must be achieved
            :param n_stops_cycle: A list with all numbers of stops 
                                  between start and end.
            :param stops: a counter to control how many stops has been made so far
            :param visited: a boolean flag to control if the end 
                            vertice has already been visited

            :returns: a sum of all stops that is equal to max_stops
        """
        # counts the stops made so far
        stops += 1

        # for each node adjacent to start, check if it's the objective
        # and if has already been visited
        # if it is, adds to a list the value of stops made until then
        # else, checks if current is equals to objective
        # if it is, mark it as visited
        # then accesses recursively the adjacent nodes.
        # In the end, returns the sum of all stops that are exactly
        # equal to max_stops
        for node in sorted(self._graph[start]):
            if node == objective and visited is True:
                n_stops_cycle.append(stops)
            else:
                if node == objective:
                    visited = True
                self.trips_with_exact_stops(node, objective, max_stops, n_stops_cycle, stops, visited)
        return sum([1 for x in n_stops_cycle if x == (max_stops + 1)])

    def dijkstra(self, start, objective):
        """ Implementation of Dijkstra Algorithm to find
            the shortest path between vertices
            Reference: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

            :param start: A string with initial vertice
            :param objective: A string with the objective vertice

            :returns: a int representing the minimum distance value
                      between vertices start and objective
        """
        # sets a variable as infinity
        inf = float('inf')
        # initialize the distances with infinity values for each node
        distances = {key: inf for key in self._graph.keys()}
        # each parent is set as None
        parent = {key: None for key in self._graph.keys()}
        # nodes are set to infinity. This structure is used as a queue
        # to control the minimum distance
        nodes = {key: inf for key in self._graph.keys()}

        # then initializes the start node with 0
        distances[start] = 0
        nodes[start] = 0

        # while node is not empty
        while nodes:
            # gets de smallest distance on node
            smallest, nodes = self._get_smallest(nodes)

            # checks if this node is unreachable
            if smallest is None or distances[smallest] == inf:
                break

            # The variable alt is the length of the path from the start node
            # to the neighbor node. If this path is shorter than the current
            # shortest path, that current path is replaced with this alt path.
            for neighbor in self._graph[smallest]:
                alt = distances[smallest] + self._graph[smallest][neighbor]
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    parent[neighbor] = smallest
                    nodes[neighbor] = alt

        return distances.get(objective, 0)

    def _get_smallest(self, nodes):
        """ Gets the smallest value from a route dictionary
            representing the possible next step from
            the current vertice

            :param nodes: a dictionary representing a vertice neighbor
                          and its weight

            :returns: the smallest neighbor value
                      and remaining neighbors dictionary
        """
        # gets the minimum value from node dictionary
        # removes it, then returns the smallest and the node dictionary
        smallest = min(nodes, key=nodes.get)
        del nodes[smallest]
        return smallest, nodes

    # The length of the shortest route (in terms of distance to travel) from A to C
    def shortest_path(self, origin, objective):
        """ Gets the shortest path between two vertices

            :param origin: A string with the origin vertice
            :param objective: A string with the objective vertice

            :returns: the value with the minimum distance value
                      between origin and objective
        """
        # if the origin is equal to objective the Dijsktra algortithm returns
        # a value of 0 because it considers the distance to itself 0.
        # To overcome this, the problem was split in two:
        #   - from start to next shortest path neighbr
        #   - then from this smallest neighbor to the objective
        if origin == objective:
            shortest_paths = { x: self.dijkstra(x, objective) for x in self._graph[objective].keys()}
            subsequent_shortest_path = min(shortest_paths, key=shortest_paths.get)
            min_value = min(shortest_paths.values())
            shortest_path_from = self.dijkstra(origin, subsequent_shortest_path)
            return sum([min_value, shortest_path_from])
        return self.dijkstra(origin, objective)

    def num_routes(self, start, objective, distance):
        """ Gets the number of routes made between vertices start
            and objective with a maximum distance

            :param start: A string with the origin vertice
            :param objective: A string with the objective vertice

            :returns: a number of routes with maximum distance
        """
        # gets all routes from start node to all nodes with maximum distance
        all_routes = self._different_routes_from_node_max_distance(start, distance)
        num_routes = 0

        # checks if the route starts with the start node
        # and ends with the objective node
        for route in all_routes:
            if route.startswith(start) and route.endswith(objective):
                num_routes += 1
        return num_routes

    def _join_paths(self, paths):
        """ Concatenates a list of strings

            :param paths: a list of a list of strings

            :returns: a list with joined strings
        """
        return ["".join(x) for x in paths]

    # The number of different routes from C to C with a distance of less than 30
    def _different_routes_from_node_max_distance(self, start, max_distance, curr_dist=0, path=[]):
        """ Evaluates the number of routes between two vertices limited 
            by an upper bound value

            :param start: A string vertice where the trip starts
            :param objective: A string vertice where the trip ends
            :param max_distance: A int value representing the maximum distance
                                 between start and objective that must be achieved
            :param curr_dist: a counter to control the distance made so far
            :param path: a list of all paths with maximum distance (max_distance)

            :returns: a list of all paths with maximum distance (max_distance)
        """
        # all nodes visited so far
        path = path + [start]

        # if the distance so far is more than the maximum distance
        # then it removes this node from the path and returns all
        # this route
        if curr_dist > max_distance:
            path.pop()
            return [path]

        paths = []

        # for each node adjacent to start
        # gets the distance from the start to it
        # then calls the method recursively to check all paths
        for node in self._graph[start]:
            distance = self._graph.get(start).get(node)
            new_paths = self._different_routes_from_node_max_distance(node, max_distance, curr_dist + distance, path)

            # adds all paths found so far that is 
            for new_path in new_paths:
                paths.append(new_path)
        return self._join_paths(paths)


if __name__ == "__main__":
    from graph_distance.paths_setup import DEFAULT_INPUT_FILE
    graph = {"A": {"B": 5, "D": 5, "E": 7},
             "B": {"C": 4},
             "C": {"D": 8, "E": 2},
             "D": {"C": 8, "E": 6},
             "E": {"B": 3}}

    paths = GraphMetrics(DEFAULT_INPUT_FILE)._different_routes_C_C_30("C", "C", 30)
    print(paths)
    print("End")
