import Inputs
import struct
import BinReadWrite
f_name = Inputs.get_file_name("Введите имя файла: ")
n = Inputs.get_pos_int("Введите количество элементов: ")
e_format = "i"
entry_size = struct.calcsize(e_format)
f = open(f_name, "wb")

for i in range(n):
    entry = Inputs.get_int(f"Введите {i + 1}-ое число: ")
    f.write(struct.pack(e_format, entry))
f.close()

n3 = 0
f = open(f_name, 'rb')
b_val = f.read(entry_size)
while b_val:
    val = struct.unpack(e_format, b_val)[0]
    if val % 3 == 0:
        n3 += 1
    b_val = f.read(entry_size)
f.close()

f = open(f_name, "r+b")
i_write = n + n3 - 1
i_read = n - 1
f.seek(i_read * entry_size)
b_val = f.read(entry_size)
while i_write != i_read:
    val = struct.unpack(e_format, b_val)[0]
    if val % 3 == 0:
        f.seek(i_write * entry_size)
        f.write(struct.pack(e_format, val * 2))
        i_write -= 1
    f.seek(i_write * entry_size)
    f.write(b_val)
    i_write -= 1
    i_read -= 1
    if i_read < 0:
        break
    f.seek(i_read * entry_size)
    b_val = f.read(entry_size)
f.close()
BinReadWrite.print_bin_file(f_name, e_format, entry_size)


