
# Testing that flight data is pulled successfully
# Source: https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-1-basic-tests/

import pytest
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")

headers = {
    'x-rapidapi-key': f"{api_key}",
    'x-rapidapi-host': "aerodatabox.p.rapidapi.com"
}

# Testing that flight delay API functions properly

def test_get_flightDL1110_status_code_equals_200():
    response = requests.request("GET", "https://aerodatabox.p.rapidapi.com/flights/DL1110/delays", headers=headers)
    assert response.status_code == 200

# Testing that flight delay API yields right output of flight number when called

def test_departure_flightnumber_equals_DL1110():
    response = requests.request("GET", "https://aerodatabox.p.rapidapi.com/flights/DL1110/delays", headers=headers)
    response_body = response.json()
    assert (response_body["number"]) == "DL 1110"

# Testing that current flight status API functions properly

def test_get_flightDL1110_current_status_equals_200():
    response = requests.request("GET", "https://aerodatabox.p.rapidapi.com/flights/DL1110/2021-08-09", headers=headers)
    assert response.status_code == 200

# Testing that environment variables are working properly
# https://tech.serhatteker.com/post/2020-02/test-env-vars-in-python/

def get_key():
    key = os.getenv("api_key")

    if key is None:
        raise OSError("API key is not set.")

# def get_secret():
   # """Simple retrieval function.
   # Returns SECRET or raises OSError.
   # """
   # secret = os.getenv('SECRET', default=None)

   # if secret is None:
     #   raise OSError("SECRET environment is not set.")

    # return secret
