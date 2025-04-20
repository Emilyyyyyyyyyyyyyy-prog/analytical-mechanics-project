import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from scipy.integrate import odeint

# Параметры системы
m = 1.0  # масса маятника (кг)
L = 1.0  # длина маятника (м)
g = 9.81  # ускорение свободного падения (м/с²)
A = 0.1  # амплитуда колебаний подвеса (м)
omega = 20.0  # частота колебаний подвеса (рад/с)

# Время симуляции
t_max = 10.0  # время симуляции (с)
dt = 0.01  # шаг времени (с)
t = np.arange(0, t_max, dt)

# Начальные условия (почти вертикальное положение)
theta0 = np.pi - 0.1  # начальный угол (рад)
theta_dot0 = 0.0  # начальная угловая скорость (рад/с)
y0 = [theta0, theta_dot0]


# Функция для вычисления производных
def derivatives(y, t, m, L, g, A, omega):
    theta, theta_dot = y
    theta_ddot = (g + A * omega ** 2 * np.cos(omega * t)) * np.sin(theta) / L
    return [theta_dot, theta_ddot]


# Решение системы ОДУ
sol = odeint(derivatives, y0, t, args=(m, L, g, A, omega))
theta = sol[:, 0]

# Положение маятника
x = L * np.sin(theta)
y = -L * np.cos(theta) + A * np.cos(omega * t)

# Создание фигуры и осей
fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.25)  # Оставляем место для слайдеров

# Оси для слайдеров
ax_A = plt.axes([0.25, 0.1, 0.65, 0.03])
ax_omega = plt.axes([0.25, 0.05, 0.65, 0.03])

# Слайдеры
slider_A = Slider(ax_A, 'Амплитуда (A)', 0.01, 0.5, valinit=A)
slider_omega = Slider(ax_omega, 'Частота (ω)', 5, 50, valinit=omega)

# Инициализация анимации
line, = ax.plot([], [], 'o-', lw=2)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
ax.set_xlim(-1.5 * L, 1.5 * L)
ax.set_ylim(-1.5 * L, 1.5 * L)
ax.set_aspect('equal')
ax.grid()


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def update_animation(frame):
    x_pivot = 0
    y_pivot = A * np.cos(omega * t[frame])
    x_mass = x_pivot + x[frame]
    y_mass = y_pivot + y[frame]
    line.set_data([x_pivot, x_mass], [y_pivot, y_mass])
    time_text.set_text(f'Время: {t[frame]:.2f} с\nУгол: {theta[frame]:.2f} рад')
    return line, time_text


# Функция обновления параметров при изменении слайдеров
def update_params(val):
    global A, omega, sol, theta, x, y
    A = slider_A.val
    omega = slider_omega.val
    sol = odeint(derivatives, y0, t, args=(m, L, g, A, omega))
    theta = sol[:, 0]
    x = L * np.sin(theta)
    y = -L * np.cos(theta) + A * np.cos(omega * t)
    ani.event_source.stop()  # Останавливаем анимацию для перезапуска
    ani.event_source.start()


# Привязка слайдеров к функции обновления
slider_A.on_changed(update_params)
slider_omega.on_changed(update_params)

# Запуск анимации
ani = FuncAnimation(fig, update_animation, frames=len(t), init_func=init, blit=True, interval=dt * 1000)
# ani.save('fluct.gif', writer='pillow')

plt.xlabel('x (м)')
plt.ylabel('y (м)')
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(t, theta, label='Угол θ(t) [рад]', color='blue')
plt.axhline(np.pi, color='red', linestyle='--', label='Верхнее положение равновесия')
plt.xlabel('Время (с)')
plt.ylabel('θ (рад)')
plt.title('Зависимость угла отклонения от времени')
plt.legend()
plt.grid()
plt.savefig('1.png')
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(theta, sol[:, 1], color='purple')
plt.xlabel('θ (рад)')
plt.ylabel('dθ/dt (рад/с)')
plt.title('Фазовый портрет маятника Капицы')
plt.grid()
plt.savefig('2.png')
plt.show()

# Построение графика y(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=1.5, label='Траектория маятника')
plt.scatter(x[0], y[0], color='red', label='Начальное положение')
# plt.scatter(x[-1], y[-1], color='green', label='Конечное положение')
plt.xlabel('x (м)', fontsize=12)
plt.ylabel('y (м)', fontsize=12)
plt.title('Траектория маятника Капицы: y(x)', fontsize=14)
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.savefig('3.png')
plt.show()