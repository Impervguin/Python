OPS = ("!=", "==", ">", "<", ">=", "<=")

d = {"int": "q",
     "float": "d",
     "str": "64s",
     "bool": "?"
     }
r_d = {
    "q": "int",
    "d": "float",
    "64s": "str",
    "?": "bool"
}
table = {
    "int": int,
    "float": float,
    "str": str,
    "bool": bool
}


def switch_to_table_type(base_struct, field, value):
    return table[base_struct[field]](value)


def get_py_type(s):
    return r_d[s]


def get_bin_type(s):
    return d[s]
