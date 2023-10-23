# airport-polygon-verifier
 A tool that checks whether each airport, represented by their FAA Airport Identifier in a list, is within a polygon represented by a list of coordinates.

## Getting Started 

To get started, follow the following steps. 

1. Set up a Python 3 virtual environment by running the following commands in your terminal. 

`python3 -m venv venv`

`source venv/bin/activate`

2. Install dependencies by running the following command in your terminal. 

`python3 -m pip install -r requirements.txt`

## Running Locally

Start the server by running the following command in your terminal. 

`python3 main.py`

Navigate to `http://127.0.0.1:8080/:` to view your server. Make sure to refresh the page after making changes to the code. 

## Testing 

To test the code, run the following commands in your terminal.

`pytest tests/test_web_scraper.py`
`pytest tests/test_polygon_checker.py`

## Understanding the structure

Here's a brief explanation of each directory and file in the project:

### `/app`

This directory contains the main application code.

- `__init__.py`: An empty file that marks the directory as a Python package.
- `web_scraper.py`: Contains code for web scraping `https://www.airnav.com` to collect airport data.
- `polygon_checker.py`: Contains code for checking whether an airport is within the polygon.

### `/tests`

This directory contains unit tests for your application.

- `__init__.py`: An empty file that marks the directory as a Python package.
- `test_web_scraper.py`: Contains tests for the web_scraper module.
- `test_polygon_checker.py`: Contains tests for the polygon_checker module.

### `main.py`

The entry point of my application, where I run my main logic and designed a simple frontend to demo the application.

# Reflection 

## Initial Planning 

[Pipeline for Application](Pipeline.jpg)

I initially broke down the problem by thinking about my inputs, actions, and outputs. The image represents my initial pipeline thought process. 

## Assumptions

Given the fact the specification of the application was left purposely under-specified, I began to think about the key assumptions that my functions would have in this application. In the future, I hope to make this application more robust and applicable to real life by loosening these assumptions and fortifying my test suite. 

1. FAA Airport Identifiers are valid identifiers, meaning they are identifiers for American airports and will not be inputted erroneously. 

2. `https://www.airnav.com` will always be correct and up to date.

3. `https://www.airnav.com` will always have the same HTML page structure. 

4. `https://www.airnav.com` lists coordinates for airports in (Latitude, Longitude) order. 

5. All given and outputted coordinates are all in decimal degrees.

6. The length of the list of coordinates is **not** upper bounded, but is lower bounded to be greater than or equal to 3 (since it must be a valid polygon).

7. The list of coordinates represents a [**simple** polygon](https://en.wikipedia.org/wiki/Simple_polygon) with only straight edges of the lowest possible distance between vertices.

8. Polygon will be "drawn" in the order of the list of coordinates. 

9. In order for an airport to be inside of a polygon, it must lie within the polygon or on one of it's edges.  

## Final thoughts

- `web_scraper.py`: I personally wish this code was more generalizable by perhaps using an API to get an airport's coordinates instead of scraping the web, in case the website we are scraping from becomes defunct.

- `polygon_checker.py`: I realized there are many ways of approaching this problem. In fact, there are many third-party Python packages that can actually perform this check. In addition, I also learned about the many different algorithms that exist to check whether a point is in a polygon. I decided to implement the simplest algorithm for now by hand since I'm not sure what the client's preferences are for using third-party Python packages (and not being able to dig into their code and see whether their implementation meets my personal assumptions).


