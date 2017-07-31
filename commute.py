import googlemaps
import requests
import json
from twilio.rest import Client
from datetime import datetime

account_sid = "ACce8cdb02b92c13c649a9038ce7a1dfe9"
auth_token = "45260117b34aee94b10a495378a54d68"


def send_update(message):
    twilio_client = Client(account_sid, auth_token)
    twilio_client.api.messages.create(to="+17144231250",
                                      from_="+19097363470",
                                      body=message)


def init_map():
    url = 'https://maps.googleapis.com/maps/api/directions/json?'
    maps_params = dict(origin='6450+Dougherty+Road+Dublin+California+94568',
                       destination='6160+Workday+Way+Pleasanton+California+94588',
                       alternatives='true',
                       departure_time='now',
                       key='AIzaSyD-D-ZaekwsZcxBDtlnG-N_Ywqwdo8jeCo')

    results = requests.get(url, maps_params)
    data = json.loads(results.content)
    legs_info = ''

    for i in range(len(data['routes'])):
        info = data['routes'][i]['summary'] + ': ' + str(data['routes'][i]['legs'][0]['duration']['text']) + '\n'
        legs_info += info

    print(legs_info)
    return legs_info


def main():
    maps_results = init_map()
    send_update(maps_results)

if __name__ == '__main__':
    main()
