from typing import List, Tuple
import numpy as np


R = 1/np.sqrt(np.pi)
POINTS = {
    0.2: 10,
    0.6: 5,
    1.: 1
} # do 20% od środka 10 punktów, 60% 5 punktów itd


def random_coordinates(low=-0.5, high=0.5) -> Tuple[float, float]:
    return np.random.uniform(low, high), np.random.uniform(low, high)

def count_points(sample, radius: float) -> int:
    for key in sorted(POINTS.keys()):
        if sample <= key * radius:
            return POINTS[key]
    return 0

def zad1(num: int, low=-0.5, high=0.5, radius=0.5) -> List[float]:
    results = []
    for _ in range(num):
        x, y = random_coordinates(low, high)
        results.append(count_points(np.sqrt(x**2 + y**2), radius))
    return results

def zad2(num: int, low=0, high=R, radius=0.5) -> List[float]:
    results = []
    for _ in range(num):
        results.append(count_points(np.random.uniform(low, high), radius))
    return results
