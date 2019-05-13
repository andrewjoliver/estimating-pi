import math
import time


def gregory_leibinz():
    pi = 0
    start = time.time()
    for x in range(0, 1000000000):
        numerator = math.pow(-1, x) * math.pow(1, 2*x+1)
        denominator = 2*x + 1
        pi += numerator/denominator
    end = time.time()
    pi = pi * 4
    print(end - start)
    print("Estimate: " + str(pi))
    print("Actual:   " + str(math.pi))


def machin():
    num_iterations = 6

    arc_tan_1_239 = arc_tan(1/239, num_iterations)
    arc_tan_1_5 = arc_tan(1/5, num_iterations)

    pi = 4 * (4*arc_tan_1_5 - arc_tan_1_239)

    print("Estimate: " + str(pi))
    print("Actual:   " + str(math.pi))


def arc_tan(x, iterations):
    arc_tan_of_x = 0
    for z in range(0, iterations):
        numerator = math.pow(-1, z) * math.pow(x, 2 * z + 1)
        denominator = 2 * z + 1
        arc_tan_of_x += numerator / denominator
    return arc_tan_of_x


if __name__ == "__main__":
    machin()