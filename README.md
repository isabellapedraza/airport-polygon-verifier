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

## Understanding the structure

TODO

Here's a brief explanation of each directory and file in the project:

app/: This directory contains the main application code.

__init__.py: An empty file that marks the directory as a Python package.
airport_locator.py: Contains code to find the nearest airport within the provided polygon.
web_scraper.py: Contains code for web scraping to collect airport data.
polygon_checker.py: Contains code for checking whether an airport is within the polygon.
tests/: This directory contains unit tests for your application.

__init__.py: An empty file that marks the directory as a Python package.
test_airport_locator.py: Contains tests for the airport_locator module.
test_web_scraper.py: Contains tests for the web_scraper module.
test_polygon_checker.py: Contains tests for the polygon_checker module.
data/: This directory can hold any data files you need for your application. For example, it might contain a CSV file with airport data.

README.md: A readme file that explains how to use your application, provides an overview of the project, and documents any other necessary information.

presentation/: This directory contains files related to your presentation, such as slides or documents.

main.py: The entry point of your application, where you run your main logic.

With this structure, you can keep your code well-organized and separated by functionality. The app directory contains the core application code, and the tests directory contains your test cases. Additionally, you have dedicated directories for data, documentation, and presentation materials.


TODO: make up robust to erroneous input