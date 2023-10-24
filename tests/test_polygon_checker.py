import pytest
import requests
from app import polygon_checker

'''
Testing strategy for in_polygon = in_polygon(airport_coords, polygon_coords)

parition on len(airport_coords):                0, 1+

partition on len(polygon_coords):               0, 1+

parition on len(output):                        0, 1+

parition on values in output:                   all True, all False, mixed True and False

'''

#Partition on len(airport_coords) = 0, len(polygon_coords) = 0, len(output) = 0
def test_in_polygon_empty():
    airport_coords = []
    polygon_coords = []
    is_inside = polygon_checker.in_polygon(airport_coords, polygon_coords)
    assert is_inside == []

#Partition on len(airport_coords) = 0, len(polygon_coords) = 1+, len(output) = 0
def test_in_polygon_empty_output():
    airport_coords = []
    polygon_coords = [[40, 60], [50, 60], [40, 70]]
    is_inside = polygon_checker.in_polygon(airport_coords, polygon_coords)
    assert is_inside == []

#Partition on len(airport_coords) = 1+, len(polygon_coords) >=3, len(output) = 1+, values in output = all True
def test_in_polygon_all_true():
    airport_coords = [[42.3629444, -71.0063889]]
    polygon_coords = [[42.7626733, -71.5933057], [40.813322, -71.6592591], [40.8465734, -68.9002058], [42.7868661, -68.9331825], [42.7626733, -71.5933057]]
    is_inside = polygon_checker.in_polygon(airport_coords, polygon_coords)
    assert is_inside == [True]

#Partition on len(airport_coords) = 1+, len(polygon_coords) >=3, len(output) = 1+, values in output = all False
def test_in_polygon_all_false():
    airport_coords = [[25.7953611,-80.2901158]]
    polygon_coords = [[42.7626733, -71.5933057], [40.813322, -71.6592591], [40.8465734, -68.9002058], [42.7868661, -68.9331825], [42.7626733, -71.5933057]]
    is_inside = polygon_checker.in_polygon(airport_coords, polygon_coords)
    assert is_inside == [False]

#Partition on len(airport_coords) = 1+, len(polygon_coords) >=3, len(output) = 1+, values in output = mixed True and False
def test_in_polygon_mixed():
    airport_coords = [[42.3629444, -71.0063889], [25.7953611,-80.2901158]]
    polygon_coords = [[42.7626733, -71.5933057], [40.813322, -71.6592591], [40.8465734, -68.9002058], [42.7868661, -68.9331825], [42.7626733, -71.5933057]]
    is_inside = polygon_checker.in_polygon(airport_coords, polygon_coords)
    assert is_inside == [True, False]

'''
Testing strategy for bool = point_in_polygon(x, y, polygon_coords)

partition on len(polygon_coords):               0, 1+

parition on (x, y):                             inside_polygon, on polygon edge, on polygon corner, outside polygon

parition on bool:                               True, False

'''

#Partition on len(polygon_coords) = 0, bool = False
def test_point_in_polygon_empty():
    x = 37.7849
    y = -122.3994
    polygon_coords = []
    result = polygon_checker.point_in_polygon(x, y, polygon_coords)
    assert result is False

# Partition on (latitude, longitude) inside_polygon, len(polygon_coords) = 1+, bool = True
def test_point_in_polygon_inside():
    polygon_coords = [[42.7626733, -71.5933057], [40.813322, -71.6592591], [40.8465734, -68.9002058], [42.7868661, -68.9331825], [42.7626733, -71.5933057]]
    x = 42.3629444
    y = -71.0063889
    result = polygon_checker.point_in_polygon(x, y, polygon_coords)
    assert result is True

# Partition on (latitude, longitude) on polygon edge, len(polygon_coords) = 1+, bool = True
def test_point_in_polygon_edge():
    polygon_coords = [[40.8465734, -68.9002058], [42.36294443, -72.5933057], [42.36294443, -70.6592591]]
    x = 42.3629444
    y = -71.0063889
    result = polygon_checker.point_in_polygon(x, y, polygon_coords)
    assert result is True

# Partition on (latitude, longitude) on polygon corner, len(polygon_coords) = 1+, bool = True
def test_point_in_polygon_corner():
    polygon_coords = [[42.36294443, -72.5933057], [42.36294443, -70.6592591], [40.8465734, -68.9002058]]
    x = 40.8465734
    y = -68.9002058
    result = polygon_checker.point_in_polygon(x, y, polygon_coords)
    assert result is True

# Partition on (latitude, longitude) outside polygon, len(polygon_coords) = 1+, bool = False
def test_point_in_polygon_outside():
    polygon_coords = [[42.36294443, -72.5933057], [42.36294443, -70.6592591], [40.8465734, -68.9002058]]
    x = 37.8049
    y = -122.3894
    result = polygon_checker.point_in_polygon(x, y, polygon_coords)
    assert result is False
    