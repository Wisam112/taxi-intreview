from dataclasses import dataclass


@dataclass
class Taxi:
    taxi_id: int
    available: bool