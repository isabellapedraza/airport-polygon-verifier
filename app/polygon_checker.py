# Inspiration from https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule


def point_in_polygon(x, y, polygon_coords):
    """
    Checks if a point x, y is within, coincides with a vertex, or lies on the edge of 
    a polygon defined by a list of coordinates using the even odd rule algorithm.

    Parameters:
        x (float): The horizontal position of the point.
        y (float): The vertical position of the point.
        polygon_coords list(list[float]): A list of lists of coordinates defining the polygon.

    Returns:
        bool: True if the point is inside the polygon, coincides with a vertex,
            or lies on the edge of a polygon, False otherwise.
    """

    odd_nodes = False
    on_boundary = False
    num_vertices = len(polygon_coords)

    j = num_vertices - 1

    for i in range(num_vertices):
        xi, yi = polygon_coords[i]
        xj, yj = polygon_coords[j]

        # Checks if the point is within the range of the edge made by two polygon points
        if (yi < y and yj >= y) or (yj < y and yi >= y) and (xi <= x or xj <= x):
            # Checks if the ray from x,y is in the path of the polygon
            if xi + (y - yi) / (yj - yi) * (xj - xi) < x:
                odd_nodes = not odd_nodes

            # Checks if the point is on an edge or vertex of the polygon
            if xi + (y - yi) / (yj - yi) * (xj - xi) == x:
                return True  # The point is on the edge

        j = i

    return on_boundary or odd_nodes


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
