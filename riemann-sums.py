import math
import time


def left_endpoint_riemann_sum():
    N = 10000000

    delta_x = (1 - 0) / N
    x = 0
    pi = 0

    while x < 1:
        f_x = math.sqrt(1 - math.pow(x, 2))
        pi += f_x * delta_x
        x += delta_x
    pi = 4 * pi

    print("Estimate: " + str(pi))
    print("Actual:   " + str(math.pi))


def midpoint_riemann_sum():
    N = 1000000000

    delta_x = (1 - 0) / N
    x = 0
    pi = 0
    start = time.time()

    while x < (1-delta_x):
        x_next = x + delta_x
        x_mid = (x_next + x) / 2
        f_x = math.sqrt(1 - math.pow(x_mid, 2))
        pi += f_x * delta_x
        x += delta_x

    pi = 4 * pi
    end = time.time()
    print(end - start)
    print("Estimate: " + str(pi))
    print("Actual:   " + str(math.pi))


if __name__ == '__main__':
    left_endpoint_riemann_sum()
