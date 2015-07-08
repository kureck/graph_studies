import graph_distance.paths_setup as ps
import graph_distance.load_graph as lg


def test_load_file():
    routes = lg.load_file(ps.DEFAULT_INPUT_FILE)
    assert routes == ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]


def test_split_single_route():
    route = "AB8"
    assert ("A", "B", 8) == lg.split_single_route(route)


def test_split_routes_input():
    routes_input = ["AB5", "BC4", "CD8"]
    routes = lg.split_routes_input(routes_input)
    assert routes == [("A", "B", 5), ("B", "C", 4), ("C", "D", 8)]

def test_load_graph_as_dict():
    routes = [("A", "B", 5), ("A", "D", 5), ("A", "E", 7),
              ("B", "C", 4),
              ("C", "D", 8), ("C", "E", 2),
              ("D", "C", 8), ("D", "E", 6),
              ("E", "B", 3)]
    graph_as_dict = lg.load_graph_as_dict(routes)
    assert graph_as_dict == { "A": { "B": 5, "D": 5, "E": 7},
                              "B": { "C": 4},
                              "C": { "D": 8, "E": 2},
                              "D": { "C": 8, "E": 6},
                              "E": { "B": 3}}