from algorithm import *
from getdata import *

# Task 1
table = read_table("data.txt")
xo = 0.675
arr_n = [1, 2, 3, 4, 5]
print("Интерполяция с помощью полинома Ньютона и Эрмита\n",
      "| n |   x   |  Ньютона   |   Эрмита   |")
for i in range(len(arr_n)):
    print("{:^5}|{:^7}|".format(arr_n[i], xo), end="")
    print("{:^12}|".format(round(newton(table, xo, arr_n[i]), 5)), end="")
    print("{:^12}|".format(round(hermit(table, xo, arr_n[i]), 5)), end="")
    print("")
    
# Task 2

for i in range(len(table)):
    table[i][0], table[i][1] = table[i][1], table[i][0]
    tmp = round(1 / table[i][2], 5)
    table[i][2] = tmp

table.sort()
print(table)

print("Нахождение корни заданной функции с помощью обратной интерполяции\n",
      "| n |   y   |  Ньютон    |  Эрмита  |")
for n in range(1, 8):
    print("{:^5}|{:^7}|{:^12}|{:^12}|".format(n, 0, round(newton(table, 0, n), 5), round(hermit(table, 0, n), 5)))

# Task 3
table_1 = read_table("tab1.txt")
table_2 = read_table("tab2.txt")

for i in range(len(table_1)):
    table_1[i][0], table_1[i][1] = table_1[i][1], table_1[i][0]

y1 = []
for i in range(len(table_2)):
    y1.append(round(newton(table_1, table_2[i][0], 9), 5))

table_3 = []
for i in range(len(table_2)):
    table_3.append([round(table_2[i][1] - y1[i], 5), table_2[i][0]])

for i in range(1, 7):
    root_x = round(newton(table_3, 0, i), 3)
    root_y = round(newton(table_2, root_x, i), 3)
    print("n = ", i, " x = ", root_x, " y = ", root_y)