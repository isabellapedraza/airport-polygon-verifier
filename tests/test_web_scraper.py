import pytest
import requests
from app import web_scraper

# Define test cases

def test_scrape_coordinates_northeast():
    url = "https://www.airnav.com/airport/BOS"
    result = web_scraper.scrape_coordinates(url)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) == 2, "Result should contain two coordinates"
    assert all(isinstance(coord, float) for coord in result), "All coordinates should be floats"
    assert result == [42.3629444, -71.0063889]

def test_scrape_coordinates_southeast():
    url = "https://www.airnav.com/airport/MIA"
    result = web_scraper.scrape_coordinates(url)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) == 2, "Result should contain two coordinates"
    assert all(isinstance(coord, float) for coord in result), "All coordinates should be floats"
    assert result == [25.7953611, -80.2901158]

def test_scrape_coordinates_northwest():
    url = "https://www.airnav.com/airport/SEA"
    result = web_scraper.scrape_coordinates(url)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) == 2, "Result should contain two coordinates"
    assert all(isinstance(coord, float) for coord in result), "All coordinates should be floats"
    assert result == [47.4498889, -122.3117778]

def test_scrape_coordinates_southwest():
    url = "https://www.airnav.com/airport/LAX"
    result = web_scraper.scrape_coordinates(url)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) == 2, "Result should contain two coordinates"
    assert all(isinstance(coord, float) for coord in result), "All coordinates should be floats"
    assert result == [33.9424964, -118.4080486]

def test_get_coordinates_empty():
    faa_ids = []
    result = web_scraper.get_coordinates(faa_ids)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) == 0, "Result should be empty"

def test_get_coordinates_one():
    faa_ids = ["MIA"]
    result = web_scraper.get_coordinates(faa_ids)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) != 0, "Result should not be empty"
    assert result == [[25.7953611, -80.2901158]]

def test_get_coordinates_many():
    faa_ids = ["MIA", "BOS"]
    result = web_scraper.get_coordinates(faa_ids)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) != 0, "Result should not be empty"
    assert result == [[25.7953611, -80.2901158], [42.3629444, -71.0063889]]


# Run the tests
if __name__ == "__main__":
    pytest.main()
    