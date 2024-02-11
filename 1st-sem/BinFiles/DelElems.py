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

f = open(f_name, "r+b")
shift = 0
i = 0
b_val = f.read(entry_size)
while b_val:
    val = struct.unpack(e_format, b_val)[0]
    if val % 2 == 0:
        shift += 1
        f.seek((i + shift) * entry_size)
        b_val = f.read(entry_size)
        continue
    f.seek(i * entry_size)
    f.write(b_val)
    i += 1
    f.seek((i + shift) * entry_size)
    b_val = f.read(entry_size)
f.truncate(i * entry_size)
f.close()

BinReadWrite.print_bin_file(f_name, e_format, entry_size)


