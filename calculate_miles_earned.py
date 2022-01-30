import calculate_miles_earned
import connect_to_db


def rdm_from_distance(miles: float, credit_airline: str, flown_airline: str, fare_code: str):
    """Returns the total rdm earned on a flight based on the distance flown, carriers, and fare code.
    
    Paramters:
        miles (float):          Distance flown in miles.
        credit_airline (str):   2-letter IATA code for airline the RDMs are credited to.
        flown_airline (str):    2-letter IATA code for airline flown.
        fare_code (str):        Single-letter fare code (A-Z).
        """
    
    fare_code = fare_code.toupper()
