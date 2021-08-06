
# this is the "app/weather_delay.py" file
from pprint import pprint
import requests
import json
import os
from dotenv import load_dotenv
import operator

if __name__ == "__main__":
    pass

    load_dotenv()

    api_key = os.getenv("api_key")

    # ANALYZING DELAYS BY FLIGHT NUMBER

    flight_number = input("please enter your flight number, two letters followed by numbers:")
    delay_url = f"https://aerodatabox.p.rapidapi.com/flights/{flight_number}/delays"

    headers = {
        'x-rapidapi-key': f"{api_key}",
        'x-rapidapi-host': "aerodatabox.p.rapidapi.com"
        }

    # GET THE DATA

    response_delay = requests.request("GET", delay_url, headers=headers)
    # print(type(response_delay)) #> <class 'requests.models.Response'>
    # print(response_delay.status_code) #> 200
    # print(response_delay.text) #>{"number":"B6 2893","origins":[],"destinations":[]}
    parsed_response_delay = json.loads(response_delay.text)
    # breakpoint()
    # pprint(parsed_response_delay)
    # print(parsed_response_delay.keys())

    # breakpoint ()

    # ANALYZE THE DATA
    anticipated_delay_destination = parsed_response_delay['destinations']
    anticipated_delay_origin = parsed_response_delay['origins']
    print("For your destination the anticipated delay is: ", anticipated_delay_destination[0]["medianDelay"])
    print("For your starting airport the anticipated delay is: ", anticipated_delay_destination[0]["medianDelay"])
    # TO DO:  PULL JUST THE FINAL VALUE NOT THE WHOLE RESPONSE


    # ANALYZING STATUS BY FLIGHT NUMBER AND FLIGHT DATE

    # flight_date = "2021-08-04"
    flight_date = input("Please input your flight date (e.g. '2021-08-04'): ")

    status_url = f"https://aerodatabox.p.rapidapi.com/flights/{flight_number}/{flight_date}"

    headers = {
        'x-rapidapi-key': f"{api_key}",
        'x-rapidapi-host': "aerodatabox.p.rapidapi.com"
        }

    response_status = requests.request("GET", status_url, headers=headers)
    parsed_response_status = json.loads(response_status.text)
    # print(type(response_status)) #> <class 'requests.models.Response'>
    # print(response_status.status_code) #> 200
    # print(response_status.text) #>[{"greatCircleDistance":{"meter":345185.09,"km":345.185,"mile":214.488,"nm":186.385,"feet":1132497.0},"departure":{"airport":{"icao":"KATL","iata":"ATL","name":"Atlanta, Hartsfield Jackson Atlanta","shortName":"Hartsfield Jackson","municipalityName":"Atlanta","location":{"lat":33.6367,"lon":-84.4281},"countryCode":"US"},"scheduledTimeLocal":"2021-08-04 23:35-04:00","actualTimeLocal":"2021-08-04 23:44-04:00","runwayTimeLocal":"2021-08-04 23:44-04:00","scheduledTimeUtc":"2021-08-05 03:35Z","actualTimeUtc":"2021-08-05 03:44Z","runwayTimeUtc":"2021-08-05 03:44Z","terminal":"S","runway":"08R","quality":["Basic","Live"]},"arrival":{"airport":{"icao":"KSAV","iata":"SAV","name":"Savannah, Savannah Hilton Head","shortName":"Hilton Head","municipalityName":"Savannah","location":{"lat":32.1276,"lon":-81.2021},"countryCode":"US"},"scheduledTimeLocal":"2021-08-05 00:38-04:00","actualTimeLocal":"2021-08-05 00:21-04:00","scheduledTimeUtc":"2021-08-05 04:38Z","actualTimeUtc":"2021-08-05 04:21Z","quality":["Basic","Live"]},"lastUpdatedUtc":"2021-08-05 03:48Z","number":"DL 1110","callSign":"DAL1110","status":"EnRoute","codeshareStatus":"IsOperator","isCargo":false,"aircraft":{"reg":"N339NW","modeS":"A3B87F","model":"Airbus A320-100/200"},"airline":{"name":"Delta Air Lines"}}]
    # pprint(parsed_response_status)
    # print(parsed_response_status.keys())
    print(parsed_response_status[0]['status'])
