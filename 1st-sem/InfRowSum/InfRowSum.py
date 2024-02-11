####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
# Вариант 55
# Программа для расчета суммы бесконечного ряда с точностью до эпсилон.
# Также программа выводит таблицу промежуточных значений
####################################################################################################################

WALL_SYMBOL = "|"  # Символ, используемый в вертикальных ограничителях
CEIL_SYMBOL = "-"  # Символ, используемый в горизонтальных ограничителях
NUMBER_SPACE = 9   # Ширина столбца с числами в символах
ITER_SPACE = 12    # Ширина столбца с итерациями (>=12)

# Ввод
eps, max_iter, h = [float(i) for i in
                    input("Введите точность, максимальное количество итераций и шаг печати через пробел: ").split()]
max_iter = int(max_iter)
h = int(h)

if eps < 0 or max_iter < 0 or h < 0:
    print("Некорректные входные данные")


row_sum = 0  # Сумма ряда
s = 1        # Элемент ряда с первым значение
i = 1        # Номер элемента

print(WALL_SYMBOL + CEIL_SYMBOL * (12 + 2 + NUMBER_SPACE * 2) + WALL_SYMBOL)  # Шапка таблицы
print(
    WALL_SYMBOL + "№ Итерации".center(ITER_SPACE) + WALL_SYMBOL + "s".center(NUMBER_SPACE) + WALL_SYMBOL + "sum".center(
        NUMBER_SPACE) + WALL_SYMBOL)
print(WALL_SYMBOL + CEIL_SYMBOL * (12 + 2 + NUMBER_SPACE * 2) + WALL_SYMBOL)
while i <= max_iter and abs(
        s) > eps:  # Пока количество итераций не превысило максимальное или не достигнута нужная точность
    row_sum += s          # Прибавляем в сумму текущий элемет
    if (i - 1) % h == 0:  # Если подходит под шаг выводим промежуточный результат в таблицу
        print(WALL_SYMBOL + str(i).center(ITER_SPACE) + WALL_SYMBOL + f"{s:.5g}".center(
            NUMBER_SPACE) + WALL_SYMBOL + f"{row_sum:.5g}".center(NUMBER_SPACE) + WALL_SYMBOL)
    s = (-1) ** i / (2 * (i + 1) - 1)  # Считаем следующий элемент
    i += 1                             # Обновляем счетчик
print(WALL_SYMBOL + CEIL_SYMBOL * (12 + 2 + NUMBER_SPACE * 2) + WALL_SYMBOL)  # Закрываем таблицу

if i - 1 == max_iter:
    print(f"За {max_iter} итераций не удалось вычислить сумму ряда с точностью до {eps}")
else:
    print(f"Сумма бесконечного ряда - {row_sum:.5g}, вычислена за {i - 1} итераций.")  # Вывод результата
