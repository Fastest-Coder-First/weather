# weathr
A command-line tool that accept's a city name as an argument and returns the weather forecast for that city.

It leverages the [OpenWeatherMap API](https://openweathermap.org/api) to retrieve the weather data and parse it using Python into a human-readable format.

## Features
- [x] Current weather
- [x] 5-day forecast

## Installation
1. Create an account on [OpenWeatherMap](https://openweathermap.org/api) and generate an API key.
2. Set API key as an environment variable.
```bash
$ export OPEN_WEATHER_MAP_API_KEY="your-api-key"
```
3. Clone the repository and install the dependencies.

```bash
$ git clone
$ cd weathr
```

## Usage
```bash
$ python weathr.py --help
usage: weathr.py [-h] [-c CITY] [-u UNITS] [-f {json,string}] [-v]

A command-line tool that accepts a city name as an argument and returns the weather forecast for that city.

optional arguments:
  -h, --help            show this help message and exit
  -c CITY, --city CITY  City name
  -u UNITS, --units UNITS
                        Units of measurement. Default: standard
  -f {json, string}, --format {json, string}
                        Output format. Default: json
  -v, --version         show program's version number and exit
```

## Examples
```bash
$ python weathr.py -c "New York"
New York, US
Current weather: Clear, 1.0°C
5-day forecast:
    2020-02-19: Clear, 1.0°C
    2020-02-20: Clear, 3.0°C
    2020-02-21: Clear, 4.0°C
    2020-02-22: Clear, 4.0°C
    2020-02-23: Clear, 4.0°C
```

```bash
$ python weathr.py -c "New York" -u metric
New York, US
Current weather: Clear, 1.0°C
5-day forecast:
    2020-02-19: Clear, 1.0°C
    2020-02-20: Clear, 3.0°C
    2020-02-21: Clear, 4.0°C
    2020-02-22: Clear, 4.0°C
    2020-02-23: Clear, 4.0°C
```

## GitHub Co-Pilot Usage 

Watch this video to see how I used GitHub Co-Pilot to write the code for this project:

https://watch.screencastify.com/v/CXfJLuprHxSCn7fGclgQ

I used GitHub Co-Pilot to create the following files:
1. readme.md : This file helped me  to create basic overview of the project. Acted as guidelines for the project.
2. weathr.py : This implemented the functionality specified in readme.md. It helped me to create the basic structure of the project.

    
## Author
Kushal Bhabra - kushal.bhabra@tcs.com
