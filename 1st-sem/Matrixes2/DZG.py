####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Подсчитать кол-во элементов в каждой строке матрицы D которые превышают сумму соотв. строки матрицы Z,
# сохранить результаты в массив G, затем умножить D на максимальное значение G
####################################################################################################################
WALL_SYMB = " "
CEIL_SYMB = " "

nd, md = map(int, input("Введите через пробел количество строк и столбцов матрицы D: ").split())
nz, mz = map(int, input("Введите через пробел количество строк и столбцов матрицы Z: ").split())
if md <= 0 or nd <= 0 or nz <= 0 or mz <= 0:
    print("Некорректные размеры матрицы.")
    exit()
if nd != nz:
    print("Матрицы имеют разное кол-во строк.")
    exit()

max_elem_len = 0
D = [[0] * md for _ in range(nd)]
Z = [[0] * mz for _ in range(nz)]
for i in range(nd):  # Ввод матрицы D
    for j in range(md):
        D[i][j] = int(input(f"Введите элемент в {i + 1}-ой строке {j + 1}-ом столбе матрицы D: "))
        max_elem_len = max(len(f"{D[i][j]:.5g}"), max_elem_len)

for i in range(nz):  # Ввод матрицы Z
    for j in range(mz):
        Z[i][j] = int(input(f"Введите элемент в {i + 1}-ой строке {j + 1}-ом столбе матрицы Z: "))
        max_elem_len = max(len(f"{Z[i][j]:.5g}"), max_elem_len)

max_elem_len += 2
table_length_d = (max_elem_len + 1) * (md + 1)
table_length_z = (max_elem_len + 1) * (mz + 1)

print("Таблица D:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(md)]) + WALL_SYMB)
print(CEIL_SYMB * table_length_d)
for i in range(nd):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(D[i][j]).center(max_elem_len) for j in range(md)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length_d)
print()

print("Таблица Z:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(mz)]) + WALL_SYMB)
print(CEIL_SYMB * table_length_z)
for i in range(nd):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(Z[i][j]).center(max_elem_len) for j in range(mz)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length_z)
print()


Z_sums = [sum(row) for row in Z]  # Сумма строк Z
G = [sum(map(lambda x: x > Z_sums[i], D[i])) for i in
     range(nd)]  # Массив количества элементов, превышающих сумму элементов соответсвующей строки матрицы Z,
# в каждой строке матрицы D
max_g = max(G)
for i in range(nd):
    for j in range(md):
        D[i][j] *= max_g


print("Изменённая таблица D:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(md)]) + WALL_SYMB)
print(CEIL_SYMB * table_length_d)
for i in range(nd):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(D[i][j]).center(max_elem_len) for j in range(md)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length_d)
print()

print("Массив G:")
for (i, el) in enumerate(G):  # Вывод
    print(f"{i + 1}-й элемент: {el}")
