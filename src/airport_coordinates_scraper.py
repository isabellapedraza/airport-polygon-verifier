from bs4 import BeautifulSoup
import requests

def parse_coordinates(url):
    try:
        response = requests.get(url, timeout=10) # Make sure we timeout if we don't hear a quick response
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        coord_string = soup.find("h3", text="Location").next_sibling.contents[3].get_text()
        
        coordinates = coord_string.split("W")[-1].split("(")[0].split(",")
       
        return [float(coordinate) for coordinate in coordinates]

    except requests.exceptions.RequestException as e:
        print("Error:", e)

def scrape_coordinates(identifiers):
    """
    Returns the latitude and longitude of an airport given it's FAA identifier.

    Parameters:
        identifiers (list[str]): A list of FAA identifiers

    Returns:
        coordinates (dict{str: list[float, float]}): A dict where keys are an airport's FAA
                                                    identifier and values are tuples of an
                                                    airport's (latitude, longitude) coordinates
    """

    url = "http://www.airnav.com/airport/"  # from specification
    coordinates = {}

    for airport in identifiers:
        coordinates[airport] = parse_coordinates(url + airport)

    return coordinates


coords = scrape_coordinates(["BOS"])
print(coords)

# links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))
