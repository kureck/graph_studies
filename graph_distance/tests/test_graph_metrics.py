from graph_distance.paths_setup import DEFAULT_INPUT_FILE
import graph_distance.graph_metrics as gm
import pytest


@pytest.fixture
def graph_metrics():
    return gm.GraphMetrics(DEFAULT_INPUT_FILE)


def test_get_route(graph_metrics):
    route = graph_metrics._get_route("A-B-C")
    assert route == ["A", "B", "C"]


def test_distance_A_B_C(graph_metrics):
    distance = graph_metrics.path_distance("A-B-C")
    assert distance == 9


def test_distance_A_D(graph_metrics):
    distance = graph_metrics.path_distance("A-D")
    assert distance == 5


def test_distance_A_D_C(graph_metrics):
    distance = graph_metrics.path_distance("A-D-C")
    assert distance == 13


def test_distance_A_E_B_C_D(graph_metrics):
    distance = graph_metrics.path_distance("A-E-B-C-D")
    assert distance == 22


def test_distance_A_E_D(graph_metrics):
    distance = graph_metrics.path_distance("A-E-D")
    assert distance == "NO SUCH ROUTE"


def test_trips_C_to_C_3_stops(graph_metrics):
    stops = graph_metrics.trips_with_max_stops("C", "C", 3, [])
    assert stops == 2


def test_trips_A_to_C_4_stops(graph_metrics):
    stops = graph_metrics.trips_with_exact_stops("A", "C", 4, [])
    assert stops == 3


def test_dijktra(graph_metrics):
    shortest = graph_metrics.dijkstra("C", "B")
    assert shortest == 5


def test_shortest_path_A_C(graph_metrics):
    shortest = graph_metrics.shortest_path("A", "C")
    assert shortest == 9


def test_shortest_path_B_B(graph_metrics):
    shortest = graph_metrics.shortest_path("B", "B")
    assert shortest == 9


def test_shortest_path_C_C(graph_metrics):
    shortest = graph_metrics.shortest_path("C", "C")
    assert shortest == 9


def test_different_routes_C_C_30(graph_metrics):
    different = graph_metrics.num_routes("C", "C", 30)
    assert different == 7
