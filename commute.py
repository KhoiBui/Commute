import googlemaps, requests, json, keys
from twilio.rest import Client
from datetime import datetime


def send_update(message):
    twilio_client = Client(keys.account_sid, keys.auth_token)
    twilio_client.api.messages.create(to=keys.to_number,
                                      from_=keys.from_number,
                                      body=message)


def init_map():
    url = 'https://maps.googleapis.com/maps/api/directions/json?'
    maps_params = dict(origin=keys.origin,
                       destination=keys.destination,
                       alternatives='true',
                       departure_time='now',
                       key=keys.api_key)

    results = requests.get(url, maps_params)
    data = json.loads(results.content.decode('utf-8'))
    legs_info = ''

    for i in range(len(data['routes'])):
        info = data['routes'][i]['summary'] + ': ' + str(data['routes'][i]['legs'][0]['duration']['text']) + '\n'
        legs_info += info

    # debug
    print(legs_info)

    return legs_info


def main():
    maps_results = init_map()
    #send_update(maps_results)

if __name__ == '__main__':
    main()
