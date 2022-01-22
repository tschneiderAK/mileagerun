"""Uses the Amadeus APIs to extract data from JSON objects."""


import json
from csv import DictReader
from pathlib import Path
from posixpath import relpath
from amadeus import Client


def main():
    """Retrieves authorization tokens, initiates amadeus client, and makes a call to find flight destinations, which are saved to file.
    
    Parameters:
    Origin (str): IATA airport or 3 letter city code. Currently hardcoded to 'JFK'
    
    """
    api_dict = retrieve_api_keys()
    api_key= api_dict['api_key']
    api_secret = api_dict['api_secret']
    print(api_key)
    print(api_secret)

    amadeus = Client(client_id=api_key, client_secret=api_secret)
    response = flight_destinations(amadeus, 'JFK')

    results = relpath("../data/result.json")
    with open(results, 'rw') as f:
        json.dump(response, f)



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
    origin:     3 letter city or IATA code. Defaults to 'JFK'. 
    """
    response = amadeus.shopping.flight_destinations.get(origin=origin)
    print(response.status_code)
    print(response.result)
    print(response.data)
    print(response.body)
    print(response.body)

    return response

if __name__ == '__main__':
    main()