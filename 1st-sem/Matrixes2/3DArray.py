####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й
# срез (матрицу - фрагмент трёхмерного массива) по второму индексу (нумерация
# индексов начинается с 1).
####################################################################################################################
WALL_SYMB = " "
CEIL_SYMB = " "

n, m, k = map(int, input("Введите через пробел количество строк, столбцов и глубину трёхмерного массива: ").split())
if n <= 0 or m <= 0 or k <= 0:
    print("Некорректные данные.")
    exit()
I = int(input("Введите номер среза: "))
if I >= m or I <= 0:
    print("Некорректные данные.")
    exit()

max_elem_len = 0
A = [[[0] * k for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        for h in range(k):
            A[i][j][h] = float(
                input(f"Введите элемент в {i + 1}-ой строке {j + 1}-ом столбе {h + 1}-ой глубины матрицы A: "))
            max_elem_len = max(len(str(A[i][j])), max_elem_len)
max_elem_len += 2
table_length = (max_elem_len + 1) * (m + 1)


slice = [[A[i][I - 1][j] for j in range(k)] for i in range(n)]


print("Матрица-срез:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(k)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(n):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(slice[i][j]).center(max_elem_len) for j in range(k)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()
