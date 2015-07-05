import networkx as nx


def load_graph_from_file(routes):
    """ Transform a list of tuples into a graph object

        :param routes: list of routes tuples
        :returns: a networkx graph object
    """
    DG = nx.DiGraph()
    DG.add_weighted_edges_from(routes)
    return DG


def load_file(file_name):
    """ Loads input file

        :param file_name: file name where are the input values
        :returns: a list of unformatted routes in the form ["AB8", "CD5"]
    """
    with open(file_name, 'r') as f:
        for line in f:
            raw_routes = [x.strip() for x in line.split(',')]

    return raw_routes


def split_single_route(single_route):
    """ Splits single route string from the "AB8" form into a ("A", "B", 8) tuple

        :param single_route: route string in the form "AB8"
        :returns: a tuple in the form ("A", "B", 8)
    """
    decoupled = list(single_route)
    decoupled[-1] = int(decoupled[-1])
    return tuple(decoupled)


def split_routes_input(raw_routes):
    """ Creates a list of splited routes

        :param raw_routes: list of raw_routes in the form ["AB8", "CD5"]
        :returns: a list of tuples in the form [("A", "B", 8)]
    """
    return [split_single_route(x) for x in raw_routes]


def plot_graph(graph):
    import matplotlib.pyplot as plt
    nx.draw_random(graph)
    plt.savefig("/tmp/temp_graph.png")


def create_graph(file_name):
    DG = load_graph_from_file(split_routes_input(load_file(file_name)))
    return DG


def run(file_name):
    DG = load_graph_from_file(split_routes_input(load_file(file_name)))
    t = DG.get_edge_data("A", "E")
    import ipdb; ipdb.set_trace()
    plot_graph(DG)


if __name__ == "__main__":
    import paths_setup as ph
    run(ph.DEFAULT_INPUT_FILE)


