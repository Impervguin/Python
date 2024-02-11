import os
import BaseWriter as bw
import BaseReader as br
import SomeFuncs as funcs

base_struct = {'id': 'int', 'name': 'str', 'developer': 'str', 'year': "int", 'price': "float", 'purchased': "bool"}
MENU = """
---------------------------Меню---------------------------
1 - Выбрать другой файл для работы (создать новый).
2 - Вывести базу данных.
3 - Добавить запись в конец базы.
4 - Найти записи по критериям.
5 - Выйти из программы.
"""
while True:
    file = input("Введите путь к файлу: ")
    try:
        open(file).close()
        des = input("Введенный файл уже существует, хотите его перезаписать(y/n)?")
        if des == "y":
            writer = bw.BaseWriter(file, base_struct, True)
            reader = br.BaseReader(file, base_struct, True)
            break
        else:
            try:
                writer = bw.BaseWriter(file)
                reader = br.BaseReader(file)
                break
            except BaseException:
                print("Файл имеет неподходящий формат.")
    except IOError:
        writer = bw.BaseWriter(file, base_struct, True)
        reader = br.BaseReader(file, base_struct, True)
        print("Файл не существует, поэтому будет создан новый.")
        break

while True:
    print(MENU)
    comm = input("Введите команду: ")
    if comm not in "12345":
        print("")
        continue
    elif comm == "1":
        while True:
            file = input("Введите путь к файлу: ")
            try:
                open(file).close()
                des = input("Введенный файл уже существует, хотите его перезаписать(y/n)?")
                if des == "y":
                    writer = bw.BaseWriter(file, base_struct, True)
                    reader = br.BaseReader(file, base_struct, True)
                    break
                else:
                    try:
                        writer = bw.BaseWriter(file)
                        reader = br.BaseReader(file)
                        break
                    except BaseException:
                        print("Файл имеет неподходящий формат.")
            except IOError:
                writer = bw.BaseWriter(file, base_struct, True)
                reader = br.BaseReader(file, base_struct, True)
                print("Файл не существует, поэтому будет создан новый.")
                break
    elif comm == "2":
        reader.print_base()
    elif comm == "3":
        try:
            writer.append(writer.get_input_from_console())
        except PermissionError:
            print("Файл недоступен для записи.")
    elif comm == "4":
        x = input("Введите критерии поиска в формате поле1 оператор1 значение1 поле2...:").split()
        if len(x) % 3 != 0:
            print("Некорректный ввод")
            continue
        try:
            r = reader.find_by_fields(*x)
            if r == 0:
                print("Некорректный ввод")
            if len(r) == 0:
                print("Ничего не найдено")
            else:
                reader.print_base_entries(r)
        except BaseException:
            print("Некорректный ввод")
    elif comm == "5":
        exit()
