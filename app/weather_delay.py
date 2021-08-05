# this is the "app/weather_delay.py" file
from pprint import pprint
import requests
import json
import os
from dotenv import load_dotenv

# api_key = os.environ.get("RapidAPI_KEY")
api_key = "bd4835e76amsh64eed19c3572ba7p146087jsn8985df88bde8"
flight_number = "JBU2893"

delay_url = f"https://aerodatabox.p.rapidapi.com/flights/{flight_number}/delays"

headers = {
    'x-rapidapi-key': f"{api_key}",
    'x-rapidapi-host': "aerodatabox.p.rapidapi.com"
    }

response_delay = requests.request("GET", delay_url, headers=headers)
parsed_response_delay = json.loads(response_delay.text)
pprint(parsed_response_delay)
print(parsed_response_delay.keys())

flight_date = "2021-08-04"

status_url = f"https://aerodatabox.p.rapidapi.com/flights/{flight_number}/{flight_date}"

headers = {
    'x-rapidapi-key': f"{api_key}",
    'x-rapidapi-host': "aerodatabox.p.rapidapi.com"
    }

response_status = requests.request("GET", status_url, headers=headers)
parsed_response_status = json.loads(response_status.text)
pprint(parsed_response_status)
print(parsed_response_status.keys())