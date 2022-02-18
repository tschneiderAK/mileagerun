from connect_to_db import connect_to_db   


def rdm_from_distance(miles: float, credit_airline: str, flown_airline: str,flight_type: str, fare_code: str):
    """Returns the total rdm earned on a flight based on the distance flown, carriers, and fare code.
    
    Parameters:
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
            AND fare_code=%s;"""

    cursor.execute(sql, (credit_airline, flown_airline, flight_type, fare_code))
    multipliers = dict(zip(cursor.column_names, cursor.fetchone()))
    
    # Calculate redeemable miles (rdm), elite qualifying miles (eqm), and elite qualifying dollars (eqd) based on miles flown and earnings multipliers.

    rdm = miles * multipliers['total_rdm_mult']
    eqm = miles * multipliers['eqm_mult']
    eqd = miles * multipliers['eqd_mult']
    earnings = {'rdm': rdm,
                'eqm': eqm,
                'eqd': eqd}
    print(earnings)
    return earnings
    

if __name__ == '__main__':
    rdm_from_distance(16500, 'DL', 'AF', 'EX-EUROPE', 'Z')

