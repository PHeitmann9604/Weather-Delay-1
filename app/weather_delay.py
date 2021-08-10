
# this is the "app/weather_delay.py" file
from pprint import pprint
import requests
import json
import os
from dotenv import load_dotenv
import operator
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import re
import datetime

if __name__ == "__main__":
    pass

    load_dotenv()

    api_key = os.getenv("api_key")

    # ANALYZING DELAYS BY FLIGHT NUMBER
    try:
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
        anticipated_delay_destination = parsed_response_delay["destinations"]
        median_delay_destination = re.split('[-:]', anticipated_delay_destination[0]["medianDelay"])
        anticipated_delay_origin = parsed_response_delay["origins"]
        median_delay_origin = re.split('[-:]', anticipated_delay_origin[0]["medianDelay"])
    except:
        print("Sorry, invalid flight number. Please input correct flight number")
        exit()
    print("For your destination the anticipated delay is: ", median_delay_destination[-3], "hours and ", median_delay_destination[-2], "minutes")
    print("For your starting airport the anticipated delay is: ", median_delay_origin[-3], "hours and ", median_delay_origin[-2], "minutes")
    # TO DO:  PULL JUST THE FINAL VALUE NOT THE WHOLE RESPONSE



    # ANALYZING STATUS BY FLIGHT NUMBER AND FLIGHT DATE

    # flight_date = "2021-08-04"
    try:
        flight_date = input("Please input your flight date (e.g. '2021-08-04'): ")

        status_url = f"https://aerodatabox.p.rapidapi.com/flights/{flight_number}/{flight_date}"

        headers = {
            'x-rapidapi-key': f"{api_key}",
            'x-rapidapi-host': "aerodatabox.p.rapidapi.com"
            }

        response_status = requests.request("GET", status_url, headers=headers)
        parsed_response_status = json.loads(response_status.text)
    except:
        print("Sorry, invalid flight date. Please input correct flight date")
        exit()
    # print(type(response_status)) #> <class 'requests.models.Response'>
    # print(response_status.status_code) #> 200
    # print(response_status.text) #>[{"greatCircleDistance":{"meter":345185.09,"km":345.185,"mile":214.488,"nm":186.385,"feet":1132497.0},"departure":{"airport":{"icao":"KATL","iata":"ATL","name":"Atlanta, Hartsfield Jackson Atlanta","shortName":"Hartsfield Jackson","municipalityName":"Atlanta","location":{"lat":33.6367,"lon":-84.4281},"countryCode":"US"},"scheduledTimeLocal":"2021-08-04 23:35-04:00","actualTimeLocal":"2021-08-04 23:44-04:00","runwayTimeLocal":"2021-08-04 23:44-04:00","scheduledTimeUtc":"2021-08-05 03:35Z","actualTimeUtc":"2021-08-05 03:44Z","runwayTimeUtc":"2021-08-05 03:44Z","terminal":"S","runway":"08R","quality":["Basic","Live"]},"arrival":{"airport":{"icao":"KSAV","iata":"SAV","name":"Savannah, Savannah Hilton Head","shortName":"Hilton Head","municipalityName":"Savannah","location":{"lat":32.1276,"lon":-81.2021},"countryCode":"US"},"scheduledTimeLocal":"2021-08-05 00:38-04:00","actualTimeLocal":"2021-08-05 00:21-04:00","scheduledTimeUtc":"2021-08-05 04:38Z","actualTimeUtc":"2021-08-05 04:21Z","quality":["Basic","Live"]},"lastUpdatedUtc":"2021-08-05 03:48Z","number":"DL 1110","callSign":"DAL1110","status":"EnRoute","codeshareStatus":"IsOperator","isCargo":false,"aircraft":{"reg":"N339NW","modeS":"A3B87F","model":"Airbus A320-100/200"},"airline":{"name":"Delta Air Lines"}}]
    # pprint(parsed_response_status)
    # print(parsed_response_status.keys())
    flight_status = parsed_response_status[0]['status']
    departure_airport = parsed_response_status[0]['departure']['airport']['name']
    departure_time = parsed_response_status[0]['departure']['scheduledTimeLocal']
    arrival_airport = parsed_response_status[0]['arrival']['airport']['name']
    arrival_time = parsed_response_status[0]['arrival']['scheduledTimeLocal']
    if flight_status == "Unknown":
        print("Your flight from", departure_airport, "to", arrival_airport, "is scheduled to depart at:", departure_time)
    elif flight_status == "Arrived":
        print("Your flight from", departure_airport, "to", arrival_airport, "is arrived at:", departure_time)
    else: 
        print("Your flight from", departure_airport, "to", arrival_airport, "is", flight_status)

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>

subject = "Your Flight Delay and Status Update"

html_content = f"Your anticipated {arrival_airport} delay is: {median_delay_destination[-3]} hours and {median_delay_destination[-2]} minutes and {departure_airport} airport anticipated delay is: {median_delay_origin[-3]} hours and {median_delay_origin[-2]} minutes. Your flight from {departure_airport} to {arrival_airport} is: {flight_status}"
email_response = input("Do you wish to have an email summary sent? (Yes/No):")
if email_response == "Yes":
    receiver_email_address = input("Please input the email address where you would like to receive updates: ")
    message = Mail(from_email=SENDER_ADDRESS, to_emails=receiver_email_address, subject=subject, html_content=html_content)
    try:
        response = client.send(message)
        print(response.status_code)#> 202 indicates SUCCESS
        print("Great, you will receive an email shortly. Have a safe trip!")
    except Exception as err:
        print(type(err))
        print(err)
else: 
    print("Thank you. Have a safe trip!")


