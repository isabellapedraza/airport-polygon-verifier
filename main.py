from flask import Flask
from flask import request
# from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    FAA_identifiers = request.args.get("identifiers", "")
    polygon_coords = request.args.get("polygon", "")
    if FAA_identifiers and polygon_coords:
        final_answer = get_coordinates(FAA_identifiers)
    else:
        final_answer = ""
    return (
        """<form action="" method="get">
                FAA_identifiers: <input type="text" name="identifiers">
                Polygon: <input type="text" name="polygon">
                <input type="submit" value="Convert to Fahrenheit">
            </form>"""
        + "In Polygon?: "
        + final_answer
    )

@app.route("/")
def get_coordinates(FAA_identifiers):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

@app.route("/")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)