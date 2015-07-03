import networkx


def load_graph_from_file():
    pass


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
    decoupled = list(single_route)
    decoupled[-1] = int(decoupled[-1])
    return tuple(decoupled)


def split_routes_input(raw_routes):
    return [split_single_route(x) for x in raw_routes]
