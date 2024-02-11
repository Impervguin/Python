import struct
import struct as st
import re
import StructTypes


def create_db(f_name: str, base_struct: dict):
    if not (all([base_struct[i] in StructTypes.table.keys() for i in base_struct.keys()])):
        raise ValueError
    f = open(f_name, "wb")
    n = len(base_struct.keys())
    f.write(struct.pack("q", n))
    format_s = ""
    for key in base_struct.keys():
        f.write(struct.pack("64s", str.encode(key)))
        format_s = format_s + StructTypes.get_bin_type(base_struct[key])
    f.write(struct.pack("64s", str.encode(format_s)))
    f.close()
    return format_s


def open_db(f_name: str) -> (dict, str):
    f = open(f_name, "rb")

    n = st.unpack("q", f.read(8))[0]
    cols = list(st.unpack("64s" * n, f.read(64 * n)))
    format_s = bytes.decode(st.unpack("64s", f.read(64))[0]).replace("\x00", "")

    f.close()

    for i in range(n):
        cols[i] = bytes.decode(cols[i]).replace("\x00", "")
    if not re.match("([0-9]*[qds?])+", format_s):
        raise ValueError
    parts_f = re.findall("[0-9]*[qds?]", format_s)
    if len(parts_f) != len(cols):
        raise KeyError
    base_struct = {cols[i]: StructTypes.get_py_type(parts_f[i]) for i in range(n)}

    return base_struct, format_s


if __name__ == "__main__":
    create_db("test", {"aaa": "int", "bbb": "str", "ccc": "bool", "dddddddd": "float"})
    print(*open_db("test"), sep="\n")
    print(open("test", "rb").read())
