import struct


def to_str(elem):
    if isinstance(elem, float):
        return f"{elem:.5g}"
    return str(elem)


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

