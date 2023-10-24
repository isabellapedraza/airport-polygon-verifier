import json
import ast
from flask import Flask
from flask import request
from shapely.geometry import Polygon
from app import polygon_checker, web_scraper

app = Flask(__name__)


def get_keys(path):
    "Use JSON to read our API key"
    with open(path) as f:
        return json.load(f)

keys = get_keys("secret.json")
api_key = keys["api_key"]


@app.route("/")
def index():
    faa_ids = request.args.get("identifiers", "")
    polygon_coords = request.args.get("polygon", "")
    if faa_ids and polygon_coords:
        airport_coords = get_coordinates(faa_ids)
        final_answer = in_polygon(airport_coords, polygon_coords)

        # Find the lat,long of the Polygon's center
        polygon_coords = ast.literal_eval(polygon_coords)
        polygon = Polygon([tuple(coord) for coord in polygon_coords])
        center = [polygon.centroid.xy[0][0], polygon.centroid.xy[1][0]]
    else:
        airport_coords = "[]"
        final_answer = "[]"
        center = [38.897840, -77.072010]
    return (
        """
        <html>
            <head>
                <title>Airport Polygon Verifier</title>
                <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
                <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
            </head>
            <body>
                <div>
                    <form action="" method="get">
                        FAA identifiers: <input type="text" name="identifiers">
                        Polygon Coordinates: <input type="text" name="polygon">
                        <input type="submit" value="Calculate">
                    </form>
                </div>
                <br>
                <div>
                    Airports: 
                """
        + str(faa_ids)
        + """
                </div>
                <br>
                <div>
                    Latitude/Longitude Coordinates for each airport, respectively:
                    <br>
                """
        + str(airport_coords)
        + """
                </div>
                <br>
                <div>
                    Is the airport in the polygon?
                    <br>
                """
        + str(final_answer)
        + """
                </div>
                <br>
                <div>
                    <h2> Polygon: </h2>
                    <div id="map" style="height: 400px;"></div>
                </div>
                
                <script>
                // Create a map centered at a specified location
                """
        + 'var map = L.map("map").setView({center}, 6); // Adjust the center and zoom level'.format(
            center=center
        )
        + """
                L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 19,
                    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
                }).addTo(map);

                // Define the polygon coordinates
                """
        + "var polygonCoords ={poly}".format(poly=polygon_coords)
        + """
                // Create a polygon and add it to the map
                L.polygon(polygonCoords, {
                    color: "red", // Set the polygon color
                    fillOpacity: 0.35, // Set the fill opacity
                }).addTo(map);
                </script>
                <br>
            </body>
        </html>
        """
    )


@app.route("/")
def get_coordinates(faa_ids):
    """Given a HTML form input, get the coordinates of each airport"""
    try:
        airports = ast.literal_eval(faa_ids)
        return web_scraper.get_coordinates(airports)
    except ValueError:
        return "Please make sure FAA IDs are inputted as a comma-separated list."


@app.route("/")
def in_polygon(airport_coords, polygon_coords):
    """Given a HTML form input, check whether the coordinates of each airport are within the polygon defined by coordinates"""
    try:
        polygon_coords = ast.literal_eval(polygon_coords)
        return polygon_checker.in_polygon(airport_coords, polygon_coords)
    except ValueError:
        return "Please make sure polygon coordinates are inputted as a comma-separated list of lists."


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
