def diff(x, y):
    """y' = 3x + y/2"""
    return (3 * x) + (y / 2)

def rungekutta(x0, y0, x, h):
    n = int((x - x0) / h)
    for i in range(1, n + 1):
        k1 = h * diff(x0, y0)
        k2 = h * diff(x0 + 0.5 * h, y0 + 0.5 * k1)
        k3 = h * diff(x0 + 0.5 * h, y0 + 0.5 * k2)
        k4 = h * diff(x0 + h, y0 + k3)
        y0 += (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x0 = x0 + h
    return y0

x0, y0 = 0, 1
x = 0.2
h = 0.005
print(f"y({x}) = {rungekutta(x0, y0, x, h):.5f}")