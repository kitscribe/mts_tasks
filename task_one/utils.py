import math


def roundup(x: [int, float]) -> int:
    """
    round up to the nearest hundreds
    :param x: value to round
    :return: rounded int
    """
    return int(math.ceil(x / 100.0)) * 100
