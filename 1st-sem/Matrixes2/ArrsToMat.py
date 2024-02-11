####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Сформировать матрицу по двум введенным массивам как синус суммы элементов массивов
####################################################################################################################
import math as m

WALL_SYMB = " "
CEIL_SYMB = " "

nd = int(input("Введите количество элементов в списке D: "))
nf = int(input("Введите количество элементов в списке F: "))
if nd < 1 or nf < 1:
    print("Некорректное значение.")

D = [float(input(f"{i + 1}-й элемент D: ")) for i in range(nd)]  # Ввод списка
F = [float(input(f"{i + 1}-й элемент F: ")) for i in range(nf)]

A = [[m.sin(D[j] + F[k]) for k in range(nf)] for j in range(nd)]  # Построение матрицы

AV = []
for i in range(nd):  # Считаем среднее положительных элементов по каждой строке
    l = 0
    s = 0
    for j in range(nf):
        if A[i][j] > 0:
            l += 1
            s += A[i][j]
    AV.append(s / l if l != 0 else float("-inf"))
L = [sum(map(lambda x: x < AV[i], A[i])) for i in range(nd)]  # Количество элементов в каждой строке, меньшей среднего
# положительных в этой строке


max_elem_len = max(len(str(nf)), len(str(nd))) + 4  # Максимальная длина элемента
for i in range(nd):
    for j in range(nf):
        max_elem_len = max(max_elem_len, len(f"{A[i][j]:.5g}") + 4)

table_length = (max_elem_len + 1) * (nf + 1)  # Длина таблицы

# Вывод матрицы A
print("Искомая таблица:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join(
    [str(i + 1).center(max_elem_len) for i in range(nf)] + [str(el).center(max_elem_len) for el in
                                                            ["AV", "L"]]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(nd):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [(f"{elem:.5g}" if elem != float('-inf') else "-").center(max_elem_len) for elem in
         A[i] + [AV[i]] + [L[i]]]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()
