# Script to run the main program
# Standard libraries used
# Open Weather Map API used
# Sample usage
"""
 python weathr.py --help
usage: weathr.py [-h] [-c CITY] [-u UNITS] [-f {json,string}] [-v]

A command-line tool that accept's a city name as an argument and returns the
weather forecast for that city.

optional arguments:
  -h, --help            show this help message and exit
  -c CITY, --city CITY  City name
  -u UNITS, --units UNITS
                        Units of measurement. Default: standard
  -f {json,xml}, --format {json,string}
                        Output format. Default: json
  -v, --version         show program's version number and exit

"""

import os
import argparse
import json
import sys
import urllib.request

# Fetch API key from environment variable
API_KEY = os.environ.get('OPEN_WEATHER_MAP_API_KEY')

# Base URL for Open Weather Map API
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast?q='

# Default units of measurement
DEFAULT_UNITS = 'standard'

# Default output format
DEFAULT_FORMAT = 'string'

# Default city
DEFAULT_CITY = 'London'

# Default mode
DEFAULT_MODE = 'json'


def get_weather(city, units, format):
    """
    Fetches weather data from Open Weather Map API
    :param city: City name
    :param units: Units of measurement
    :param format: Output format
    :return: Weather data
    """

    # Check if API key is set
    if not API_KEY:
        print('API key not set. Please set OPEN_WEATHER_MAP_API_KEY environment variable')
        sys.exit(1)

    # Check if city is set
    if not city:
        city = DEFAULT_CITY

    # Check if units is set
    if not units:
        units = DEFAULT_UNITS

    # Check if format is set
    if not format:
        format = DEFAULT_FORMAT

    # Build URL
    url = BASE_URL + city + '&units=' + units + '&appid=' + API_KEY + '&mode=' + DEFAULT_FORMAT

    # Fetch data
    try:
        response = urllib.request.urlopen(url)
    except Exception as e:
        print('Error fetching data from Open Weather Map API')
        print(e)
        sys.exit(1)

    # Parse data
    try:
        if format == 'json':
            data = json.loads(response.read().decode('utf-8'))
        elif format == 'string':
            data = json.loads(response.read().decode('utf-8'))
        else:
            print('Invalid format')
            sys.exit(1)
    except Exception as e:
        print('Error parsing data')
        print(e)
        sys.exit(1)

    return data


def main():
    """
    Main function
    :return: None
    """

    # Parse arguments 
    parser = argparse.ArgumentParser(description='A command-line tool that accept\'s a city name as an argument and '
                                                 'returns the weather forecast for that city.')
    parser.add_argument('-c', '--city', help='City name')
    parser.add_argument('-u', '--units', help='Units of measurement. Default: standard (Kelvin) Options : metric, imperial')
    parser.add_argument('-f', '--format', choices=['json', 'string'], help='Output format. Default: String')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()
    
    # Use default values if arguments are not set
    if not args.city:
        args.city = DEFAULT_CITY
    if not args.units:
        args.units = DEFAULT_UNITS
    if not args.format:
        args.format = DEFAULT_FORMAT


    # Fetch weather data
    data = get_weather(args.city, args.units, args.format)

    # get unit of measurement
    if args.units == 'metric':
        args.units = 'C'
    elif args.units == 'imperial':
        args.units = 'F'
    else:
        args.units = 'K'


    # Print data
    if args.format == 'json':
        print(data)
    else:
        # Call function to format data as string like given in sample usage    
        print_data(data, args)


# Function that formats data as string
"""
Sample output : 
  <city name>, <country>
  Current weather: <weather_description>, <temperature> <unit of measurement>
  5-day forecast with dates:
  <date_1>: <weather_description>, <temperature> <unit of measurement>
  <date_2>: <weather_description>, <temperature> <unit of measurement>
  <date_3>: <weather_description>, <temperature> <unit of measurement>
  <date_4>: <weather_description>, <temperature> <unit of measurement>
  <date_5>: <weather_description>, <temperature> <unit of measurement>        
  """
def print_data(data, args):
    """
    Prints weather data
    :param data: Weather data
    :param args: Arguments
    :return: None
    """

    # Get city name
    city = data['city']['name']

    # Get country name
    country = data['city']['country']

    # Get current weather
    current_weather = data['list'][0]['weather'][0]['description']

    # Get current temperature
    current_temperature = data['list'][0]['main']['temp']

    # Get date
    date = data['list'][0]['dt_txt']

    # Print data
    print(city + ', ' + country)
    print('Current weather: ' + current_weather + ', ' + str(current_temperature) + ' ' + args.units)

    # Show future 5 days forecast, group by date
    print('5-day forecast with dates:')
    for item in data['list']:
        if item['dt_txt'].split(' ')[0] != date.split(' ')[0]:
            date = item['dt_txt']
            print(date + ': ' + item['weather'][0]['description'] + ', ' + str(item['main']['temp']) + ' ' + args.units)
            
    
        
if __name__ == '__main__':
    main()





