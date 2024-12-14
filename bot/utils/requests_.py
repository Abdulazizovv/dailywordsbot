import requests
from requests.adapters import HTTPAdapter
import logging

url = 'http://localhost:8000'
session = requests.Session()
session.mount('http://', HTTPAdapter(max_retries=3))


def get(url, params=None):
    try:
        response = session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        logging.error(err)
        return None


def post(url, data=None):
    try:
        response = session.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        logging.error(err)
        return None
    

def put(url, data=None):
    try:
        response = session.put(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        logging.error(err)
        return None


def delete(url):
    try:
        response = session.delete(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        logging.error(err)
        return None
    

# for getting all bot users from the API
def get_users():
    """Get all bot users from the API"""
    return get(f'{url}/api/bot-users/')


# for getting a single bot user from the API
def get_user(user_id: int):
    """Get a single bot user from the API
    Args:
        user_id (int): The ID of the bot user not telegram user ID
    """
    return get(f'{url}/api/bot-users/{user_id}/')


# for creating a new bot user
def create_user(data):
    """Create a new bot user in the API database
    Args:
        data (dict): The data to be sent to the API
        data = {
            "user_id": 1, -> telegram user ID
            "username": "test", -> telegram username
            "first_name": "test",
            "last_name": "test",
            "phone_number": "123456789"|None
        }
    """
    return post(f'{url}/api/bot-users/', data)

