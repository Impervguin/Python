####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Программа для сравнения точности таких методов расчёта определённых интегралов, как метод серединных прямоугольников
# и метод парабол
####################################################################################################################


from IntegralMethods import newton, simpson, centered_rects
from Sort.PrintMatrix import print_matrix
from Inputs import pos_int_input, float_input


def f(x):
    return 4 * x ** 3


def primordial_f(x):
    return x ** 4

EPS = 0.0000001

# Блок ввода
while True:
    st = float_input("Введите начало отрезка интегрирования: ")
    ed = float_input("Введите конец отрезка интегрирования: ")
    if st >= ed:
        print("Начало не может быть больше конца.")
        continue
    break
n1 = pos_int_input("Введите первое количество участков разбиения: ", "Количество разбиений не может быть отрицательно.")
n2 = pos_int_input("Введите первое количество участков разбиения: ", "Количество разбиений не может быть отрицательно.")

# Данный для вывода таблицы
foot = ["Серединных прямоугольников", "Парабол"]
head = [n1, n2]

# Расчет интегралов
l_s1 = simpson(st, ed, n1, f) if n1 % 2 == 0 else float("+inf")
l_s2 = simpson(st, ed, n2, f) if n2 % 2 == 0 else float("+inf")
l_r1 = centered_rects(st, ed, n1, f)
l_r2 = centered_rects(st, ed, n2, f)
accurate_int = newton(st, ed, primordial_f)

# Вывод таблицы значений интегралов
mat = [
    [f"{l_r1:.5g}", f"{l_r2:.5g}"],
    [f"{l_s1:.5g}" if l_s1 != float('+inf') else "-", f"{l_s2:.5g}" if l_s2 != float('+inf') else "-"]
]
print_matrix(mat, head=head, foot=foot, name="Методы Интегральных вычислений")
print(f"Точное значение интеграла по формул Ньютона-Лейбница: {accurate_int:.5g}")

# Расчёт абсолютной погрешности методов
e_s1 = abs(accurate_int - l_s1)
e_s2 = abs(accurate_int - l_s2)
e_r1 = abs(accurate_int - l_r1)
e_r2 = abs(accurate_int - l_r2)

# Расчет относительной погрешности
if accurate_int != 0:
    re_s1 = abs(e_s1 / accurate_int * 100)
    re_s2 = abs(e_s2 / accurate_int * 100)
    re_r1 = abs(e_r1 / accurate_int * 100)
    re_r2 = abs(e_r2 / accurate_int * 100)

    e_mat = [
        [f"{e_r1:.5g}, {re_r1:.5g}%", f"{e_r2:.5g}, {re_r2:.5g}%"],
        [f"{e_s1:.5g}, {re_s1:.5g}%" if e_s1 != float('+inf') else "-", f"{e_s2:.5g}, {re_s2:.5g}%" if e_s2 != float('+inf') else "-"]
    ]
else:
    e_mat = [
        [f"{e_r1:.5g}, -", f"{e_r2:.5g}, -"],
        [f"{e_s1:.5g}, -", f"{e_s2:.5g}, -"]
    ]
# Вывод таблицы погрешности
print_matrix(e_mat, foot=foot, head=head, name="Погрешности методов")
if abs(min(e_r1, e_r2) - min(e_s1, e_s2)) < EPS:
    print("Методы показывают одинаковую точность.")
    exit()
elif min(e_r1, e_r2) > min(e_s1, e_s2):
    print("Метод симпсона оказался точнее при заданных параметрах.")
    simpson_better = True  # Флаг, показывающий более точный метод
else:
    print("Метод срединных прямоугольников оказался точнее при заданных параметрах.")
    simpson_better = False
# Ввод
while True:
    eps = float_input("Введите точность, до которой нужно довести менее точный метод: ")
    if eps <= 0:
        print("Точность не может быть меньше нуля.")
        continue
    break
        
max_it = pos_int_input("Введите максимальное количество разбиений: ", "Количество итераций не может быть меньше нуля.")

# Поиск подходящего числа разбиений
i = 1 if simpson_better else 2
while i <= max_it:
    integ = centered_rects(st, ed, i, f) if simpson_better else simpson(st, ed, i, f)
    integ2 = centered_rects(st, ed, 2 * i, f) if simpson_better else simpson(st, ed, 2 * i, f)
    if abs(integ - integ2) < eps:
        break
    i *= 2
else:
    print(f"Не удалось достигнуть заданной точности при максимуме в {max_it} разбиений")
    exit()
print(f"{'Метод серединных прямоуольников' if simpson_better else 'Метод парабол'}"
      f" достигает нужной точности при количестве разбиений в {i}")
