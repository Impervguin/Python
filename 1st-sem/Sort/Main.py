from PrintMatrix import print_matrix
from ShakerSort import shaker_sort
from Inputs import pos_int_input, float_input
import timeit
import random


def get_time_and_permutations(lst, sort):
    t = timeit.default_timer()
    _, k1 = sort(lst)
    t1 = timeit.default_timer() - t
    return t1, k1


n = pos_int_input("Введите размер массива: ", "Некорректное значение")

lst = [float_input(f"{i + 1}-й элемент: ") for i in range(n)]

sorted_lst, _ = shaker_sort(lst)

print("Отсортированный массив")
for (i, el) in enumerate(lst):
    print(f"{i + 1}-й элемент: {el:.5g}")

n_rand1 = pos_int_input("Введите 1-й размер случайно генерируемого массива: ", "Некорректное значение")
n_rand2 = pos_int_input("Введите 2-й размер случайно генерируемого массива: ", "Некорректное значение")
n_rand3 = pos_int_input("Введите 3-й размер случайно генерируемого массива: ", "Некорректное значение")

rlst1 = [random.randint(-10000, 10000) for i in range(n_rand1)]
rlst_sorted1 = sorted(rlst1)
rlst_reverse1 = rlst_sorted1[::-1]

rlst2 = [random.randint(-10000, 10000) for i in range(n_rand2)]
rlst_sorted2 = sorted(rlst2)
rlst_reverse2 = rlst_sorted2[::-1]

rlst3 = [random.randint(-10000, 10000) for i in range(n_rand3)]
rlst_sorted3 = sorted(rlst3)
rlst_reverse3 = rlst_sorted3[::-1]

head = ["Время N1", "Перерестановки N1", "Время N2", "Перерестановки N2", "Время N3", "Перерестановки N3"]
foot = ['Упорядоченный список', "Случайный список", "Упорядоченный в обратном порядке"]

t1, k1 = get_time_and_permutations(rlst_sorted1, shaker_sort)
t2, k2 = get_time_and_permutations(rlst_sorted2, shaker_sort)
t3, k3 = get_time_and_permutations(rlst_sorted3, shaker_sort)
t4, k4 = get_time_and_permutations(rlst1, shaker_sort)
t5, k5 = get_time_and_permutations(rlst2, shaker_sort)
t6, k6 = get_time_and_permutations(rlst3, shaker_sort)
t7, k7 = get_time_and_permutations(rlst_reverse1, shaker_sort)
t8, k8 = get_time_and_permutations(rlst_reverse2, shaker_sort)
t9, k9 = get_time_and_permutations(rlst_reverse3, shaker_sort)

mat = [[t1, k1, t2, k2, t3, k3],
       [t4, k4, t5, k5, t6, k6],
       [t7, k7, t8, k8, t9, k9]]
for i in range(3):
    for j in range(6):
        mat[i][j] = f"{mat[i][j]:.5g}"
print_matrix(mat, head=head, foot=foot)