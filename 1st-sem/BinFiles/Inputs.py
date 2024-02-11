def get_int(message):
    while True:
        try:
            x = int(input(message))
            break
        except Exception:
            print("Неккоректный ввод.")
    return x


def get_pos_int(message):
    while True:
        try:
            x = int(input(message))
            if x <= 0:
                raise ValueError
            break
        except Exception:
            print("Неккоректный ввод.")
    return x

def get_file_name(message):
    while True:
        try:
            f = input(message)
            open(f, "w").close()
            break
        except IsADirectoryError:
            print("Неккоректный путь")
        except PermissionError:
            print("Не хватает прав на запись.")
    return f
