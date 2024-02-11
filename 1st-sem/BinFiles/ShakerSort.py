import Inputs
import struct
import BinReadWrite

def swap(f, e_size, pos1, pos2):
    f.seek(e_size * pos1)
    data1 = f.read(e_size)
    f.seek(e_size * pos2)
    data2 = f.read(e_size)

    f.seek(e_size * pos1)
    f.write(data2)
    f.seek(e_size * pos2)
    f.write(data1)

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
start = 0
end = n - 1
flag = True
while start != end and flag:
    flag = False
    for i in range(start, end):
        f.seek(entry_size * i)
        datai = struct.unpack(e_format, f.read(entry_size))[0]
        datai1 = struct.unpack(e_format, f.read(entry_size))[0]
        if datai > datai1:
            swap(f, entry_size, i, i + 1)
            flag = True
    end -= 1
    if start == end or not flag:
        break
    flag = False
    for i in range(end, start, -1):
        f.seek(entry_size * (i - 1))
        datai = struct.unpack(e_format, f.read(entry_size))[0]
        datai1 = struct.unpack(e_format, f.read(entry_size))[0]
        if datai > datai1:
            swap(f, entry_size, i - 1, i)
            flag = True
    start += 1
f.close()
BinReadWrite.print_bin_file(f_name, e_format, entry_size)


