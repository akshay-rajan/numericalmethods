def f(x):
    return 3 * pow(x, 2) - 10 * x + 8

def fprime(x):
    return 6 * x - 10

def newtonRaphson(x):
    """Approximate x with x - (f(x)/f'(x))"""
    
    h = f(x) / fprime(x)
    while abs(h) > 0.0001:
        h = f(x) / fprime(x)
        x -= h
        print(x)
    print("Root: " , x)

newtonRaphson(1)