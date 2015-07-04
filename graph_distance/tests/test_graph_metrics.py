import graph_distance.paths_setup as ps
import graph_distance.load_graph as lg
import graph_distance.graph_metrics as gm
import pytest

@pytest.fixture
def graph():
    DG = lg.create_graph(ps.DEFAULT_INPUT_FILE)
    return DG

def test_distance_A_B_C(graph):
    distance = gm.distance_A_B_C(graph)
    assert distance == 9

