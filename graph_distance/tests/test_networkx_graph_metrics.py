import graph_distance.paths_setup as ps
import graph_distance.load_graph as lg
import graph_distance.networkx_graph_metrics as nxgm
import pytest

@pytest.fixture
def graph():
    DG = lg.create_networkx_graph(ps.DEFAULT_INPUT_FILE)
    return DG


def test_distance_A_B_C(graph):
    distance = nxgm.distance_A_B_C(graph)
    assert distance == 9


def test_distance_A_D(graph):
    distance = nxgm.distance_A_D(graph)
    assert distance == 5


def test_distance_A_D_C(graph):
    distance = nxgm.distance_A_D_C(graph)
    assert distance == 13


def test_distance_A_E_B_C_D(graph):
    distance = nxgm.distance_A_E_B_C_D(graph)
    assert distance == 22


def test_distance_A_E_D(graph):
    distance = nxgm.distance_A_E_D(graph)
    assert distance == None


def test_trips_C_to_C_3_stops(graph):
    stops = nxgm.trips_C_to_C_3_stops(graph)
    assert stops == 2


def test_trips_A_to_C_4_stops(graph):
    stops = nxgm.trips_A_to_C_4_stops(graph)
    assert stops == 3


def test_shortest_path_A_C(graph):
    shortest = nxgm.shortest_path_A_C(graph)
    assert shortest == 9


def test_shortest_path_B_B(graph):
    shortest = nxgm.shortest_path_B_B(graph)
    assert shortest == 9


def test_different_routes_C_C_30(graph):
    different = nxgm.different_routes_C_C_30(graph)
    assert different == 7