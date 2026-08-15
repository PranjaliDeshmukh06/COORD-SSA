from datetime import datetime, timezone
from itertools import combinations

from src.person1_orbit.tle_loader import load_satellite
from src.person1_orbit.propagator import propagate_satellite
from src.person1_orbit.conjunction_detector import find_closest_approach


def load_tle_file(file_path):
    """Read a 3-line TLE file."""
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    if len(lines) != 3:
        raise ValueError(
            f"{file_path} must contain exactly 3 non-empty lines."
        )

    return lines[0], lines[1], lines[2]


def load_object(file_path):
    """Load one orbital object from a TLE file."""
    name, line1, line2 = load_tle_file(file_path)

    satellite = load_satellite(
        name,
        line1,
        line2
    )

    return {
        "name": name,
        "satellite": satellite
    }


# Load orbital objects
objects = [
    load_object("data/raw/orbital_data/iss.txt"),
    load_object("data/raw/orbital_data/iss2.txt"),
]


# Simulation start time
start_time = datetime(
    2026,
    8,
    15,
    12,
    0,
    0,
    tzinfo=timezone.utc
)


print("MULTI-OBJECT CONJUNCTION ANALYSIS")
print("----------------------------------")


# Check every unique pair
for object_a, object_b in combinations(objects, 2):

    result = find_closest_approach(
        object_a["satellite"],
        object_b["satellite"],
        propagate_satellite,
        start_time,
        duration_minutes=10,
        step_minutes=1,
        screening_threshold_km=10.0
    )

    print(f"\n{object_a['name']} ↔ {object_b['name']}")
    print(f"Closest approach: {result['closest_distance_km']:.3f} km")
    print(f"TCA: {result['tca']}")
    print(f"Status: {result['status']}")

