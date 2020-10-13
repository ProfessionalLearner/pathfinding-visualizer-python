from typing import Tuple
import math


def get_manhattan_distance(point_one: Tuple[int, int], point_two: Tuple[int, int], width: int, height: int) -> int:
    x1, y1 = point_one
    x2, y2 = point_two
    return abs(x1 - x2) * width + abs(y1 - y2) * height


def get_euclidean_distance(point_one: Tuple[int, int], point_two: Tuple[int, int], width: int, height: int) -> int:
    x1, y1 = point_one
    x2, y2 = point_two
    return int(math.sqrt((x1 * width - x2 * width) ** 2 + (y1 * height - y2 * height) ** 2))
