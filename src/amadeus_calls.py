"""Uses the Amadeus APIs to extract data from JSON objects."""


from http import client
import json
from csv import DictReader
from pathlib import Path
from posixpath import relpath
from amadeus import Client, ResponseError


def main():
    """Initiates amadeus client, and makes a call to find flight destinations, which are saved to file.
    
    Parameters:
    Origin (str): IATA airport or 3 letter city code. Currently hardcoded to 'JFK'
    
    """
    amadeus = initialize_client()
    response = flight_destinations(amadeus, 'PAR')
    results = relpath("../data/result.json")
    with open(results, 'w') as f:
        json.dump(response.data, f)


def initialize_client():
    api_dict = retrieve_api_keys()
    api_key= api_dict['api_key']
    api_secret = api_dict['api_secret']
    return Client(client_id=api_key, client_secret=api_secret)

def retrieve_api_keys():
    """Pulls API keys from a csv.
    
    Paramters:
    path (str): Path to file containing API keys. Currntly hard coded.
    
    """

    api_keys = relpath("../config/api-keys.csv")
    with open(api_keys, 'r') as f:
        reader= DictReader(f)
        for row in reader:
            return row


def flight_destinations(amadeus: Client, origin: str):
    """Uses the amadeus client to pull a response object with data on flight destinations from an origin city or airport.
    
    Paramters:
    amadeus:    The amadeus Client object initialized using API keys.
    origin:     3 letter city or IATA code. 
    """
    response = amadeus.shopping.flight_destinations.get(origin=origin)
    print(response.status_code)
    print(response.result)
    print(response.data)
    print(response.body)

    return response

if __name__ == '__main__':
    main()