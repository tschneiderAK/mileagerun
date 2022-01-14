"""Finds flights using the Amadeus API.

args:
    orgin (str):            3 letter IATA airport code for origin.
    destinations (.txt):    .txt file containing a destination airport code on each line.
    start (str):            Date for start of search range, formatted yyyy-mm-dd.
    end (str):              Date for end of search range, formatter yyyy-mm-dd.
    
returns:
    itineraries (list):     List of itinerary objects."""

