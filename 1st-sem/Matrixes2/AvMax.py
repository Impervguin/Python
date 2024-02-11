####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение.
####################################################################################################################
WALL_SYMB = " "
CEIL_SYMB = " "

nd, md = map(int, input("Введите через пробел количество строк и столбцов матрицы D: ").split())
nl = int(input("Введите размер массива I: "))
if md <= 0 or nd <= 0 or nl <= 0:
    print("Некорректные размеры матрицы или массива.")
    exit()
max_elem_len = 0
D = [[0] * md for _ in range(nd)]

for i in range(nd):  # Ввод матрицы
    for j in range(md):
        D[i][j] = int(input(f"Введите элемент в {i + 1}-ой строке {j + 1}-ом столбе матрицы D: "))
        max_elem_len = max(len(f"{D[i][j]:.5g}"), max_elem_len)
max_elem_len += 2
table_length = (max_elem_len + 1) * (md + 1)


l = [int(input(f"{i + 1}-й элемент: ")) for i in range(nl)]  # Ввод массива
R = [0] * nl
for i in range(nl):  # Заполняем массив R по условию
    if l[i] - 1 > nd:
        print(f"В массиве есть номер превышающий количество строк в матрице.")
        exit()
    R[i] = max(D[l[i] - 1])
Av_R = sum(R) / nl  # Среднее массива R


print("Таблица D:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(md)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(nd):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(D[i][j]).center(max_elem_len) for j in range(md)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()

print("Массив l:")
for (i, el) in enumerate(l):  # Вывод
    print(f"{i + 1}-й элемент: {el}")
print()

print("Массив R:")
for (i, el) in enumerate(R):  # Вывод
    print(f"{i + 1}-й элемент: {el}")
print()

print(f"Среднее арифметическое элементов R: {Av_R:.5g}")
