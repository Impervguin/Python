####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Программа для вставки элемента в массив по индексу алгоритмически
####################################################################################################################
# Блок ввода
n = int(input("Введите количество элементов в списке: "))
if n < 1:
    print("Некорректное значение.")

lst = [int(input(f"{i + 1}-й элемент: ")) for i in range(n)]
elem, ind = [int(i) for i in input("Введите элемент и его номер через пробел: ").split()]
ind -= 1
if ind > len(lst) or ind < 0:
    print("Введен не корректный индекс.")
    exit()

# Блок обработки
if ind == len(lst) - 1:
    lst.append(elem)
else:
    lst.append(0)  # Добавляем в конец пустой элемент
    for i in range(len(lst) - 1, ind, -1):
        lst[i] = lst[i - 1]  # Смещаем каждое значение вправо на один, начиная с введенного индекса
    lst[ind] = elem  # Вставляем элемент на нужное место

# Блок вывода
for (i, el) in enumerate(lst):
    print(f"{i + 1}-й элемент: {el}")