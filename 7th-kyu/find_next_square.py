import math


def find_next_square(sq):
    n = math.sqrt(sq)

    if n % 1 == 0:
        next_n = n + 1
        return int(next_n ** 2)

    return -1
