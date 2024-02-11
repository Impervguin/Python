import struct


def print_bin_file(f_name, e_format, e_size):
    i = 1
    f = open(f_name, "rb")
    x = f.read(e_size)
    while x:
        print(f"{i}-й элемент: {struct.unpack(e_format, x)[0]}")
        i += 1
        x = f.read(e_size)
    f.close()
    if i == 1:
        print("Пустой файл.")