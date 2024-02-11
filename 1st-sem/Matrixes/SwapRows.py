####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Программа для перестановки местами строк с максимальным количеством отрицательных элементов и минимальным
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
max_n = 0  # Наибольшее кол-во отрицательных
min_n = m  # Наименьшее кол-во отрицательных
max_n_index = 0  # Индекс строки с наибольшим кол-вом отрицательных
min_n_index = 0  # Индекс строки с наименьшим кол-вом отрицательных
for i in range(n):
    now = 0  # Сколько в данной строке отрицательных
    for j in range(m):
        if matrix[i][j] < 0:
            now += 1
    if now > max_n:
        max_n = now
        max_n_index = i
    if 0 < now < min_n:
        min_n = now
        min_n_index = now

if max_n == 0:  # Ни разу не изменилась
    print("Матрица не имеет отрицательных элементов")
elif max_n == min_n:
    print("Строка, содержащая максимальное количество отрицательных элементов, имеет столько же отрицательных элементов"
          ", сколько и строка, содержащая минимальное количество отрицательных элементов")
else:
    matrix[max_n_index], matrix[min_n_index] = matrix[min_n_index], matrix[max_n_index]  # Меняем местами

# Блок вывода
print("Модифицированная таблица:")
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(m)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(n):
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(matrix[i][j]).center(max_elem_len) for j in range(m)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()
