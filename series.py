import math
import decimal


def madhava_leibniz():
    decimal.getcontext().prec = 50
    sqrt_12 = math.sqrt(12)
    pi = 0

    for k in range(0, 32):
        numerator = math.pow(-3, -k)
        denominator = (2*k + 1)
        pi += numerator / denominator

    pi = sqrt_12 * pi
    print("Estimate: " + str(decimal.Decimal(pi)))
    print("Actual:   " + str(math.pi))


def chudnovsky():
    pi = 0

    for k in range(0, 15):
        numerator = math.pow(-1, k % 2) * math.factorial(6*k) * (13591409 + 545140134*k)
        denominator = math.factorial(3*k) * math.pow(math.factorial(k), 3) * math.pow(640320, 3*k+3/2)
        pi += numerator / denominator
    pi = 12 * pi
    pi = 1/pi
    print("Estimate: " + str(pi))
    print("Actual:   " + str(math.pi))


if __name__ == '__main__':
    chudnovsky()
