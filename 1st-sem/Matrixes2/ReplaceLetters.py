####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Дана матрица символов, заменить все гласные английские буквы на точки
####################################################################################################################
WALL_SYMB = " "
CEIL_SYMB = " "

nd, md = map(int, input("Введите через пробел количество строк и столбцов: ").split())
if md <= 0 or nd <= 0:
    print("Некорректные размеры матрицы.")
    exit()
max_elem_len = 0
D = [[0] * md for _ in range(nd)]

for i in range(nd):  # Ввод матрицы
    for j in range(md):
        D[i][j] = input(f"Введите элемент в {i + 1}-ой строке {j + 1}-ом столбе матрицы D: ")
        max_elem_len = max(len(D[i][j]), max_elem_len)
max_elem_len += 2
table_length = (max_elem_len + 1) * (md + 1)

print("Исходная матрица:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(md)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(nd):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(D[i][j]).center(max_elem_len) for j in range(md)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()


vowel = "eyuioa"  # Гласные
for i in range(nd):
    for j in range(md):
        if D[i][j].lower() in vowel:
            D[i][j] = '.'  # Замена гласной на точку


print("Модифицированная матрица:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(md)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(nd):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(D[i][j]).center(max_elem_len) for j in range(md)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()
