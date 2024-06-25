import math                 # to use exp
from decimal import *       # to work with float values correctly

# Not using decimal 1.1 + 1.2 = 2.3
# Using decimal 1.1 + 1.2 = 2.300000000000000044408920985


def f(x):
    # ℯ^(x)-x^(2)+3x-2
    x = Decimal(x)
    return Decimal(math.exp(x)) - x * x + 3 * x - 2     # function


def bisection(a, b, Niter, TOL):
    if f(a) * f(b) > 0:             # law of signs
        return False

    if f(a) == 0:
        return a, 0
    elif f(b) == 0:
        return b, 0

    for iteration in range(1, Niter+1):

        x: Decimal = (Decimal(a) + Decimal(b)) / 2

        if f(x) == 0 or abs(b - a) <= TOL:
            return float(x), iteration

        if f(x) * f(a) < 0:
            b = x
        else:
            a = x

    return False


print(bisection(-1, 2, 100, 0.00001))

# result 2 and TOL 0.01
# real result between 2.01 and 1.09
