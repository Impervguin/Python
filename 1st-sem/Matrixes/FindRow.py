####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Программа для поиска в матрице строки с наибольшим количеством идущих подряд одинаковых элементов
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

# Блок решения
max_n = 1  # Наибольшее количество идущих подряд элементов
max_n_index = 0  # Индекс строки с наибольшим количеством идущих подряд элементов
for i in range(n):
    now = 1  # Сколько сейчас идущих подряд элементов
    for j in range(1, m):
        if matrix[i][j] == matrix[i][j - 1]:
            now += 1
        else:
            if now > max_n:
                max_n = now
                max_n_index = i
            now = 1
    if now > max_n:
        max_n = now
        max_n_index = i

# Блок вывода
if max_n == 1:
    print("В матрице в каждой строке нет одинаковых подряд идущих элементов")
else:
    print(f"Искомая строка имеет номер {max_n_index + 1} и содержит {max_n} идущих подряд элемента: ")
    print(*matrix[max_n_index])
