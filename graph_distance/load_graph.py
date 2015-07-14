"""
    graph_distance.load_graph
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Creates a graph dictionary structure from file.
    The content of the file must be in a single line
    and with the following format: <node_1><node_2><weight>
        Ex.: AB5, AD8, AC4, CD5

    The only method exposable is .graph() which returns
    a dict like graph from file.

"""


from collections import defaultdict


class Graph:

    def __init__(self, file_name):
        self._file_name = file_name
        self._graph = self._create_dict_graph()

    def graph(self):
        """ Public method to access the dictionary graph.

            :returns: a dictionary graph
                      in the form { "A": { "B": 5, "D": 5, "E": 7}
        """
        return self._graph

    def _load_graph_as_dict(self, routes):
        """ Transform a list of tuples into a graph as a dictionary

            :param routes: list of routes tuples
                           in the form [("A", "B", 5), ("A", "D", 5), ("A", "E", 7)]
            :returns: a dictionary graph
                      in the form { "A": { "B": 5, "D": 5, "E": 7}
        """
        graph = defaultdict(dict)
        for route in routes:
            source = route[0]
            graph[source].update({route[1]: route[2]})

        return graph

    def _load_file(self):
        """ Loads input file

            :returns: a list of unformatted routes
                      in the ["AB8", "CD5"] format
        """
        with open(self._file_name, 'r') as f:
            for line in f:
                raw_routes = [x.strip() for x in line.split(',')]

        return raw_routes

    def _split_single_route(self, single_route):
        """ Splits single route string from the "AB8"
            format into a ("A", "B", 8) tuple format

            :param single_route: route string in the form "AB8"
            :returns: a tuple in the form ("A", "B", 8)
        """
        decoupled = list(single_route)
        decoupled[-1] = int(decoupled[-1])
        return tuple(decoupled)

    def _split_routes_input(self, raw_routes):
        """ Creates a list of splited routes

            :param raw_routes: list of raw_routes
                               in the form ["AB8", "CD5"]
            :returns: a list of tuples in the form [("A", "B", 8)]
        """
        return [self._split_single_route(x) for x in raw_routes]

    def _create_dict_graph(self):
        """ Creates a dictionary graph executing all
            the methods needed to create a graph from file

            :returns: a dictionary graph
                      in the form { "A": { "B": 5, "D": 5, "E": 7}
        """
        graph = self._load_graph_as_dict(self._split_routes_input(self._load_file()))
        return graph
