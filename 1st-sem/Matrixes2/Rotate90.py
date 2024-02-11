####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Повернуть матрицу на 90 градусов по часовой стрелке, затем против часовой
####################################################################################################################

WALL_SYMB = " "
CEIL_SYMB = " "

n = int(input("Введите размер квадратной матрицы: "))
if n <= 0:
    print("Некорректный ввод")
    exit()

max_elem_len = len(str(n)) + 4  # Максимальная ширина элемента
matrix = [[0] * n for _ in range(n)]  # Пустая матрица

for i in range(n):  # Ввод матрицы
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

# Поворот по часовой стрелке
for i in range(n // 2):
    for j in range(i, n - i - 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[n - 1 - j][i]
        matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
        matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
        matrix[j][n - 1 - i] = temp

print("Промежуточная таблица:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(n)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(n):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(matrix[i][j]).center(max_elem_len) for j in range(n)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()

# Поворот против часовой стрелки
for i in range(n // 2):
    for j in range(i, n - i - 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][n - 1 - i]
        matrix[j][n - 1 - i] = matrix[n - 1 - i][n - 1 - j]
        matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - j][i]
        matrix[n - 1 - j][i] = temp

print("Финальная таблица:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(n)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(n):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(matrix[i][j]).center(max_elem_len) for j in range(n)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()
