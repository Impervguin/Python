# Удалить из матрицы строки с нулевыми элементами

n, m = map(int, input("Введите через пробел количество строк и столбцов матрицы: ").split())
if m <= 0 or n <= 0:
    print("Некорректные размеры матрицы.")
    exit()
max_elem_len = 0
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = float(input(f"Введите элемент в {i + 1}-ой строке {j + 1}-ом столбе: "))
        max_elem_len = max(len(f"{matrix[i][j]:.5g}"), max_elem_len)
max_elem_len += 2

print("Исходная матрица:")
for i in range(n):
    print()
    for j in range(m):
        now_len = len(f"{matrix[i][j]:.5g}")
        print(f"{matrix[i][j]:.5g}", end="")
        if j != m - 1:
            print(" " * (max_elem_len - now_len), end="")
print()

i = 0
while i < len(matrix):
    for j in range(n):
        if matrix[i][j] == 0:
            del matrix[i]
            break
    else:
        i += 1

if len(matrix) == 0:
    print("Все строки содержат нулевой элемент")
else:
    print("Модифицированная матрица:")
    for i in range(len(matrix)):
        print()
        for j in range(m):
            now_len = len(f"{matrix[i][j]:.5g}")
            print(f"{matrix[i][j]:.5g}", end="")
            if j != m - 1:
                print(" " * (max_elem_len - now_len), end="")

