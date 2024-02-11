def shaker_sort(lst, reverse=False):
    k = 0
    if len(lst) < 2:
        return lst, 0
    lst = lst.copy()
    left, right = 0, len(lst) - 1
    flag = True
    while left < right and flag:
        flag = False
        for i in range(left, right):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                k += 1
                flag = True
        right -= 1

        for i in range(right, left, -1):
            if lst[i - 1] > lst[i]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                k += 1
                flag = True
        left += 1

    if reverse:
        lst = lst[::-1]
    return lst, k
