from datetime import datetime, timezone
from sgp4.api import Satrec, jday


def propagate_satellite(satellite: Satrec, dt: datetime):
    """
    Calculate the satellite's position and velocity at a given time.

    Returns:
        position: (x, y, z) in km
        velocity: (vx, vy, vz) in km/s
    """

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)

    dt = dt.astimezone(timezone.utc)

    jd, fr = jday(
        dt.year,
        dt.month,
        dt.day,
        dt.hour,
        dt.minute,
        dt.second + dt.microsecond / 1_000_000,
    )

    error_code, position, velocity = satellite.sgp4(jd, fr)

    if error_code != 0:
        raise RuntimeError(f"SGP4 propagation failed with error code {error_code}")

    return position, velocity