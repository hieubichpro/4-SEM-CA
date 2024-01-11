from getdata import *
from algorithm import *

table, n, xo = get_data_from_user("data.txt")
print("Интерполяция с помощью полинома Ньютона и Эрмита\n",
      "| n |   x   |  Ньютона   |   Эрмита   |")
print("{:^5}|{:^7}|".format(n, xo), end="")
print("{:^12}|".format(round(newton(table, xo, n), 5)), end="")
print("{:^12}|".format(round(hermit(table, xo, n), 5)), end="")