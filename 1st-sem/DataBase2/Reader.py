import struct
import Funcs
import StructTypes

WALL = "|"
CEIL = "-"


def decode_from_format(format, base_struct, entry) -> dict:
    d = {}
    data = struct.unpack(format, entry)
    for i in range(len(base_struct.keys())):
        key = list(base_struct.keys())[i]
        typ = base_struct[key]
        el = data[i]
        if typ == "str":
            el = Funcs.clean_str(bytes.decode(el))
        d[key] = el
    return d


def print_base(f_name: str, format: str, base_struct: dict):
    entry_bytes = struct.calcsize(format)
    max_elem_len = max(map(len, base_struct.keys()))
    n = len(base_struct.keys())

    f = open(f_name, "rb")
    f.seek(8 + 64 * (n + 1))
    entry = f.read(entry_bytes)
    while entry:
        entry = struct.unpack(format, entry)
        max_elem_len = max(max_elem_len, max(map(len, map(Funcs.to_str, entry))))
        entry = f.read(entry_bytes)
    f.close()

    max_elem_len += 2
    table_length = (max_elem_len + 1) * (len(base_struct.keys()))
    print(WALL + WALL.join([str(i).center(max_elem_len) for i in base_struct.keys()]) + WALL)
    print(WALL + WALL.join([base_struct[i].center(max_elem_len) for i in base_struct.keys()]) + WALL)
    print(CEIL * table_length)
    f = open(f_name, "rb")
    f.seek(8 + 64 * (n + 1))
    entry = f.read(entry_bytes)
    while entry:
        entry = struct.unpack(format, entry)
        print(WALL + WALL.join([Funcs.to_str(el).center(max_elem_len) for el in entry]) + WALL)
        print(CEIL * table_length)
        entry = f.read(entry_bytes)
    f.close()


def get_number_of_entries(f_name, format, base_struct):
    f = open(f_name, "rb")
    f.seek(8 + 64 * (len(base_struct.keys()) + 1))
    n = 0
    entry_bytes = struct.calcsize(format)
    while f.read(entry_bytes):
        n += 1
    f.close()
    return n


def find_by_fields(f_name, format, base_struct, *args):
    fields = args[::3]
    ops = args[1::3]
    vals = list(args[2::3])
    if len(fields) != len(ops) or len(vals) != len(ops):
        raise ValueError("Wrong amount of args")
    if not all([op in StructTypes.OPS for op in ops]):
        raise ValueError("Operator error")
    if not all([field in base_struct.keys() for field in fields]):
        raise ValueError("Field error")
    for i in range(len(fields)):
        vals[i] = StructTypes.switch_to_table_type(base_struct, fields[i], vals[i])
    res = []

    entry_bytes = Funcs.get_entry_bytes(format)
    n = get_number_of_entries(f_name, format, base_struct)
    f = open(f_name, "rb")
    f.seek(8 + 64 * (len(base_struct.keys()) + 1))
    for _ in range(n):
        data = decode_from_format(format, base_struct, f.read(entry_bytes))
        if all([Funcs.compare(data[fields[i]], ops[i], vals[i]) for i in range(len(fields))]):
            res.append(data)
    return res


def print_base_entries(base_struct, entries):
    max_elem_len = max(map(len, base_struct.keys()))
    for el in entries:
        max_elem_len = max(max_elem_len, max(map(len, map(Funcs.to_str, el.values()))))
    max_elem_len += 2
    table_length = (max_elem_len + 1) * (len(base_struct.keys()))
    print(WALL + WALL.join([str(i).center(max_elem_len) for i in base_struct.keys()]) + WALL)
    print(WALL + WALL.join([base_struct[i].center(max_elem_len) for i in base_struct.keys()]) + WALL)
    print(CEIL * table_length)
    for entry in entries:
        print(WALL + WALL.join([Funcs.to_str(entry[key]).center(max_elem_len) for key in entry]) + WALL)
        print(CEIL * table_length)