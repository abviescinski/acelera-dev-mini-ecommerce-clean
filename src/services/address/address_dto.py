from dataclasses import dataclass


@dataclass
class AddresstDTO:
    address: str
    city: str
    state: str
    number: str
    zipcode: str
    neighbourhood: str
    primary: bool
    customer_id: int
