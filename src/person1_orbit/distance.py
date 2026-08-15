import numpy as np


def calculate_distance(position1, position2):
    """
    Calculate the straight-line distance between two positions.

    Positions are given in km.
    Returns distance in km.
    """
    position1 = np.array(position1)
    position2 = np.array(position2)

    distance = np.linalg.norm(position1 - position2)

    return distance