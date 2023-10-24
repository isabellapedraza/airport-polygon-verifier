# Inspiration from https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule

def point_in_polygon(latitude, longitude, polygon_coords):
    """
    Checks if a set of latitude, longitude coordinates is within,
    coincides with a corner, or lies on the edge of a polygon defined
    by a list of latitude, longitude coordinates using the even odd rule algorithm.

    Parameters:
        latitude (float): The latitude of the point.
        longitude (float): The longitude of the point.
        polygon_coords list(list[float]): A list of lists of latitude, longitude 
            coordinates defining the polygon.

    Returns:
        bool: True if the point is inside the polygon, coincides with a corner, 
            or lies on the edge of a polygon, False otherwise.
    """

    crossing_count = 0
    on_boundary = False

    for i in range(len(polygon_coords) - 1):
        x1, y1 = polygon_coords[i]
        x2, y2 = polygon_coords[i + 1]  # The next coordinate

        # Check if the point coincides with a corner
        if latitude == x1 and longitude == y1:
            on_boundary = True
            break

        # Check if the point lies on the edge of the polygon
        if (
            (y1 < longitude and y2 >= longitude) or (y2 < longitude and y1 >= longitude)
        ) and x1 + (longitude - y1) / (y2 - y1) * (x2 - x1) == latitude:
            on_boundary = True
            break

        # Check if the path crosses the edge of the polygon
        if (y1 < longitude and y2 >= longitude) or (y2 < longitude and y1 >= longitude):
            if x1 + (longitude - y1) / (y2 - y1) * (x2 - x1) > latitude:
                crossing_count += 1

    # Determine if the point is inside the polygon
    return on_boundary or crossing_count % 2 == 1


def in_polygon(airport_coords, polygon_coords):
    """
    Check if a list of airport coordinates are inside a polygon defined by a list of coordinates.

    Parameters:
        airport_coords list(list[float]): A list of lists of latitude, longitude coordinates
            representing airport locations.
        polygon_coords list(list[float]): A list of lists of latitude, longitude coordinates
            defining the polygon.

    Returns:
        list[bool]: A list of boolean values indicating whether each airport coordinate
            is inside the polygon.
    """

    output = []

    for airport_coord in airport_coords:
        latitude, longitude = airport_coord
        is_inside = point_in_polygon(latitude, longitude, polygon_coords)
        output.append(is_inside)

    return output
