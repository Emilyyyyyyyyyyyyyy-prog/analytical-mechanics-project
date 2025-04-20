import numpy as np
import matplotlib.pyplot as plt


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


# Зададим единичный кватернион
q = np.array([0, 0, 0, 1])

w = np.array([5, 1, 1])  # Зададим угловую скорость
y0 = np.concatenate([q, w])  # Вектор состояния y

m = 1
R = 1
A = 2 / 3 * m * R ** 2
B = 2 / 3 * m * R ** 2
C = 1 / 3 * m * R ** 2

# Запускаем метод Рунге-Кутты и смотрим, как меняется угловая скорость при движении твердого тела
y = rk4(y0, 0, A, B, C)
w = [yi[4:] for yi in y][:-2]
t = np.arange(0, 10, 0.1)
plt.scatter(t, [wi[0] for wi in w], label='w1')
plt.scatter(t, [wi[1] for wi in w], label='w2')
plt.scatter(t, [wi[2] for wi in w], label='w3')
plt.legend()
plt.grid()
plt.xlabel('t')
plt.ylabel('w')
plt.title('Зависимость угловой скорости от времени')
plt.savefig('graph1.png')
plt.show()
