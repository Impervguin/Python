import random
from copy import deepcopy
text = "ИУ7-12Б занимается в аудитории 534л"
l = len(text)


def generate_2n_matrix(n):
    mat = [[0] * (2 * n) for _ in range(2 * n)]
    choices = [0, 0, 0, 1]
    for k in range(n * n):
        random.shuffle(choices)
        i, j = divmod(k, n)
        mat[i][j] = choices[0]
        mat[j][2 * n - 1 - i] = choices[1]
        mat[2 * n - i - 1][2 * n - j - 1] = choices[2]
        mat[2 * n - 1 - j][i] = choices[3]
    return mat


def rotate90(mat):
    n = len(mat)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = mat[i][j]
            mat[i][j] = mat[n - 1 - j][i]
            mat[n - 1 - j][i] = mat[n - 1 - i][n - 1 - j]
            mat[n - 1 - i][n - 1 - j] = mat[j][n - 1 - i]
            mat[j][n - 1 - i] = temp


def decrypt(arr, mat):
    c_mat = deepcopy(mat)
    text = ""
    for i in range(len(arr)):
        for _ in range(4):
            for j in range(len(arr[i])):
                for k in range(len(arr[i][j])):
                    if c_mat[j][k]:
                        text += arr[i][j][k]
            rotate90(c_mat)
    return text.rstrip()

def encrypt(text, mat):
    c_mat = deepcopy(mat)
    arr = [[[" "] * (2 * n) for _ in range(2 * n)] for _ in range((l) // 64 + 1)]
    text_it = 0
    arr_it = 0
    while True:
        for i in range(2 * n):
            for j in range(2 * n):
                if c_mat[i][j]:
                    arr[arr_it][i][j] = text[text_it]
                    text_it += 1
                    if text_it % 64 == 0:
                        arr_it += 1
                if text_it >= l:
                    break
            if text_it >= l:
                break
        if text_it >= l:
            break
        rotate90(c_mat)
    return arr
n = 4
mat = generate_2n_matrix(n)
for i in range(2 * n):
    print(*mat[i], end="\n")
# arr = [[[" "] * (2 * n) for _ in range(2 * n)] for _ in range((l) // 64 + 1)]
# text_it = 0
# arr_it = 0
# c_mat = deepcopy(mat)
# while True:
#     for i in range(2 * n):
#         for j in range(2 * n):
#             if mat[i][j]:
#                 arr[arr_it][i][j] = text[text_it]
#                 text_it += 1
#                 if text_it % 64 == 0:
#                     arr_it += 1
#             if text_it >= l:
#                 break
#         if text_it >= l:
#             break
#     if text_it >= l:
#         break
#     rotate90(mat)
# print(arr, sep="\n")
arr = encrypt(text, mat)
# for i in range(arr_it + 1):
#     for j in range(len(arr[i])):
#         print(*arr[i][j], end="\n")
#     print()
print(arr)
print(decrypt(arr, mat))
