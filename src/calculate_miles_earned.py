from connect_to_db import connect_to_db
import dataclasses


@dataclasses.dataclass
class Segment:
    origin:         str
    destination:    str
    date:           str
    flight_number:  str
    fare_code:      str


class Itinerary:
    def __init__(
            self, 
            price: float,
            currency: str,
            origin: str,
            destination: str,
            date: str,
            segments: list
            ) -> None:

        self.price = price
        self.currency = currency
        self.origin = origin
        self.destination = destination
        self.date = date
        self.segmentss = segments



def rdm_from_distance(miles: float, credit_airline: str, flown_airline: str,flight_type: str, fare_code: str):
    """Returns the total rdm earned on a flight based on the distance flown, carriers, and fare code.
    
    Paramters:
        miles (float):          Distance flown in miles.
        credit_airline (str):   2-letter IATA code for airline the RDMs are credited to.
        flown_airline (str):    2-letter IATA code for airline flown.
        fare_code (str):        Single-letter fare code (A-Z).
        """
    
    cnx = connect_to_db('db_config.csv')
    cursor = cnx.cursor()
    sql = """SELECT total_rdm_mult, eqm_mult, eqd_mult FROM earning_by_miles
            WHERE credit_airline=%s
            AND flown_airline=%s
            AND flight_type=%s
            AND fare_code=%s
            LIMIT 1;"""
    cursor.execute(sql, (credit_airline, flown_airline, flight_type, fare_code))
    print(cursor.fetchall())

    cnx

if __name__ == '__main__':
    rdm_from_distance(100, 'DL', 'AF', 'EX-EUROPE', 'J')

