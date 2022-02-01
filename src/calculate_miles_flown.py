"""Calculates the distance in miles between airports."""


import mysql.connector as sql
import haversine
import sys
from connect_to_db import connect_to_db
from re import match


def main(origin, destination):
    cnx = connect_to_db('db_config.csv')
    cursor = cnx.cursor()

    origin_coords = get_coordinates(airport=origin, cursor=cursor)
    dest_coords = get_coordinates(airport=destination, cursor=cursor)
    distance = calculate_distance(origin_coords, dest_coords)
    print(distance)

def get_coordinates(airport: str, cursor):
    """Returns a tuple of lat/long coordinatees for an airport given the 3 letter IATA code."""
    
    if not match('[A-Z]{3}', airport):
        raise ValueError('Airport must be 3 letter uppercase IATA code.') 

    coords = []
    query_coords = "SELECT lat_decimal, lon_decimal FROM airports WHERE iata_code=%s"
    cursor.execute(query_coords, (airport,))
    for (lat_demical, lon_decmial) in cursor:
        coords.append((lat_demical, lon_decmial))
    
    if len(coords) == 0:
        raise LookupError('Airport code not found in database.')
    if len(coords) > 1:
        raise LookupError('Multiple coordinate sets found for airport entry.')

    return coords[0]


def calculate_distance(origin: tuple, destination: tuple):
    """Returns the distance in miles between two coordinate tuples.
    
    Paramters:
        origin, destination:    coordinates in decimal, using negative values for south/west, ex (12.345, -123.456)
    """
    return haversine.haversine(origin, destination, unit=haversine.Unit.MILES)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])