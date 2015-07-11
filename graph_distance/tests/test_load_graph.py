import pytest
import graph_distance.paths_setup as ps
import graph_distance.load_graph as lg


@pytest.fixture
def graph():
    graph = lg.Graph(ps.DEFAULT_INPUT_FILE)
    return graph


def test_load_file(graph):
    routes = graph._load_file()
    assert routes == ["AB5", "BC4", "CD8", "DC8", "DE6", "AD5", "CE2", "EB3", "AE7"]


def test_split_single_route(graph):
    route = "AB8"
    assert ("A", "B", 8) == graph._split_single_route(route)


def test_split_routes_input(graph):
    routes_input = ["AB5", "BC4", "CD8"]
    routes = graph._split_routes_input(routes_input)
    assert routes == [("A", "B", 5), ("B", "C", 4), ("C", "D", 8)]

def test_load_graph_as_dict(graph):
    routes = [("A", "B", 5), ("A", "D", 5), ("A", "E", 7),
              ("B", "C", 4),
              ("C", "D", 8), ("C", "E", 2),
              ("D", "C", 8), ("D", "E", 6),
              ("E", "B", 3)]
    graph_as_dict = graph._load_graph_as_dict(routes)
    assert graph_as_dict == { "A": { "B": 5, "D": 5, "E": 7},
                              "B": { "C": 4},
                              "C": { "D": 8, "E": 2},
                              "D": { "C": 8, "E": 6},
                              "E": { "B": 3}}