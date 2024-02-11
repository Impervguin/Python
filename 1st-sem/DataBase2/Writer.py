import struct
from Reader import get_number_of_entries
import Funcs
from tempfile import NamedTemporaryFile
from shutil import copyfile

def append(f_name: str, format: str, base_struct: dict, d: dict):
    f = open(f_name, "ab")
    lst = []
    for key in base_struct.keys():
        lst.append(d[key] if base_struct[key] != 'str' else str.encode(d[key]))
    f.write(struct.pack(format, *lst))
    f.close()


# def insert(f_name: str, format: str, base_struct: dict, pos: int, entry: dict):
#     n = get_number_of_entries(f_name, format, base_struct)
#     lst = []
#     entry_bytes = Funcs.get_entry_bytes(format)
#     for key in base_struct.keys():
#         lst.append(entry[key] if base_struct[key] != 'str' else str.encode(entry[key]))
#     if pos > n:
#         f = open(f_name, "ab")
#         f.write(struct.pack(format, *lst))
#         f.close()
#         return 0
#     temp = NamedTemporaryFile("wb")
#     f = open(f_name, "rb")
#     temp.file.write(f.read(8 + 64 * (len(base_struct.keys()) + 1)))
#     for i in range(n):
#         if i == pos - 1:
#             temp.file.write(struct.pack(format, *lst))
#         data = f.read(entry_bytes)
#         print(data)
#         temp.file.write(data)
#     f.close()
#     temp.flush()
#     copyfile(temp.name, f_name)
#     temp.close()


def insert(f_name: str, format: str, base_struct: dict, pos: int, entry: dict):
    n = get_number_of_entries(f_name, format, base_struct)
    entry_bytes = Funcs.get_entry_bytes(format)
    lst = []
    for key in base_struct.keys():
        lst.append(entry[key] if base_struct[key] != 'str' else str.encode(entry[key]))
    if pos > n:
        f = open(f_name, "ab")
        f.write(struct.pack(format, *lst))
        f.close()
        return 1
    f = open(f_name, "r+b")
    for i in range(n - 1, pos - 2, -1):
        f.seek(8 + 64 * (len(base_struct.keys()) + 1) + entry_bytes * i)
        data = f.read(entry_bytes)
        f.write(data)
    f.seek(8 + 64 * (len(base_struct.keys()) + 1) + (pos - 1) * entry_bytes)
    f.write(struct.pack(format, *lst))
    return 1

def delete(f_name: str, format: str, base_struct: dict, pos: int):
    n = get_number_of_entries(f_name, format, base_struct)
    entry_bytes = Funcs.get_entry_bytes(format)
    if pos > n:
        raise ValueError
    f = open(f_name, "r+b")
    if pos == n:
        f.seek(8 + 64 * (len(base_struct.keys()) + 1) + entry_bytes * (pos - 1))
        f.truncate()
        f.close()
        return 1
    for i in range(pos, n):
        f.seek(8 + 64 * (len(base_struct.keys()) + 1) + entry_bytes * i)
        data = f.read(entry_bytes)
        f.seek(8 + 64 * (len(base_struct.keys()) + 1) + entry_bytes * (i - 1))
        f.write(data)
    f.truncate()
    f.close()
    return 1




