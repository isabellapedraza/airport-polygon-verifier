import re
from bs4 import BeautifulSoup
import requests

def scrape_coordinates(url):
    '''
    Retrieve the latitude and longitude coordinates of an airport in decimal degrees
    using https://www.airnav.com.

    Parameters:
        url (str): The URL of the web page containing airport coordinates.

    Returns:
        list[float, float]: A list containing the latitude and longitude 
                                coordinates of the airport in decimal degrees.
    
    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request, such as a timeout or a non-200 status code.
    '''
    try:
        response = requests.get(
            url, timeout=5
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Find the <td> containing the "Lat/Long:" label using a regular expression
        coord_td = soup.find('td', string=re.compile(r'Lat/Long:'))

        # Get the latitude and longitude from the next <td>
        coord_string = coord_td.find_next('td').contents[4]

        # Split the coordinate string by comma and create a list with the coordinates as floats
        return [float(coordinate) for coordinate in coord_string.split(",")]

    except requests.exceptions.RequestException as e:
        print("Error:", e)


def get_coordinates(faa_ids):
    """
    Returns the respective latitude and longitude coordinates of airports given FAA identifiers
    using the website https://www.airnav.com.

    Parameters:
        faa_ids (list[str]): A list of FAA identifiers

    Returns:
        coordinates (list[list[float, float]]}): A list where list[i] is the [latitude, longitude]
                                                    of the airport faa_ids[i]
    """
    coordinates = []

    for airport_code in faa_ids:
        url = f"https://www.airnav.com/airport/{airport_code}" #URL is from specification
        coordinates.append(scrape_coordinates(url))

    return coordinates
