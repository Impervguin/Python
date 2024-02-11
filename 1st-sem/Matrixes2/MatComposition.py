####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Построчно перемножить одноразмерные матрицы A и B, сохранить результат в C, и записать в массив V
# все суммы столбцов C
####################################################################################################################
WALL_SYMB = " "
CEIL_SYMB = " "

n, m = map(int, input("Введите через пробел количество строк и столбцов в матрицах: ").split())
if m <= 0 or n <= 0:
    print("Некорректные размеры матрицы.")
    exit()
max_elem_len = 0
A = [[0] * m for _ in range(n)]
B = [[0] * m for _ in range(n)]

for i in range(n): # Ввод матрицы A
    for j in range(m):
        A[i][j] = float(input(f"Введите элемент в {i + 1}-ой строке {j + 1}-ом столбе матрицы A: "))
        max_elem_len = max(len(str(A[i][j])), max_elem_len)
for i in range(n): # Ввод матрицы B
    for j in range(m):
        B[i][j] = float(input(f"Введите элемент в {i + 1}-ой строке {j + 1}-ом столбе матрицы B: "))
        max_elem_len = max(len(str(B[i][j])), max_elem_len)


C = [[A[i][j] * B[i][j] for j in range(m)] for i in range(n)] # Считаем матрицу C как построчное произведение A и B

for i in range(n):
    for j in range(m):
        max_elem_len = max(len(str(C[i][j])), max_elem_len)

V = [sum([C[i][j] for i in range(n)]) for j in range(m)] # Суммы в каждом столбце C

max_elem_len += 2
table_length = (max_elem_len + 1) * (m + 1)


print("Матрица A:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(m)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(n):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(A[i][j]).center(max_elem_len) for j in range(m)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()

print("Матрица B:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(m)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(n):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(B[i][j]).center(max_elem_len) for j in range(m)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()

print("Матрица C:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(m)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(n):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(f'{C[i][j]:.5g}').center(max_elem_len) for j in range(m)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print("V".center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
    [str(f'{V[i]:.5g}').center(max_elem_len) for i in range(m)]) + WALL_SYMB) # Вывод массива V