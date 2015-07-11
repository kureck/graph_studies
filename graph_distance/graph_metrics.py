from graph_distance.load_graph import Graph

class GraphMetrics:

    def __init__(self, file_name):
        self._graph = Graph(file_name).graph()


    def _get_route(self, route):
        return route.split("-")


    def path_distance(self, route):
        nodes = self._get_route(route)
        total_distance = 0
        for i, node in enumerate(nodes[:-1]):
            distance = self._graph.get(nodes[i]).get(nodes[i+1])
            if distance is None:
                return "NO SUCH ROUTE"
            total_distance += distance
        return total_distance


    # The number of trips starting at C and ending at C with a maximum of 3 stops
    def trips_C_to_C_3_stops(self, start, objective, n_stops_cycle, stops=0):

            stops += 1
            for node in self._graph[start]:

                if node == objective:
                    n_stops_cycle.append(stops)
                else:
                    self.trips_C_to_C_3_stops(node, objective, n_stops_cycle, stops)
            return sum([1 for x in n_stops_cycle if x <= 3])


    # Has one problem here!
    # If the keys are not sorted the behavior is inconstant.
    # The answer depends on the order which the neighbor is visited.
    # For example:
    #   when the node D is visited the two possibles neighbors are C and E
    #   if we first visit C it marks C as visited then the recursion goes to
    #   the next D neighbor (E). When it gets there, C somehow has been marked as visited
    #   then the recursion stops when the next C is found.
    #   This doesn't happen when the order is the opposite.
    def trips_A_to_C_4_stops(self, start, objective, n_stops_cycle, stops=0, visited=False):
            stops += 1
            for node in sorted(self._graph[start]):
                if node == objective and visited is True:
                    n_stops_cycle.append(stops)
                else:
                    if node == objective:
                        visited = True
                    self.trips_A_to_C_4_stops(node, objective, n_stops_cycle, stops, visited)
            return sum([1 for x in n_stops_cycle if x == 5])


    def _get_smallest(self, nodes):
        smallest = min(nodes, key=nodes.get)
        del nodes[smallest]
        return smallest, nodes


    def dijkstra(self, start, objective):
        inf = float('inf')
        distances = {key: inf for key in self._graph.keys()}
        parent = {key: None for key in self._graph.keys()}
        nodes = {key: inf for key in self._graph.keys()}

        distances[start] = 0
        nodes[start] = 0

        while nodes:
            smallest, nodes = self._get_smallest(nodes)

            if smallest is None or distances[smallest] == inf:
                break

            for neighbor in self._graph[smallest]:
                alt = distances[smallest] + self._graph[smallest][neighbor]
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    parent[neighbor] = smallest
                    nodes[neighbor] = alt
        return {"distances": distances}


    # The length of the shortest route (in terms of distance to travel) from A to C
    def shortest_path(self, origin, destination):
        return self.dijkstra(origin, destination)['distances'][destination]


    # The length of the shortest route (in terms of distance to travel) from B to B
    def shortest_path_B_B(self):
        BC = self.dijkstra("B", "C")["distances"]["C"]
        CB = self.dijkstra("C", "B")["distances"]["B"]

        return (BC + CB)


    def num_routes(self, start, objective, distance):
        all_routes = self._different_routes_C_C_30(start, objective, distance)
        num_routes = 0

        for route in all_routes:
            if route[0] == start and route[-1] == objective:
                num_routes += 1
        return num_routes


    # The number of different routes from C to C with a distance of less than 30
    def _different_routes_C_C_30(self, start, objective, max_distance, curr_dist=0, path=[]):
        path = path + [start]

        if curr_dist > max_distance:
            path.pop()
            return [path]

        paths = []

        for node in self._graph[start]:
            distance = self._graph.get(start).get(node)
            new_paths = self._different_routes_C_C_30(node, objective, max_distance, curr_dist + distance, path)
            for new_path in new_paths:
                paths.append(new_path)
        return paths


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
