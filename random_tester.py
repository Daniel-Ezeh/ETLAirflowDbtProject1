import os
from dotenv import load_dotenv
import requests
from pprint import pprint
import random
import datetime

load_dotenv()

API = os.getenv('RANDOM_USER_API_KEY')


def get_user(number):
    """
    Fetch weather data from the API for a specific city.
    """
    # Endpoint URL for the weather API
    url = f'https://randomuser.me/api/?results={number}'
    try:
        # Send GET request to the API
        response = requests.get(url)
        response.raise_for_status() 

        data = response.json()

        myDict = dict(
        title = data['results'][0]['name']['title'],
        firstname = data['results'][0]['name']['first'],
        lastname = data['results'][0]['name']['last'],
        email = data['results'][0]['email'],
        gender = data['results'][0]['gender'],
        phone = data['results'][0]['phone'],
        country = data['results'][0]['location']['country'],
        post_code = data['results'][0]['location']['postcode']
        )

        return myDict



    except requests.exceptions.RequestException as e:
        # Handle connection errors or bad responses
        print("Error getting user:", e)
        return None




USER = get_user(1)
# pprint(USER)

for keys, values in USER.items():
    print(f'{keys}:\t{values}')



random.randint(5, 30)
def date_gen(x, y):
    start_date = datetime.date(2022, 2, 24)  # import random
    end_date = datetime.date(2022, 3, 7)  # import datetime
    random_duration = random.randrange((end_date - start_date).days)
    random_date = start_date + datetime.timedelta(random_duration)
    return (random_date)

