####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Вариант 51
# Программа для расчета двух функций в заданном диапазоне с заданным шагом,
# а также для вывода символьного графика одной из этих функций.
####################################################################################################################
import math as m

# Константы
WALL_SYMBOL = "|"  # Символ, используемый в вертикальных ограничителях
CEIL_SYMBOL = "-"  # Символ, используемый в горизонтальных ограничителях
GRAPH_WIDTH = 150  # Количество символов, используемых для вывода графика по Y

#  Блок ввода
b0, h, bn = [float(i) for i in
             input("Введите начальное значение, шаг и конечное значение аргумента через запятую с пробелом: ").split(
                 ", ")]

if b0 > bn:
    print("Некорректный ввод: начальное значение больше конечного")
    exit()

# Блок вычислений
# Инициализация переменных
max_number_width = 0  # Максимальная длина числа в таблице
max_b_width = 0  # Максимальная длина аргумента в таблице
s_max = 3.04 * b0 ** 3 - 2.89 * m.sin(5 * b0) - 1.72  # Начальные значения для максимального и минимального значений
s_min = 3.04 * b0 ** 3 - 2.89 * m.sin(5 * b0) - 1.72  # функции s2 соответственно
n_steps = int((bn - b0) / h + 1)  # Количество вычислений(шагов) функции на заданном отрезке
n_s1_neg = 0  # Количество отрицательных и положительных
n_s1_pos = 0  # значений функции s1 соответственно

for i in range(n_steps):  # Цикл для просчёта различных значений
    b = b0 + h * i
    s1 = 1.021 * b ** 3 - 3.995 * b ** 2 + 2.5
    if s1 > 0:
        n_s1_pos += 1
    elif s1 < 0:
        n_s1_neg += 1
    s2 = 3.04 * b ** 3 - 2.89 * m.sin(5 * b) - 1.72
    s_max = max(s_max, s2)  # Находим максимальное значение функции s2
    s_min = min(s2, s_min)  # Находим минимальное значение функции s2
    max_number_width = max(len(f"{b:.5g}"), len(f"{s1:.5g}"), len(f"{s2:.5g}"),
                           max_number_width)  # Находим максимальное длину числа в таблице
    max_b_width = max(len(f"{b:.5g}"), max_b_width)  # Находим максимальное длину аргумента в таблице
max_number_width += 2

# Блок вывода
print("Таблица значений:")

print(WALL_SYMBOL + CEIL_SYMBOL * (max_number_width * 3 + 2) + WALL_SYMBOL)
print(WALL_SYMBOL + "b".center(max_number_width) + WALL_SYMBOL + "s1".center(
    max_number_width) + WALL_SYMBOL + "s2".center(
    max_number_width) + WALL_SYMBOL)
print(WALL_SYMBOL + CEIL_SYMBOL * (max_number_width * 3 + 2) + WALL_SYMBOL)

# Последовательно выводим значения аргемента и функций а таблице
for i in range(n_steps):
    b = b0 + h * i
    s1 = 1.021 * b ** 3 - 3.995 * b ** 2 + 2.5
    s2 = 3.04 * b ** 3 - 2.89 * m.sin(5 * b) - 1.72
    3
    print(WALL_SYMBOL + f"{b:.5g}".center(max_number_width) + WALL_SYMBOL + f"{s1:.5g}".center(
        max_number_width) + WALL_SYMBOL + f"{s2:.5g}".center(
        max_number_width) + WALL_SYMBOL)
print(WALL_SYMBOL + CEIL_SYMBOL * (max_number_width * 3 + 2) + WALL_SYMBOL)
print()

# Отрисовка графика функции s = 3.04 * b ** 3 - 2.89 * m.sin(5 * b) - 1.72
n_marks = int(input("Введите количество засечек по y: "))
marks_dist = GRAPH_WIDTH // (n_marks - 1)  # Расстояние между началами засечек в символах
s_step = (s_max - s_min) / GRAPH_WIDTH  # Расстояние между соседними символами по Y

print((max_b_width + 1) * " ", end="")  # Отрисовываем засечки
for i in range(n_marks - 1):
    s_now = s_min + s_step * (i * marks_dist)  # Значение засечки, которую сейчас отрисовываем
    str_mark = f"{s_now:.5g}"  # Переводим его в строку

    print(str_mark, end="")
    dist_to_next_mark = marks_dist - len(str_mark)  # Количество пустых символов до начала следующей засечки
    print(" " * dist_to_next_mark, end="")
print(f"{s_min + s_step * ((i + 1) * marks_dist):.5g}")  # Последняя засечка

b_zero_pos = int(- s_min / s_step)  # Координата нулевого значения функции в символах
for i in range(n_steps):  # Отрисовывем график построчно
    b = b0 + i * h
    s = (3.04 * b ** 3 - 2.89 * m.sin(5 * b) - 1.72) - s_min
    print(f"{b:.5g}".center(max_b_width) + WALL_SYMBOL, end="")
    y = int(s / s_step)  # Координата точки графика в символах по Y
    if b_zero_pos == y or b_zero_pos < 0:  # Если нет нуля на графике, или он совпадает со значением функции,
        # то отрисовываем только точку в этой строке
        print(" " * y + "*" + " " * (GRAPH_WIDTH - y - 1))
    elif b_zero_pos < y:  # Ноль левее точки на графике
        print(" " * b_zero_pos + WALL_SYMBOL + " " * (y - b_zero_pos - 1) + "*" + " " * (GRAPH_WIDTH - y - 1))
    else:  # Ноль правее точки на графике
        print(" " * y + "*" + " " * (b_zero_pos - y - 1) + WALL_SYMBOL + " " * (GRAPH_WIDTH - b_zero_pos - 1))
print()

print(f"Количество отрицательных элементов функции s1: {n_s1_neg:.5g}")
print(f"Количество положительных элементов функции s1: {n_s1_pos:.5g}")
