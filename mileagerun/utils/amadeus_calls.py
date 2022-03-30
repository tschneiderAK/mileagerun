"""Uses the Amadeus APIs to extract data from JSON objects."""


import os.path
from csv import DictReader
from amadeus import Client, ResponseError


def main():
    """Initiates amadeus client, and makes a call to find flight destinations, which are saved to file.
    
    Parameters:
    Origin (str): IATA airport or 3 letter city code. Currently hardcoded to 'JFK'
    
    """
    amadeus = initialize_client()
    # pricing_test(amadeus)       
    # response = flight_destinations(amadeus, 'PAR')
    # results = relpath("../data/result.json")
    # with open(results, 'w') as f:
    #     json.dump(response.data, f)


def pricing_test(amadeus):
    try:
        '''
        Confirm availability and price from SYD to BKK in summer 2022
        '''
        flights = amadeus.shopping.flight_offers_search.get(originLocationCode='SYD', destinationLocationCode='BKK',
                                                            departureDate='2022-07-01', adults=1).data
        response_one_flight = amadeus.shopping.flight_offers.pricing.post(
            flights[0])
        print(response_one_flight.data)

        response_two_flights = amadeus.shopping.flight_offers.pricing.post(
            flights[0:2])
        print(response_two_flights.data)
    except ResponseError as error:
        raise error

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

    api_keys = os.path.join(os.path.dirname(__file__), "../config/api-keys.csv")
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