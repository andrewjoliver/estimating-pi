import random
import math


def monte_carlo_estimation():
    area_circle = 1
    area_square = 1
    pi = 0

    for z in range(0, 1000000000):
        x = random.uniform(0, 2)
        y = random.uniform(0, 2)
        in_circle = math.pow((x-1), 2) + math.pow((y-1), 2) <= 1
        if in_circle:
            area_circle += 1
        area_square += 1
        pi = 4 * (area_circle / area_square)

    print("Estimate: " + str(pi))


if __name__ == '__main__':
    monte_carlo_estimation()
