import math


def f(x) :
    """Return e^x - 1"""
    return x * math.exp(x) - 1

def g(x):
    """Return the derivative of f(x)"""
    return math.exp(-x)

def iteration(x0):
    step = 1
    condition = True
    while condition:
        x1 = g(x0)
        print(f"x1: {x1:0.8f}, f(x1): {f(x1):0.8f}")
        x0 = x1
        step = step + 1
        if step > 20:
            break
        condition = abs(f(x1)) > 0

iteration(1)