import requests
from dotenv import load_dotenv
import os

class DataManager:
    def __init__(self):
        load_dotenv()
        self.sheet_endpoint = os.environ["SHEETY_ENDPOINT"]
        self.headers = {
            "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
        }

    def get_data(self):
        self.response = requests.get(self.sheet_endpoint, headers=self.headers)
        if self.response.status_code == 200:
            print("Success!")
        else:
            print("Failed to retrieve data:", self.response.status_code)

        self.sheet_data = self.response.json()["prices"]

    def put_data(self, row):
        self.response = requests.put(self.sheet_endpoint + "/" + str(row["id"]),
                                     json={"price": {"iataCode": row["iataCode"]}},
                                     headers=self.headers)


