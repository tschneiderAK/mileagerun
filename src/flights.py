"""Defines classes Segment and Itinerary."""


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
        self.segments = segments

def main():
    return


