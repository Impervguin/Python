def sort(lst):
    lst = lst.copy()
    factor = 1.247
    step = len(lst) - 1
    while step >= 1:
        i = 0
        while i + step < len(lst):
            if lst[i] > lst[i + step]:
                lst[i], lst[i + step] = lst[i + step], lst[i]
            i += 1
        step = int(step // factor)
    return lst


n = int(input("Введите размер массива: "))
if n <= 0:
    print("Некорректный размер.")
    exit()

lst = [int(input(f"Введите {i + 1}-й элемент массива: ")) for i in range(n)]
s_lst = sort(lst)
print("Отсортированный массив: ")
for i in range(len(lst)):
    print(f"{i + 1}-й элемент массива: {s_lst[i]}")

