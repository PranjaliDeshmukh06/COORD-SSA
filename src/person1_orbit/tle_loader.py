from sgp4.api import Satrec


def load_satellite(name: str, line1: str, line2: str) -> Satrec:
    """
    Create a satellite object from TLE data.
    """
    satellite = Satrec.twoline2rv(line1, line2)
    return satellite