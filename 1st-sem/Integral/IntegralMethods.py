def centered_rects(start: float, end: float, n: int, f) -> float:
    '''Вычисление определённого интеграла методом серединных прямоугольников'''
    s = 0
    dx = (end - start) / n
    for i in range(n):
        fi = f(start + dx * (i + 0.5))
        s += dx * fi
    return s


def simpson(start: float, end: float, n: int, f) -> float:
    '''Вычисление определённого интеграла методом Парабол(Симпсона)'''
    s = 0
    dx = (end - start) / n
    for i in range(0, n, 2):
        s += f(start + dx * i) + 4 * f(start + dx * (i + 1)) + f(start + dx * (i + 2))
    s *= dx / 3
    return s


def newton(start, end, primordial) -> float:
    '''Вычисление определённого интеграла по формуле Ньютона-Лейбница'''
    return primordial(end) - primordial(start)
