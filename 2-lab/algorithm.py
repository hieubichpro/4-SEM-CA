def find_range(arr_x, x):
    res = 0
    
    for i in range(len(arr_x)):
        if x < arr_x[i]:
            res = i
            break
        
    return res

def spline(x, y, st, end, xo):
    n = len(x)

    h = [0 if not i else x[i] - x[i - 1] for i in range(n)]
    
    F = [0 if i < 2 else 3 * ((y[i] - y[i - 1]) / h[i] - (y[i - 1] - y[i - 2]) / h[i - 1]) for i in range(n)]

    # прямой ход
    ksi = [0 for i in range(n + 1)]
    eta = [st/2 for i in range(n + 1)]
    for i in range(2, n):
        ksi[i + 1] = -h[i] / (2*(h[i-1] + h[i]) + h[i-1] * ksi[i])
        eta[i + 1] = (F[i] - h[i-1]*eta[i]) / (h[i-1] * ksi[i] + 2*(h[i-1] + h[i]))

    # обратный ход
    c = [0 for i in range(n + 1)]
    c[1] = st/2
    c[n] = end/2
    for i in range(n - 2, -1, -1):
        c[i] = ksi[i + 1] * c[i + 1] + eta[i + 1]


    a = [0 if i < 1 else y[i-1] for i in range(n)]
    b = [0 if i < 1 else (y[i] - y[i - 1]) / h[i] - h[i] / 3 * (c[i + 1] + 2 * c[i]) for i in range(n)]
    d = [0 if i < 1 else (c[i + 1] - c[i]) / (3 * h[i]) for i in range(n)]

    idx = find_range(x, xo)
    
    x1 = xo - x[idx - 1]
    x2 = x1 * x1
    x3 = x1 * x1 * x1
    res = a[idx] + b[idx]*x1 + c[idx]*x2 + d[idx]*x3
    
    return res
    
        
        
    
        