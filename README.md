# flight-finder
Calculates frequent flyer miles earned based on the earning airline and the marketing/operating airline.

Usage:

calculate_miles_earned:

rdm_from_distance():
Returns the total rdm earned on a flight based on the distance flown, carriers, and fare code.
    
    Parameters:
        miles (float):          Distance flown in miles.
        credit_airline (str):   2-letter IATA code for airline the RDMs are credited to.
        flown_airline (str):    2-letter IATA code for airline flown.
        fare_code (str):        Single-letter fare code (A-Z).

Test re-name.