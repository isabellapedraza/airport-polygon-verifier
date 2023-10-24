# from polygon_checker import *
# from web_scraper import *
import json
import math


def get_keys(path):
    "Use JSON to read our API key"
    with open(path) as f:
        return json.load(f)

airports = get_keys("airports.json")

def near_airports(polygon, airports):

    output = []

    for i in range(len(airports)):
        airport = airports[i]
        airport_coords = get_coordinates([airport[0]["IATA"]])
        if in_polygon(airport_coords, polygon):
            output.append(airport_coords)
    
    return output

paths = get_keys("paths.json")

def get_airport_paths(start_airports, end_airports, all_paths):

    paths = {} #path (start, end): cost 

    for s_airport in start_airports:
        for e_airport in end_airports:
            for i in range(len(all_paths)):
                path = paths[i]
                if s_airport == path["Source"] and e_airport == path["Dest"]:
                    paths[(s_airport, e_airport)] = path["Fare"]

    return paths

def get_cheapest_path(paths, start, end):

    driving = math.dist(start, end)
    
    min_flight = min(paths)

    if driving < min_flight:
        return ("Driving", driving, start, end)

    return ("Flying", min_flight.keys(), min_flight.values())
    
            




