from datetime import datetime, timedelta, timezone

from src.person1_orbit.tle_loader import load_satellite
from src.person1_orbit.propagator import propagate_satellite
from src.person1_orbit.distance import calculate_distance


def load_tle_file(file_path):
    """Read a 3-line TLE file."""
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    if len(lines) != 3:
        raise ValueError(
            f"{file_path} must contain exactly 3 non-empty lines."
        )

    return lines[0], lines[1], lines[2]


# Load Satellite A
name1, line1_1, line2_1 = load_tle_file(
    "data/raw/orbital_data/iss.txt"
)

satellite1 = load_satellite(name1, line1_1, line2_1)


# Load Satellite B
name2, line1_2, line2_2 = load_tle_file(
    "data/raw/orbital_data/iss2.txt"
)

satellite2 = load_satellite(name2, line1_2, line2_2)


# Simulation start time
start_time = datetime(
    2026, 8, 15, 12, 0, 0, tzinfo=timezone.utc
)


# Track the closest approach
minimum_distance = float("inf")
time_of_closest_approach = None


print("Satellite 1:", name1)
print("Satellite 2:", name2)
print("\nSimulation:\n")


# Simulate for 10 minutes
for i in range(10):

    current_time = start_time + timedelta(minutes=i)

    position1, velocity1 = propagate_satellite(
        satellite1,
        current_time
    )

    position2, velocity2 = propagate_satellite(
        satellite2,
        current_time
    )

    distance = calculate_distance(
        position1,
        position2
    )

    print(
        f"{current_time.strftime('%H:%M:%S')} UTC "
        f"→ Distance: {distance:.3f} km"
    )

    # Check whether this is the closest point so far
    if distance < minimum_distance:
        minimum_distance = distance
        time_of_closest_approach = current_time


print("\n-----------------------------")
print("Closest approach:")
print("Time:", time_of_closest_approach)
print(f"Minimum distance: {minimum_distance:.3f} km")
print("-----------------------------")