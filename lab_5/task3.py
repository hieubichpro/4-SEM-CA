from math import sqrt
import numpy as np
from matplotlib import pyplot as plt


# Определяем параметры задачи
a = 0.0
b = 1.0
ya = 1.0
yb = 3.0

N = 10
h = (b - a) / N
tol = 1e-6
max_iter = 1000


# Функция для аппроксимации второй производной
def d2y(x, y):
    return (y[x - 1] - 2 * y[x] + y[x + 1]) / (h ** 2)


# Функция для вычисления функции и ее производной в каждой точке сетки
def F(y):
    f = np.zeros(N + 1)
    f[0] = y[0] - ya
    f[N] = y[N] - yb
    for i in range(1, N):
        f[i] = d2y(i, y) - y[i] ** 3 - (i * h) ** 2
    return f


# Функция для вычисления Якобиана
def diag_mat(y):
    jac = np.zeros((N + 1, N + 1))

    jac[0][0] = 1.0
    jac[N][N] = 1.0
    for i in range(1, N):
        jac[i][i - 1] = 1.0 / (h ** 2)
        jac[i][i] = -2.0 / (h ** 2) - 3.0 * y[i] ** 2
        jac[i][i + 1] = 1.0 / (h ** 2)
    return jac


def get_vector_norm(var_seq):
    sum = 0
    for i in range(2):
        sum += var_seq[i] ** 2

    return sqrt(sum)


# Процедура нахождения решения 3-х диагональной матрицы
def three_diag(jac, f):
    n = len(jac)
    x = [0 for _ in range(0, n)]  # обнуление вектора решений

    # Прямой ход
    v = [0 for _ in range(0, n)]
    u = [0 for _ in range(0, n)]
    # для первой 0-й строки
    v[0] = jac[0][1] / (-jac[0][0])
    u[0] = (- f[0]) / (-jac[0][0])
    for i in range(1, n):  # заполняем за исключением 1-й и (n-1)-й строк матрицы
        v[i] = jac[i][i + 1] / (-jac[i][i] - jac[i][i - 1] * v[i - 1]) if i < n - 1 else 0
        u[i] = (jac[i][i - 1] * u[i - 1] - f[i]) / (-jac[i][i] - jac[i][i - 1] * v[i - 1])

    # Обратный ход
    x[n - 1] = u[n - 1]
    for i in range(n - 1, 0, -1):
        x[i - 1] = v[i - 1] * x[i] + u[i - 1]

    return x


# Функция для решения системы нелинейных уравнений методом Ньютона
def newton_three_diag(F, diag_mat, x, tol, max_iter):
    for _ in range(max_iter):
        f = F(x)
        jac = diag_mat(x)

        # решаем jac * var = -f
        # dx = get_coefs(jac, -f)

        dx = three_diag(jac, -f)

        x += dx
        if get_vector_norm(dx) < tol:
            return x
    return None


# Решаем краевую задачу

# разностная сетка
x = np.linspace(a, b, N + 1)
y = np.linspace(ya, yb, N + 1)

for i in range(N + 1):
    y[i] = ya + i * (yb - ya) / N

# решаем систему нелинейных уравнений методом ньютона
y = newton_three_diag(F, diag_mat, y, tol, max_iter)

print("x\t y")
for i in range(N + 1):
    print("{:.4f}\t {:.4f}".format(x[i], y[i]))

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
