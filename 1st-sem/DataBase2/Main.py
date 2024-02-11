import InitDB
import Writer
import Reader
import Funcs
import StructTypes

base_struct = {'id': 'int', 'name': 'str', 'developer': 'str', 'year': "int", 'price': "float", 'purchased': "bool"}

MENU = """
---------------------------Меню---------------------------
1 - Выбрать другой файл для работы (создать новый).
2 - Вывести базу данных.
3 - Добавить запись в произвольное место.
4 - Найти записи по критериям.
5 - Удалить запись.
6 - Выйти из программы.
"""

while True:
    done = False
    file = input("Введите путь к файлу: ")
    try:
        open(file).close()
        while True:
            des = input("Введенный файл уже существует, хотите его перезаписать(y/n)?")
            if des == "y":
                try:
                    format = InitDB.create_db(file, base_struct)
                    f_struct = base_struct
                    done = True
                    break
                except ValueError:
                    print("Некорректная структура базы данных")
                    break
                except PermissionError:
                    print("Не хватает прав для создания/изменения данного файла.")
                    break
            elif des == "n":
                try:
                    f_struct, format = InitDB.open_db(file)
                    done = True
                    break
                except BaseException:
                    print("Файл имеет неподходящий формат.")
            else:
                print("Неккоректный ввод.")
    except FileNotFoundError:
        while True:
            des = input("Файл не существует. Хотите создать пустую базу данных в этом файле(y/n)?")
            if des == "y":
                try:
                    format = InitDB.create_db(file, base_struct)
                    f_struct = base_struct
                    done = True
                    break
                except ValueError:
                    print("Некорректная структура базы данных.")
                    break
                except PermissionError:
                    print("Не хватает прав для создания/изменения данного файла.")
                    break
            elif des == "n":
                break
            else:
                print("Неккоректный ввод.")
    except IsADirectoryError:
        print("Выбранный файл является директорией")
    except PermissionError:
        print("Не хватает прав для работы с файлом.")
    if done:
        break



while True:
    print(MENU)
    comm = input("Введите команду: ")
    if comm not in "123456":
        print("Неверная команда.")
        continue
    elif comm == "1":
        while True:
            done = False
            file = input("Введите путь к файлу: ")
            try:
                open(file).close()
                while True:
                    des = input("Введенный файл уже существует, хотите его перезаписать(y/n)?")
                    if des == "y":
                        try:
                            format = InitDB.create_db(file, base_struct)
                            f_struct = base_struct
                            done = True
                            break
                        except ValueError:
                            print("Некорректная структура базы данных")
                            break
                        except PermissionError:
                            print("Не хватает прав для создания/изменения данного файла.")
                            break
                    elif des == "n":
                        try:
                            f_struct, format = InitDB.open_db(file)
                            done = True
                            break
                        except BaseException:
                            print("Файл имеет неподходящий формат.")
                    else:
                        print("Неккоректный ввод.")
            except FileNotFoundError:
                while True:
                    des = input("Файл не существует. Хотите создать пустую базу данных в этом файле(y/n)?")
                    if des == "y":
                        try:
                            format = InitDB.create_db(file, base_struct)
                            f_struct = base_struct
                            done = True
                            break
                        except ValueError:
                            print("Некорректная структура базы данных.")
                            break
                        except PermissionError:
                            print("Не хватает прав для создания/изменения данного файла.")
                            break
                    elif des == "n":
                        done = True
                        break
                    else:
                        print("Неккоректный ввод.")
            except IsADirectoryError:
                print("Выбранный файл является директорией")
            except PermissionError:
                print("Не хватает прав для работы с файлом.")
            if done:
                break
    elif comm == "2":
        try:
            Reader.print_base(file, format, f_struct)
        except PermissionError:
            print("Файл недоступен для чтения.")
    elif comm == "3":
        try:
            n = Funcs.pos_int_input("Введите номер, куда вставить запись: ", "Неверный номер.")
            entry = Funcs.get_entry_from_console(f_struct)
            Writer.insert(file, format, f_struct, n, entry)
        except PermissionError:
            print("Файл недоступен для записи.")
    elif comm == "4":
        x = input("Введите критерии поиска в формате поле1 оператор1 значение1 поле2...:").split()
        if len(x) % 3 != 0:
            print("Некорректный ввод")
            continue
        try:
            r = Reader.find_by_fields(file, format, f_struct, *x)
            if r == 0:
                print("Некорректный ввод")
            if len(r) == 0:
                print("Ничего не найдено")
            else:
                Reader.print_base_entries(f_struct, r)
        except ValueError:
            print("Некорректный ввод")
        except PermissionError:
            print("Файл недоступен для чтения.")
    elif comm == "5":
        n = Funcs.pos_int_input("Введите номер, записи для удаления: ", "Неверный номер.")
        try:
            Writer.delete(file, format, f_struct, n)
        except ValueError:
            print("Некорректный номер.")
        except PermissionError:
            print("Файл недоступен для записи.")
    elif comm == "6":
        exit()
