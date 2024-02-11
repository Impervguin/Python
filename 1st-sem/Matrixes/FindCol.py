####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Программа для нахождения столбца с максимальным количеством простых чисел
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
max_n = 0  # Наибольшее кол-во простых чисел в столбце
max_n_index = 0  # Индекс стоблца с наибольшим кол-вом простых чисел в столбце
for j in range(m):
    now = 0  # Количество простых чисел в текущем столбце
    for i in range(n):
        elem = matrix[i][j]
        for k in range(2, int(elem ** 0.5) + 1):  # Проходим по числам до корня числа
            if elem % k == 0:  # Если кратно хоть одному - не подходит
                break
        else:
            now += 1
    if now > max_n:
        max_n = now
        max_n_index = j

# Блок Вывода
if max_n == 0:
    print("В матрице нет простых чисел.")
    exit()

print(f"Искомый столбец имеет номер {max_n_index + 1} и содержит {max_n} простых чисел: ")
for i in range(n):
    print(matrix[i][max_n_index])
