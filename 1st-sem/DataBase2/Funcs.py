import struct
import StructTypes
import fcntl


def clean_str(s: str):
    return s.replace("\x00", "")


def to_str(elem):
    if isinstance(elem, float):
        return f"{elem:.5g}"
    if isinstance(elem, bytes):
        return bytes.decode(elem).replace("\x00", "")
    return str(elem)


def get_entry_bytes(format):
    return struct.calcsize(format)


def compare(val1, op, val2):
    match op:
        case "<":
            return val1 < val2
        case ">":
            return val1 > val2
        case "<=":
            return val1 <= val2
        case ">=":
            return val1 >= val2
        case '==':
            return val1 == val2
        case "!=":
            return val1 != val2


def pos_int_input(input_mes: str, negative_mes: str) -> int:
    while True:
        try:
            n = int(input(input_mes))
            if n <= 0:
                print(negative_mes)
                continue
            break
        except Exception:
            print("Неккоректный ввод")
    return n


def get_entry_from_console(base_struct):
    entry = {}
    for key in base_struct.keys():
        while True:
            try:
                el = input(f"Введите поле {key}({base_struct[key]}): ").strip()
                if base_struct[key] == "bool":
                    if el not in ("True", "False", "true", "false", "1", "0"):
                        raise ValueError
                    entry[key] = True if el in ("True", "true", "1") else False
                    break
                entry[key] = StructTypes.switch_to_table_type(base_struct, key, el)
                break
            except ValueError:
                print("Некорректный ввод. ")
    return entry
