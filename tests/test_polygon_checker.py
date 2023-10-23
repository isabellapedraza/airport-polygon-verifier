import pytest
import requests
from app import polygon_checker

'''
Testing strategy for in_polygon = in_polygon(airport_coords, polygon_coords)

parition on len(airport_coords):                0, 1+

partition on len(polygon_coords):               0, 1, 2, 3+

parition on airport_coords:                     inside_polygon, on polygon edge, outside polygon

parition on len(in_polygon):                    0, 1+

parition on values in in_polygon:               all True, all False, mixed True and False

'''
