# Трапецией sinx на [a, b] с числом разбиений n
from math import sin, cos


def f(x):
    return sin(x)


def primordial_f(x):
    return -cos(x)


def trapez(start, end, n, f):
    dx = (end - start) / n
    s = 0
    for i in range(n):
        s += (f(start + dx * i) + f(start + dx * (i + 1))) / 2 * dx
    return s


def newton(start, end, prim_f):
    return prim_f(end) - prim_f(start)


st = float(input("Введите начало отрезка интегрирования: "))
ed = float(input("Введите конец отрезка интегрирования: "))
if st > ed:
    print("Некорректные значения.")
    exit()
n = int(input("Введите количество отрезков интегрирования: "))
if n <= 0:
    print("Некорректные значения.")
    exit()

print(f"Интеграл по методу трапеций: {trapez(st, ed, n, f)}")
print(f"Точный интеграл по формуле Ньютона-Лейбница: {newton(st, ed, primordial_f)}")
