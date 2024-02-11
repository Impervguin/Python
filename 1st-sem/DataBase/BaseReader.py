import BaseWorker as bw
import SomeFuncs as funcs

WALL = "|"
CEIL = "-"


class BaseReader(bw.BaseWorker):
    def __init__(self, f_name, base_struct={}, reset=False):
        super(BaseReader, self).__init__(f_name, base_struct, reset)
        self.f_mode = "r"

    def __get_next_line(self):
        line = self.f.readline()
        if not line:
            return 0

        els = line.strip().split(bw.SEPARATOR)
        if len(els) != len(self.struct_list):
            return 1
        try:
            d = {self.struct_list[i]: bw.TABLE[self.struct[self.struct_list[i]]](els[i]) for i in
                 range(len(self.struct_list))}
        except ValueError:
            return 1
        return d

    def print_base_entries(self, entries):
        # Находим длину максимального элемента
        self._open_file()
        max_elem_len = max(map(len, self.struct_list))
        while entry := self.__get_next_line():
            if entry == 1:
                continue
            max_elem_len = max(max_elem_len, max(map(len, map(funcs.to_str, entry.values()))))
        max_elem_len += 2
        table_length = (max_elem_len + 1) * (len(self.struct_list))
        self._close_file()

        self._open_file()
        print(WALL + WALL.join([str(i).center(max_elem_len) for i in self.struct_list]) + WALL)
        print(WALL + WALL.join([self.struct[i].center(max_elem_len) for i in self.struct_list]) + WALL)
        print(CEIL * table_length)
        for entry in entries:
            print(WALL + WALL.join([funcs.to_str(entry[key]).center(max_elem_len) for key in self.struct_list]) + WALL)
            print(CEIL * table_length)
        self._close_file()

    def print_base(self):
        # Находим длину максимального элемента
        self._open_file()
        max_elem_len = max(map(len, self.struct_list))
        while entry := self.__get_next_line():
            print(entry)
            if entry == 1:
                continue
            max_elem_len = max(max_elem_len, max(map(len, map(funcs.to_str, entry.values()))))
        max_elem_len += 2
        table_length = (max_elem_len + 1) * (len(self.struct_list))
        self._close_file()

        self._open_file()
        print(WALL + WALL.join([str(i).center(max_elem_len) for i in self.struct_list]) + WALL)
        print(WALL + WALL.join([self.struct[i].center(max_elem_len) for i in self.struct_list]) + WALL)
        print(CEIL * table_length)
        while entry := self.__get_next_line():
            if entry == 1:
                continue
            print(WALL + WALL.join([funcs.to_str(entry[key]).center(max_elem_len) for key in self.struct_list]) + WALL)
            print(CEIL * table_length)
        self._close_file()

    def find_by_fields(self, *args):
        fields = args[::3]
        ops = args[1::3]
        vals = list(args[2::3])
        try:
            for i in range(len(fields)):
                vals[i] = bw.TABLE[self.struct[fields[i]]](vals[i])
        except ValueError:
            return 0
        res = []
        self._open_file()
        while entry := self.__get_next_line():
            if all([funcs.compare(entry[fields[i]], ops[i], vals[i]) for i in range(len(vals))]):
                res.append(entry)
        self._close_file()
        return res

    # def find_by_one_field(self, field, op, val):
    #     try:
    #         val = self.struct[field](val)
    #     except ValueError:
    #         return 0
    #     res = []
    #     self._open_file()
    #     while entry := self.__get_next_line():
    #         f_val = entry[field]
    #         if funcs.compare(f_val, op, val):
    #             res.append(entry)
    #     self._close_file()
    #     return res
    #
    # def find_by_two_fields(self, field1, op1, val1, field2, op2, val2):
    #     try:
    #         val1 = self.struct[field1](val1)
    #         val2 = self.struct[field2](val2)
    #     except ValueError:
    #         return 0
    #     res = []
    #     self._open_file()
    #     while entry := self.__get_next_line():
    #         f_val1 = entry[field1]
    #         f_val2 = entry[field2]
    #
    #         if x:
    #             res.append(entry)
    #     self._close_file()
    #     return res


if __name__ == "__main__":
    b = BaseReader("Example.csv")
    b.print_base()
    # print(b.find_by_fields("year", ">=", "2018", "developer", "!=", "Shiro Games"))
    # b.print_base_entries([{'id': 3, 'name': 'Factorio', 'developer': 'Wube Software LTD', 'year': 2020, 'price': 4.99,
    #                        'purchased': True},
    #                       {'id': 4, 'name': 'aaaa', 'developer': 'Wube Software LTD', 'year': 20202, 'price': 4.99,
    #                        'purchased': True}])
