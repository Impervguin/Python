####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Программа для перестановки местами с максимальной и минимальной суммами
####################################################################################################################
WALL_SYMB = "#"
CEIL_SYMB = "#"

# Блок Ввода
m, n = map(int, input("Введите через пробел количество строк и стобцов матрицы: ").split())
if m <= 0 or n <= 0:
    print("Некорректный ввод")
    exit()

max_elem_len = max(len(str(m)), len(str(n))) + 4  # Максимальная ширина элемента
matrix = [[0] * m for _ in range(n)]  # Пустая матрица

for i in range(n):
    for j in range(m):
        matrix[i][j] = int(input(f"Введите элемент {i + 1}-ой строки {j + 1}-ого столбца: "))
        max_elem_len = max(max_elem_len, len(str(matrix[i][j])) + 4)

# Блок вывода исходной матрицы
table_length = (max_elem_len + 1) * (m + 1)

print("Исходная таблица:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(m)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(n):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(matrix[i][j]).center(max_elem_len) for j in range(m)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()

# Блок Решения
max_s = float("-inf")  # Максимальная сумма
min_s = float("+inf")  # Минимальная сумма
max_s_index = 0  # Индекс столбца с макс суммой
min_s_index = 0  # Индекс столбца с минимальной суммой
for j in range(m):
    s = 0  # Сумма текущего столбца
    for i in range(n):
        s += matrix[i][j]
    if s > max_s:
        max_s = s
        max_s_index = j
    if s < min_s:
        min_s = s
        min_s_index = j

if max_s == min_s:
    print("Столбец с максимальной суммой и есть столбец с минимальной суммой")
else:
    for i in range(n):
        matrix[i][max_s_index], matrix[i][min_s_index] = matrix[i][min_s_index], matrix[i][
            max_s_index]  # Меняем местами

# Блок вывода
print("Модифицированная таблица:")
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(m)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(n):
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(matrix[i][j]).center(max_elem_len) for j in range(m)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()
