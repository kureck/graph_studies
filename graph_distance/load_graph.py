from collections import defaultdict
from graph_distance.paths_setup import DEFAULT_GRAPH_IMAGE


class Graph:

    def __init__(self, file_name):
        self._file_name = file_name
        self._graph = self._create_dict_graph(file_name)


    def graph(self):
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

            :param file_name: file name where are the input values
            :returns: a list of unformatted routes in the form ["AB8", "CD5"]
        """
        with open(self._file_name, 'r') as f:
            for line in f:
                raw_routes = [x.strip() for x in line.split(',')]

        return raw_routes


    def _split_single_route(self, single_route):
        """ Splits single route string from the "AB8" form into a ("A", "B", 8) tuple

            :param single_route: route string in the form "AB8"
            :returns: a tuple in the form ("A", "B", 8)
        """
        decoupled = list(single_route)
        decoupled[-1] = int(decoupled[-1])
        return tuple(decoupled)


    def _split_routes_input(self, raw_routes):
        """ Creates a list of splited routes

            :param raw_routes: list of raw_routes in the form ["AB8", "CD5"]
            :returns: a list of tuples in the form [("A", "B", 8)]
        """
        return [self._split_single_route(x) for x in raw_routes]


    def _create_dict_graph(self, file_name):
        graph = self._load_graph_as_dict(self._split_routes_input(self._load_file()))
        return graph


