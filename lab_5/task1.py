from math import sqrt
import numpy as np

VAR_NUM = 3


def Gauss_method(jac, f):
    n = len(f)
    for i in range(n):
        # Приведение к верхнетреугольному виду
        for k in range(i + 1, n):
            c = -jac[k][i] / jac[i][i]
            for j in range(i, n):
                if i == j:
                    jac[k][j] = 0
                else:
                    jac[k][j] += c * jac[i][j]
            f[k] += c * f[i]

    # Обратный ход метода Гаусса
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = f[i]
        for j in range(i + 1, n):
            x[i] -= jac[i][j] * x[j]
        x[i] /= jac[i][i]

    return x


def equations(var):
    return np.array([var[0] ** 2 + var[1] ** 2 + var[2] ** 2 - 1,
                     2 * var[0] ** 2 + var[1] ** 2 - 4 * var[2],
                     3 * var[0] ** 2 - 4 * var[1] + var[2] ** 2])


def jacobian(var):
    return np.array([[2 * var[0], 2 * var[1], 2 * var[2]],
                     [4 * var[0], 2 * var[1], -4],
                     [6 * var[0], -4, 2 * var[2]]])


def get_vector_norm(var_seq):
    sum = 0
    for i in range(VAR_NUM):
        sum += var_seq[i] ** 2

    return sqrt(sum)


def newton_system(equations, jacobian, var0, tol = 1e-9, max_iter = 1000):
    var = var0.copy()
    for _ in range(max_iter):
        fx = equations(var)
        J = jacobian(var)

        # решается матрица системы линейных уравнений
        # вычисление поправки к текущему приближению
        dx = Gauss_method(J, -fx)

        var += dx
        if get_vector_norm(dx) < tol:
            return var
    raise ValueError("Failed to converge after {} iterations".format(max_iter))


x0 = np.array([0.5, 0.5, 0.5])
result = newton_system(equations, jacobian, x0)


print("Solution:")
print("x = {:.4f}".format(result[0]))
print("y = {:.4f}".format(result[1]))
print("z = {:.4f}".format(result[2]))
