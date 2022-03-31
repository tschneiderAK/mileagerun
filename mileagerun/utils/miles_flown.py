"""Calculates the distance in miles between airports."""


import mysql.connector as sql
from haversine import haversine, Unit
import sys
from re import match
from mileagerun import db
from mileagerun.models import *



def calc_distance(origin, destination):
    origin_model = db.session.query(airports).filter_by(iata_code=origin).first()
    dest_model = db.session.query(airports).filter_by(iata_code=destination).first()

    if not (origin_model and dest_model):
        return 'Origin or destination not found.'

    origin_coords = (origin_model.lat_decimal, origin_model.lon_decimal)
    dest_coords = (dest_model.lat_decimal, dest_model.lon_decimal)

    if not (origin_coords and dest_coords):
        return 'Coordinates not found'

    distance = round(haversine(origin_coords, dest_coords, unit=Unit.MILES))

    print(f"Origin: {origin}")
    print(f"Destination: {destination}")
    print(f"Miles flown: {str(round(distance))}")

    return distance


def get_coordinates(airport: str, cursor):
    """Returns a tuple of lat/long coordinatees for an airport given the 3 letter IATA code.
    
    Parameters:
        airport (str):  3-letter IATA code, case insensitive.
        cursor:         MySQL database connection cursor.

    Returns:
        coords (tuple): Latitude/Longitude for the airport in decimal format, negative values denote West/South coordinates.
    """
    airport = airport.upper()
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
