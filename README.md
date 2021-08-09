
# FLIGHT DELAY APP
A python application that you can use to provide travelers with a tool to assess the likelihood of flight delay, and send delay-related messages once they book.

## Prerequisites
To use this application, you will need:

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## INSTALLATION
Fork this repository from Github (https://github.com/PHeitmann9604/Weather-Delay-1) and then clone to use under your own control.

Once the product information is set, navigate to the project repository from the command line.

```sh
 cd app/weather_delay
 ```

Use Anaconda to create, activate, and name a new virtual environment for this app:

```sh
conda create -n delay-env python=3.8
conda activate delay-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

## Setup

Create a ".env" file in the root directory of your local repository. You will need to update this file with the API key that you obtain from AeroDataBox (https://rapidapi.com/aerodatabox/api/aerodatabox/).

    api_key="this will be a long string of numbers and letters"

NOTE - utilization of this API is only free with the Basic plan. Should you wish to make a significant number of data calls or use for commercial purposes, you will need to pay for a higher tier of access.

 ## USAGE
 Run the Python program:

 ```py
 python app/weather_delay.py
 ```
 ## CONTACT
If you have any questions about this program, please contact Patrick at pjh9604@stern.nyu.edu  or  Claire at cec9702@stern.nyu.edu.
