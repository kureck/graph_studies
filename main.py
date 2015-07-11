import argparse
import graph_distance.paths_setup as ps
from graph_distance.graph_metrics import GraphMetrics

def main():
    parser = argparse.ArgumentParser(description='Deliver products to customer. You should either load from file or a direct string from terminal.')
    parser.add_argument('-f', '--file', help="File where are the routes.", default=ps.DEFAULT_INPUT_FILE)

    args = parser.parse_args()
    file_name = args.file

    print("\n============================================================")
    print("Running the Deliver routes according to the following tests:")
    print("============================================================")
    print("1. The distance of the route A-B-C")
    print("2. The distance of the route A-D")
    print("3. The distance of the route A-D-C")
    print("4. The distance of the route A-E-B-C-D")
    print("5. The distance of the route A-E-D")
    print("6. The number of trips starting at C and ending at C with a maximum of 3 stops")
    print("7. The number of trips starting at A and ending at C with exactly 4 stops")
    print("8. The length of the shortest route (in terms of distance to travel) from A to C")
    print("9. The length of the shortest route (in terms of distance to travel) from B to B")
    print("10.The number of different routes from C to C with a distance of less than 30")

    graph_metrics = GraphMetrics(file_name)
    print("\n")
    print("Output #1: %s" % graph_metrics.path_distance("A-B-C"))
    print("Output #2: %s" % graph_metrics.path_distance("A-D"))
    print("Output #3: %s" % graph_metrics.path_distance("A-D-C"))
    print("Output #4: %s" % graph_metrics.path_distance("A-E-B-C-D"))
    print("Output #5: %s" % graph_metrics.path_distance("A-E-D"))
    print("Output #6: %s" % graph_metrics.trips_with_max_stops("C", "C", 3, []))
    print("Output #7: %s" % graph_metrics.trips_with_exact_stops("A", "C", 4, []))
    print("Output #8: %s" % graph_metrics.shortest_path("A", "C"))
    print("Output #9: %s" % graph_metrics.shortest_path("B", "B"))
    print("Output #10: %s" % graph_metrics.num_routes("C", "C", 30))

if __name__ == "__main__":
    main()