####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Программа для нахождения минимального элемента под побочной диагонолью квадратной матрицы и максимального над главной
# диагональю
####################################################################################################################
WALL_SYMB = "#"
CEIL_SYMB = "#"

# Блок Ввода
n = int(input("Введите размер квадратной матрицы: "))
if n <= 0:
    print("Некорректный ввод")
    exit()

max_elem_len = len(str(n)) + 4  # Максимальная ширина элемента
matrix = [[0] * n for _ in range(n)]  # Пустая матрица

for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input(f"Введите элемент {i + 1}-ой строки {j + 1}-ого столбца: "))
        max_elem_len = max(max_elem_len, len(str(matrix[i][j])) + 4)

# Блок вывода исходной матрицы
table_length = (max_elem_len + 1) * (n + 1)

print("Исходная таблица:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(n)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(n):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(matrix[i][j]).center(max_elem_len) for j in range(n)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()

# Блок Решения
for i in range(1, n):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Блок Вывода
print("Модифицированная таблица:")
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len)for i in range(n)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(n):
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join([str(matrix[i][j]).center(max_elem_len) for j in range(n)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()
