# Задание с первой лабораторной работы по программированию (писалась на листочке)

# Вводится квадратная целочисленная матрица.
# В каждой строке матрицы нужно поменять местами минимальный и диагональный элементы местами,
# затем вывести матрицу. При выводе добавить столбик с количеством нулевых элементов в соответствующей строке.

def findMinInd(lst):
    m = [lst[0], 0]
    for i in range(len(lst)):
        if m[0] > lst[i]:
            m[0], m[1] = lst[i], i
    return m

def main():
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append([])
        for _ in range(n):
            mat[-1].append(int(input()))
    for i in range(n):
        lst = mat[i]
        m, ind = findMinInd(lst)
        lst[ind], lst[i] = lst[i], lst[ind]
        n0 = 0
        for elem in lst:
            if elem == 0:
                n0 += 1
        lst.append(n0)
        print(*lst, sep="\t")

if __name__ == "__main__":
    main()