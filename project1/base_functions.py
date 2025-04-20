import numpy as np


def f(t, y, A, B, C):
    ans = np.zeros(7)
    ans[0] = -0.5 * (y[1] * y[4] + y[2] * y[5] + y[3] * y[6])
    ans[1] = 0.5 * (y[0] * y[4] - y[3] * y[5] + y[2] * y[6])
    ans[2] = 0.5 * (y[3] * y[4] + y[0] * y[5] - y[1] * y[6])
    ans[3] = 0.5 * (-y[2] * y[4] + y[1] * y[5] + y[0] * y[6])
    ans[4] = y[5] * y[6] * (B / C - C / B)
    ans[5] = y[4] * y[6] * (C / A - A / C)
    ans[6] = y[4] * y[5] * (A / B - B / A)
    return ans


def rk4(y0, t0, A, B, C):  # метод Рунге-Кутты 4го порядка
    tn = 10  # предел интегрирования
    h = 0.1  # величина шага по сетке t
    t = t0
    y = y0
    a = []
    a.append(y0)
    while t <= tn:
        k1 = f(t, y, A, B, C)
        k2 = f(t + h / 2, y + k1 / 2, A, B, C)
        k3 = f(t + h / 2, y + k2 / 2, A, B, C)
        k4 = f(t + h, y + h * k3, A, B, C)
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
        t += h
        a.append(y)
    return a
