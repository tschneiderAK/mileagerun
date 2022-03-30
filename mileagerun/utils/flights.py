"""Defines classes Segment and Itinerary."""


import dataclasses


@dataclasses.dataclass
class Segment:
    origin:         str
    destination:    str
    date:           str
    flight_number:  str
    fare_code:      str
    airline:        str


class Itinerary:
    def __init__(
            self, 
            price: float,
            currency: str,
            origin: str,
            destination: str,
            date: str,
            segments: list,
            ) -> None:

        self.price = price
        self.currency = currency
        self.origin = origin
        self.destination = destination
        self.date = date
        self.segments = segments


class ReturnItinerary(Itinerary):
    def __init__(self,
                return_date = str,
                return_segments = list):
        super().__init__()
        self.return_date = return_date
        self.return_segments = return_segments

def main():
    return


