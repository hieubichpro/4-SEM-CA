from math import sqrt, exp, pi


def integrand(t):
    return exp(- (t**2) / 2)


def trapezoidal_rule(f, x, n = 100):

    a, b = 0, x
    h = (b - a) / n
    sum = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        x = a + i * h
        sum += f(x)

    return h * sum


def laplace_func(x):
    integral = trapezoidal_rule(integrand, x)
    return (2 / sqrt(2 * pi)) * integral


def f(x, fx):
    return laplace_func(x) - fx


def my_half_interval_method(fx, a, b, tol = 1e-5, max_iters = 1000):
    i = 0
    c = 0

    while i < max_iters:
        c = (a + b) / 2

        if b - a < tol:
            break

        if f(c, fx) * f(a, fx) < 0:
            b = c
        else:
            a = c
        i += 1
    
    if i == max_iters:
        return None
    return c
 

def my_find_laplace(fx):
    return my_half_interval_method(fx, -10, 10)


print(my_find_laplace(0.4861))