from math import pow


def create_f():
    """Create a polynomial by reading the degree and coefficients from the user"""

    degree = int(input("Enter the degree of the algebraic equation: "))
    coefficients = [int(input(f"Enter the coefficient of x^{degree - i}: ")) for i in range(degree + 1)]
    return lambda x: sum(coefficients[i] * pow(x, degree - i) for i in range(degree + 1))

    
def bisection():
    """Find the root of a polynomial using bisection method"""
    
    # Create the polynomial
    f = create_f()
    
    # Read the bounds
    a, b = int(input("a: ")), int(input("b: "))
    
    # Make sure f(a) and f(b) are on either sides of the x axis
    if f(a) * f(b) >= 0:
        print("Wrong Assumption of a and b!")
        return 1
    while (b - a >= 0.001):
        c = (a + b) / 2
        # If the root has been found
        if f(c) == 0:
            break
        # If a and b are of opposite signs, replace b with c
        if f(c) * f(a) < 0:
            b = c
        # Otherwise replace a with c
        else:
            a = c
    return c

print(bisection())
            
