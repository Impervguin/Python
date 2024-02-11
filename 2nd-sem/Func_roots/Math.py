from sympy import *
DELTA=0.1


def find_roots(func, left, right, step, max_iter, eps):
    res = []
    n = 1
    while left + step < right:
        root = secant_method(func, left, left + step, max_iter, eps)
        res.append({
            "value": root[1],
            "num": n,
            "iter": root[2],
            "error": root[0],
            "error_t": root[3],
            "left":left,
            "right":left + step,
            "f_value":func(root[1])
        })
        n += 1
        left += step
    root = secant_method(func, left, right, max_iter, eps)
    res.append({
            "value": root[1],
            "num": n,
            "iter": root[2],
            "error": root[0],
            "error_t": root[3],
            "left": left,
            "right": right,
            "f_value": func(root[1])
        })
    return res


def secant_method(func, left, right, max_iter, eps):
    maxx = right
    minn = left
    if abs(func(left)) < eps:
        return (0, left, 0, "")
    if func(left) * func(right) < 0:
        prev = right
        d_f_prev = (func(prev) - func(prev - DELTA)) / DELTA

        f_prev = func(prev)
        n = 1
        if d_f_prev == 0:
            return (2, 0, n, "Деление на ноль")
        now = prev - func(prev) / d_f_prev

        f_now = func(now)

        while abs(f_now) > eps and n < max_iter:
            if (f_now - f_prev) == 0:
                return (2, now, n, "Деление на ноль")
            new = now - (f_now / (f_now - f_prev) * (now - prev))
            prev, f_prev = now, f_now
            now, f_now = new, func(new)
            n += 1
        if minn < now and now < maxx:
            return (0, now, n, "")
        else:
            return (1, 0, 0, "Нет корня")
    else:
        return (1, 0, 0, "Нет корня")

def find_extr(func_t, left, right, step, max_iter, eps):
    x = Symbol('x')

    y = eval(func_t)
    d = y.diff(x)

    def d_f(x):
        return eval(str(d))
    
    return find_roots(d_f, left, right, step, max_iter, eps)

def find_inflection(func_t, left, right, step, max_iter, eps):
    x = Symbol('x')

    y = eval(func_t)
    d = y.diff(x)

    return find_extr(str(d), left, right, step, max_iter, eps)