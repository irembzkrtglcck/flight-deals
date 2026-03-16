#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint
from notification_manager import NotificationManager
import time

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

data_manager.get_data()

for row in data_manager.sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_iata_code(row["city"])
        data_manager.put_data(row)
        time.sleep(2)

#pprint(data_manager.sheet_data)

all_deals = ""

for row in data_manager.sheet_data:
    data = flight_search.search_flights("IST", row["iataCode"])
    cheapest = FlightData.find_cheapest_flight(data)
    print(f"{row['city']}: {cheapest.price} TRY, {cheapest.out_date} - {cheapest.return_date}")

    if cheapest.price != "N/A" and float(cheapest.price) < row["lowestPrice"]:
        all_deals += (f"{row['city']}: {cheapest.price} TRY\n"
                      f"  {cheapest.origin_airport} -> {cheapest.destination_airport}\n"
                      f"  Gidis: {cheapest.out_date}\n"
                      f"  Donus: {cheapest.return_date}\n"
                      f"  Istanbul cikisli, Gidis-Donus, 2 Yetiskin, Aktarmali\n\n Bilgi: SAW: Sabiha Gokcen Havalimani, IST: Istanbul Havalimani \n\n")

    time.sleep(2)

if all_deals:
    notification_manager.send_email(all_deals)
    print("Email gonderildi!")
