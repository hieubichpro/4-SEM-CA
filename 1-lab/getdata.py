import math as m

def read_table(fname):
    table = []

    with open(fname, "r") as f:
        table = []
        while True:
            line = f.readline().strip()
            if (len(line)):
                table.append([float(x) for x in line.split()])
            else:
                break
    
    return table

def enter_x():
    print("Введите значение x, по которому вычисляется y : ", end = "")
    while True:
        try:
            val = float(input())
            break
        except:
            print("Ввод некорректно! x должно быть числом")
    return val

def enter_n(table):
    print("Введите степень n аппроксимирующих полиномов Ньютона и Эрмита: ", end = "")
    flag = 1
    while flag:
        try:
            val = int(input())
            if val < 0 or val > (len(table) - 1):
                print("n должно быть в интервале [{} , {}]".format(0, len(table) - 1))
            else:
                flag = 0
        except:
            print("Ввод некорректно! n должно быть целым") 
    return val

def get_data_from_user(fname):
    table = read_table(fname)
    table.sort()
    x = enter_x()
    n = enter_n(table)
    return table, n, x