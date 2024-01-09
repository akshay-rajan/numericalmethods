def f(x, y):
    """dy/dx = x + y"""
    return x + y

def euler(x0, y0, xn, n):
    h = (xn - x0) / n
    print("x0\ty0\tslope\tyn")
    for i in range(n):
        slope = f(x0, y0)
        yn = y0 + (h * slope)
        print(f"{x0:.4f}\t{y0:.4f}\t{slope:.4f}\t{yn:.4f}")
        y0, x0 = yn, x0 + h
    print(f"At x = {xn:.4f}, y = {yn:.4f}")
    
x0, y0 = 0, 1
xn = 1
euler(x0, y0, xn, 10)