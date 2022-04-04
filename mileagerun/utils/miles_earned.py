from mileagerun import db
from mileagerun.models import EarningByMiles as E   
from mileagerun.utils.miles_flown import calc_distance
import dataclasses


def miles_earned(miles: float, credit_airline: str, flown_airline: str,flight_type: str, fare_code: str):
    """Returns the total rdm earned on a flight based on the distance flown, carriers, and fare code.
    
    Parameters:
        miles (float):          Distance flown in miles.
        credit_airline (str):   2-letter IATA code for airline the RDMs are credited to.
        flown_airline (str):    2-letter IATA code for airline flown.
        fare_code (str):        Single-letter fare code (A-Z).
    """
    
    multipliers = db.session.query(E).filter(E.credit_airline==credit_airline).\
                                                filter(E.flown_airline==flown_airline).\
                                                filter(E.flight_type==flight_type).\
                                                filter(E.fare_code==fare_code).first()
    
                                           
        # Calculate redeemable miles (rdm), elite qualifying miles (eqm), and elite qualifying dollars (eqd) based on miles flown and earnings multipliers.

    rdm = round(miles * multipliers.total_rdm_mult)
    eqm = round(miles * multipliers.eqm_mult)
    eqd = round(miles * multipliers.eqd_mult)
    earnings = {'rdm': rdm,
                'eqm': eqm,
                'eqd': eqd}
    print(earnings)
    return earnings



if __name__ == '__main__':
    miles_earned(16500, 'DL', 'AF', 'EX-EUROPE', 'Z')

