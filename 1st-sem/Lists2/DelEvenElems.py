####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Программа для удаления чётных элементов в массиве
####################################################################################################################
n = int(input("Введите количество элементов в списке: "))
if n < 1:
    print("Некорректное значение.")

lst = [int(input(f"{i + 1}-й элемент: ")) for i in range(n)]  # Ввод списка

i = 0
while i < len(lst):
    if lst[i] % 2 == 0:  # Проверяем на чётность
        del lst[i]  # Удаляем
        i -= 1
    i += 1

for (i, el) in enumerate(lst):  # Вывод
    print(f"{i + 1}-й элемент: {el}")
if len(lst) == 0:
    print("Пустой массив")
