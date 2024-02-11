def print_matrix(mat, wall_symb="|", ceil_symb="-", head=None, foot=None, name=""):
    '''Функция для красивого вывода матрицы'''
    if len(mat) == 0 or len(mat[0]) == 0:
        print("Пустая матрица")
        return 0
    if head is None:
        head = [str(i) for i in range(1, len(mat[0]) + 1)]
    if foot is None:
        foot = [str(i) for i in range(1, len(mat) + 1)]
    foot_len = max([len(str(i)) for i in foot])
    if len(head) != len(mat[0]) or len(foot) != len(mat):
        raise ValueError("Шапка не соответствует размеру матрицы")

    max_elem_len = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            max_elem_len = max(max_elem_len, len(str(mat[i][j])) + 4)
    for el in head:
        max_elem_len = max(max_elem_len, len(str(el)) + 4)

    table_length = (max_elem_len + 1) * (len(mat[0])) + foot_len
    print(name.center(table_length))
    print(" " * foot_len + wall_symb + wall_symb.join(
        [str(i).center(max_elem_len) for i in head]) + wall_symb)
    print(ceil_symb * table_length)
    for i in range(len(mat)):
        # Строки матрицы
        print(str(foot[i]) + " " * (foot_len - len(str(foot[i]))) + wall_symb + wall_symb.join(
            [str(mat[i][j]).center(max_elem_len) for j in range(len(mat[i]))]) + wall_symb)
        print(ceil_symb * table_length)
    print()
    return 0
