import pytest
import requests
# from requests import ValueError
from app import web_scraper

'''
Testing strategy for coordinates = get_coordinates(faa_ids)

partition on len(faa_ids):                      0, 1, 1+

parition on len(coordinates):                   0, 1, 1+

'''

#Partition on len(faa_ids) = 0, len(coordinates) = 0
def test_get_coordinates_empty():
    faa_ids = []
    result = web_scraper.get_coordinates(faa_ids)
    assert isinstance(result, list), "Result should be a list"
    assert(len(faa_ids) == len(result))
    assert len(result) == 0, "Result should be empty"

#Partition on len(faa_ids) = 1, len(coordinates) = 1
def test_get_coordinates_one():
    faa_ids = ["MIA"]
    result = web_scraper.get_coordinates(faa_ids)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) != 0, "Result should not be empty"
    assert(len(faa_ids) == len(result))
    assert result == [[25.7953611, -80.2901158]]

#Partition on len(faa_ids) > 1, len(coordinates) > 1
def test_get_coordinates_many():
    faa_ids = ["58MN", "EYW", "65B", "ADK"]
    result = web_scraper.get_coordinates(faa_ids)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) != 0, "Result should not be empty"
    assert(len(faa_ids) == len(result))
    assert result == [[45.2673456, -94.0620867], [24.5561197, -81.7599558], [44.8365556,-67.0269722], [51.8835828, -176.6424822]]

'''
Testing strategy for coordinates = scrape_coordinates(faa_ids)

partition on len(url):                          0, 1+

partition on url:                               valid, invalid

parition on coordinates of airports in the 
    North-most, East-most, South-most, 
    West-most in USA:                           58MN, EYW, 65B, ADK 

'''

#Partition on len(url) = 0, url is invalid 
def test_scrape_coordinates_empty():
    url = ""
    result = web_scraper.scrape_coordinates(url)
    assert result is None

#Partition on len(url) = 1+, url is valid, coordinates are northmost
def test_scrape_coordinates_north():
    url = "https://www.airnav.com/airport/58MN"
    result = web_scraper.scrape_coordinates(url)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) == 2, "Result should contain latitude and longitude"
    assert all(isinstance(coord, float) for coord in result), "All coordinates should be floats"
    assert result == [45.2673456, -94.0620867]

#Partition on len(url) = 1+, url is valid, coordinates are eastmost
def test_scrape_coordinates_east():
    url = "https://www.airnav.com/airport/EYW"
    result = web_scraper.scrape_coordinates(url)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) == 2, "Result should contain latitude and longitude"
    assert all(isinstance(coord, float) for coord in result), "All coordinates should be floats"
    assert result == [24.5561197, -81.7599558]

#Partition on len(url) = 1+, url is valid, coordinates are southhmost
def test_scrape_coordinates_south():
    url = "https://www.airnav.com/airport/65B"
    result = web_scraper.scrape_coordinates(url)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) == 2, "Result should contain latitude and longitude"
    assert all(isinstance(coord, float) for coord in result), "All coordinates should be floats"
    assert result == [44.8365556,-67.0269722]

#Partition on len(url) = 1+, url is valid, coordinates are westmost
def test_scrape_coordinates_west():
    url = "https://www.airnav.com/airport/ADK"
    result = web_scraper.scrape_coordinates(url)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) == 2, "Result should contain latitude and longitude"
    assert all(isinstance(coord, float) for coord in result), "All coordinates should be floats"
    assert result == [51.8835828, -176.6424822]

# Run the tests
if __name__ == "__main__":
    pytest.main()
    