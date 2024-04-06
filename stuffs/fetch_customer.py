import os
import requests
from datetime import datetime


def get_user():
    """
    Fetch weather data from the API for a specific city.
    """
    t = datetime.now()
    customer_id = t.strftime("%f%y%j%H%M")
    a = int(customer_id)

    dating = t.strftime("%Y-%m-%dT%H:%M:%S")


    # Endpoint URL for the weather API
    url = f'https://randomuser.me/api/?results=1'
    try:
        # Send GET request to the API
        response = requests.get(url)
        response.raise_for_status() 

        data = response.json()

        myDict = dict(
        customer_id = a,
        title = data['results'][0]['name']['title'],
        firstname = data['results'][0]['name']['first'],
        lastname = data['results'][0]['name']['last'],
         address = str(data['results'][0]['location']['street']['number']) + " " + data['results'][0]['location']['street']['name'] + " " + data['results'][0]['location']['city'] + " " + data['results'][0]['location']['state'],
        email = data['results'][0]['email'],
        gender = data['results'][0]['gender'],
        phone = data['results'][0]['phone'],
        country = data['results'][0]['location']['country'],
        date_added = dating
        )
        return myDict

    except requests.exceptions.RequestException as e:
        # Handle connection errors or bad responses
        print("Error getting user:", e)
        return None


USER = get_user()


values = (
    USER['customer_id'],
    USER['firstname'],
    USER['lastname'],
    USER['gender'],
    USER['email'],
    USER['phone'],
    USER['address'],
    USER['country'],
    USER['date_added']
)

print(values)

