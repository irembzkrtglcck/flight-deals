from dotenv import load_dotenv
import os, requests
from datetime import datetime, timedelta

class FlightSearch:
    def __init__(self):
        load_dotenv()
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._api_url = os.environ["AMADEUS_ENDPOINT"]
        self._token = self._get_new_token()

    def get_iata_code(self, city_name):
        city_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        headers = {"Authorization": f"Bearer {self._token}"}
        params = {"keyword": city_name}
        response = requests.get(url=city_endpoint, params= params , headers=headers)
        try:
            return response.json()["data"][0]["iataCode"]
        except(IndexError, KeyError):
            return "N/A"

    def _get_new_token(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"grant_type": "client_credentials",
                     "client_id": self._api_key,
                     "client_secret": self._api_secret}
        response = requests.post(self._api_url, data=data, headers=headers)

        # print(f"Your token is {response.json()['access_token']}")
        # print(f"Your token expires in {response.json()['expires_in']} seconds")

        return response.json()["access_token"]

    def search_flights(self, origin, destination):
        flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {"Authorization": f"Bearer {self._token}"}

        params = {"originLocationCode": origin,
                  "destinationLocationCode": destination,
                  "departureDate": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
                  "returnDate": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
                  "adults": 2,
                  "nonStop": "false",
                  "currencyCode": "TRY"}

        response = requests.get(url=flight_endpoint, params= params , headers=headers)
        # print(response.status_code)
        # print(response.text)
        try:
            return response.json()
        except (IndexError, KeyError):
            print(f"No flights found for {destination}")
            return None