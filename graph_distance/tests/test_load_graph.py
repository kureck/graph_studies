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
