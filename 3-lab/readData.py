from polynom import zIndexData, yIndexData, xIndexData, matrixIndexData, infinity
from numpy import linspace

EPS = 1e-6


# сама функция для генерации таблицы многомерной интерполяции
def f(x, y, z):
    if abs(x + y) < EPS:
        return infinity
    return 1 / (x + y) - z

    # if abs(x - y - z) < EPS:
    #     return infinity
    # return x**2 / (x - y - z)

    # if abs(x - y) < EPS:
    #     return infinity
    # return (1 + z) / (x - y)

    #return x**2 + y**2 + z**3

def readTable(filename):
    dataTable = [[], [], [], [[]]]
    file = open(filename)
    flagaddx = False
    flagaddy = False
    zIndex = 0
    yIndex = 0
    for line in file.readlines():
        row = line.split("\n")[0].split("\t")

        if "z=" in row[0]:
            zStr = row[0].split("z=")
            dataTable[zIndexData].append(float(zStr[1]))
        elif "y\\x" in row[0]:
            if flagaddx:
                continue
            for i in range(1, len(row)):
                dataTable[xIndexData].append(float(row[i]))
            flagaddx = True
        else:
            if "end" in row[0]:
                continue
            if not row[0].isdigit():
                zIndex += 1
                dataTable[matrixIndexData].append([])
                yIndex = 0
                flagaddy = True
                continue

            if not flagaddy:
                dataTable[yIndexData].append(float(row[0]))

            dataTable[matrixIndexData][zIndex].append([])
            for i in range(1, len(row)):
                dataTable[matrixIndexData][zIndex][yIndex].append(float(row[i]))
            yIndex += 1

    file.close()
    return dataTable


# красивый вывод и точка
def printTable(dataTable):

    for k in range(len(dataTable[zIndexData])):
        print("z =", dataTable[zIndexData][k])
        print(("+" + "-" * 10) * (len(dataTable[xIndexData]) + 1) + "+")
        print("| {:^8s}".format("Y / X"), end=" ")
        for i in range(len(dataTable[xIndexData])):
            print("| {:^8.2f}".format(dataTable[xIndexData][i]), end=" ")
        print("|")
        print(("+" + "-" * 10) * (len(dataTable[xIndexData]) + 1) + "+")
        for i in range(len(dataTable[matrixIndexData][k])):
            print("| {:^8.3f}".format(dataTable[yIndexData][i]), end=" ")
            for j in range(len(dataTable[matrixIndexData][zIndexData][i])):
                if dataTable[matrixIndexData][k][i][j] == infinity:
                    print("| {:^8s}".format("inf"), end=" ")
                else:
                    print("| {:^8.3f}".format(dataTable[matrixIndexData][k][i][j]), end=" ")
            print("|")
        print(("+" + "-" * 10) * (len(dataTable[xIndexData]) + 1) + "+")