def find_closest_approach(
    satellite1,
    satellite2,
    propagate_function,
    start_time,
    duration_minutes=10,
    step_minutes=1,
    screening_threshold_km=10.0
):
    """
    Find the closest approach between two space objects
    during the simulation window.

    The screening threshold is a prototype parameter,
    not an operational collision threshold.
    """

    from datetime import timedelta

    minimum_distance_km = float("inf")
    time_of_closest_approach = None

    for i in range(0, duration_minutes, step_minutes):

        current_time = start_time + timedelta(minutes=i)

        position1, _ = propagate_function(
            satellite1,
            current_time
        )

        position2, _ = propagate_function(
            satellite2,
            current_time
        )

        dx = position1[0] - position2[0]
        dy = position1[1] - position2[1]
        dz = position1[2] - position2[2]

        distance_km = (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5

        if distance_km < minimum_distance_km:
            minimum_distance_km = distance_km
            time_of_closest_approach = current_time

    if minimum_distance_km <= screening_threshold_km:
        status = "CONJUNCTION CANDIDATE"
    else:
        status = "SAFE"

    return {
        "closest_distance_km": minimum_distance_km,
        "tca": time_of_closest_approach,
        "status": status
    }