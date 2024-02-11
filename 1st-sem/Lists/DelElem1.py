####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Программа для удаления элемента в массиве по индексу встроенными методами
####################################################################################################################
# Блок ввода
n = int(input("Введите количество элементов в списке: "))
if n < 1:
    print("Некорректное значение.")

lst = [int(input(f"{i + 1}-й элемент: ")) for i in range(n)]
ind = int(input("Введите номер удаляемого элемента: ")) - 1
if ind >= len(lst) or ind < 0:
    print("Введен не корректный индекс.")
    exit()

# Блок обработки
lst.pop(ind)  # Удаляем элемент с помощью встроенного метода

# Блок вывода
for (i, el) in enumerate(lst):
    print(f"{i + 1}-й элемент: {el}")
if len(lst) == 0:
    print("Пустой массив")
