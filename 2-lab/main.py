from data import *
from algorithm import *
from newton import *

table = read_table("data.txt")
print_table(table)

x = [table[i][0] for i in range(len(table))]
y = [table[i][1] for i in range(len(table))]

xo = float(input("Введите x, по которому вы хотите вычислить y: "))
print("Вычисление полиномом Ньютона")
print("При x = {:.6f}, y = {:.6f}".format(xo, newton(table, xo, 3)))

print("\nП 2.1: вторые производные равна нулю")
print("При x = {:.6f}, y = {:.6f}".format(xo, spline(x, y,0, 0, xo)))

f_2_xo = find_newton_second(table, x[0], 3)
f_2_xn = find_newton_second(table, x[len(x) - 1], 3)

print("\nП 2.2: Вторая производная равна нулю при x = x_o, а на другой по прежнему")
print("При x = {:.6f}, y = {:.6f}".format(xo, spline(x, y, f_2_xo, 0, xo)))

print("\nП 2.3: На обеих границах вторая производная равна второй производной полинома Ньютона третьей степени ")
print("При x = {:.6f}, y = {:.6f}".format(xo, spline(x, y, f_2_xo, f_2_xn, xo)))