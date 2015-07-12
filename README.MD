# How to use it

## Requirements

1. Python 2.7 or Python 3.4
2. git
3. virtualenv
4. Linux ou Mac

### Installation

Go to a directory of your choice to create a virtual environment using virtualenv for Python 2.7 or pyvenv for Python 3.4

Python 2.7:

- virtualenv graph_distance

Python 3.4:

- pyvenv-3.4 graph_distance

If you have some pip trouble try this:

- pyvenv-3.4 --without-pip graph_distance
- cd graph_distance
- source bin/activate
- wget https://pypi.python.org/packages/source/s/setuptools/setuptools-3.4.4.tar.gz
- tar -vzxf setuptools-3.4.4.tar.gz
- cd setuptools-3.4.4
- python setup.py install
- cd ..
- wget https://pypi.python.org/packages/source/p/pip/pip-1.5.6.tar.gz
- tar -vzxf pip-1.5.6.tar.gz
- cd pip-1.5.6
- python setup.py install
- cd ..
- deactivate
- source ./myvenv/bin/activate

Else, continue to download and run the code:

- cd graph_distance
- source bin/activate
- git clone https://github.com/kureck/graph_studies
- cd graph_studies
- pip install -e .
- py.test graph_distance/tests # to run tests
- python main.py


# Deliver products to customer

The purpose of this problem is to help the suppliers with information about the routes to delivery product.
In particular, you will compute the distance along a certain route, the number of different routes between two places, and the shortest route between two places.

## Input
A directed graph where a node represents a place and an edge represents a route between two places.
The weighting of the edge represents the distance between the two places.
A given route will never appear more than once, and for a given route, the starting and ending place will not be the same place.

## Output
For test input 1 through 5, if no such route exists, output 'NO SUCH ROUTE'.
Otherwise, follow the route as given; do not make any extra stops!
For example, the first problem means to start at city A, then travel directly to city B (a distance of 5), then directly to city C (a distance of 4).

## Input explanation
1. The distance of the route A-B-C.
2. The distance of the route A-D.
3. The distance of the route A-D-C.
4. The distance of the route A-E-B-C-D.
5. The distance of the route A-E-D.
6. The number of trips starting at C and ending at C with a maximum of 3 stops.
    * In the sample data below, there are two such trips: C-D-C (2 stops). and C-E-B-C (3 stops).
7. The number of trips starting at A and ending at C with exactly 4 stops.
    * In the sample data below, there are three such trips: A to C (via B,C,D); A to C (via D,C,D); and A to C (via D,E,B).
8. The length of the shortest route (in terms of distance to travel) from A to C.
9. The length of the shortest route (in terms of distance to travel) from B to B.
10.The number of different routes from C to C with a distance of less than 30.
    *In the sample data, the trips are: CEBC, CEBCEBC, CEBCEBCEBC, CDEBC, CDC, CEBCDC, CDCEBC.
    ['CEBC', 'CEBCEBC', 'CEBCEBCEBC', 'CDEBC', 'CDC']

### Test Input
For the test input, the places are named using the first few letters of the alphabet from A to E.
A route between two places (A to B) with a distance of 5 is represented as AB5.

Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7

### Expected Output

* Output #1: 9
* Output #2: 5
* Output #3: 13
* Output #4: 22
* Output #5: NO SUCH ROUTE
* Output #6: 2
* Output #7: 3
* Output #8: 9
* Output #9: 9
* Output #10: 7

