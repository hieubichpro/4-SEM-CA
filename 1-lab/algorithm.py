def find_st_end(table, n, xo):
    x = [table[i][0] for i in range(len(table))]
    if xo < x[0]:
        return 0, n
    elif xo > x[-1]:
        return len(table) - 1 - n, len(table) - 1
    else:
        i = 0
        while x[i] < xo:
            i += 1
        st = i - n // 2 - 1
        end = i + n // 2 + (n % 2) - 1
        if end > len(x) - 1:
            st -= end - len(x) + 1
            end = len(x) - 1
        elif st < 0:
            end += -st
            st = 0
        return st, end
            

def diff_newton(x, y, n):
    L = []
    L.append(y)

    for i in range(n):
        curr_col = L[i]
        new_col = []
        for j in range(len(curr_col) - 1):
            new_elem = round((curr_col[j + 1] - curr_col[j]) / (x[j + i + 1] - x[j]), 5)
            new_col.append(new_elem)
        L.append(new_col)
    return L

def get_value(x, diff, xo):
    res = 0
    for i in range(len(diff)):
        term = diff[i][0]
        for j in range(i):
            term *= (xo - x[j])
        res += term
    return res

def newton(table, xo, n):
    st, end = find_st_end(table, n, xo)
    x = [table[i][0] for i in range(st, end + 1)]
    y = [table[i][1] for i in range(st, end + 1)]
    d = diff_newton(x, y, n)
    # print(d)
    return get_value(x, d, xo)

def diff_hermite(x, y, y1, n):
    L = []
    L.append(y)
    for i in range(n):
        curr_col = L[i]
        new_col = []
        for j in range(len(curr_col) - 1):
            if (x[j] == x[j + i + 1]):
                new_elem = y1[j // 2]
            else:
                new_elem = round((curr_col[j + 1] - curr_col[j]) / (x[j + i + 1] - x[j]), 5)
            new_col.append(new_elem)
        L.append(new_col)
    return L

def hermit(table, xo, n):
    st, end = find_st_end(table, n // 2, xo)
    table = table[st : end + 1]
    x = []
    y = []
    y1 = []
    for i in range (len(table)):
        for j in range(2):
            x.append(table[i][0])
            y.append(table[i][1])
        y1.append(table[i][2])
    if n / 2 == 1:
        x.pop()
        y.pop()
    d = diff_hermite(x, y, y1, n)
    # print("hermit tab", d)
    return get_value(x, d, xo)
    
    



