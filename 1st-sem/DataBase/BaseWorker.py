TABLE = {
    "int": int,
    "str": str,
    "float": float,
    "bool": bool
}
SEPARATOR = ","

class BaseWorker:
    def __init__(self, f_name, base_struct={}, reset=False):
        self.f_name = f_name
        self.f_mode = "a"
        if reset:
            self.struct = base_struct
            self.struct_list = list(base_struct.keys())
            self.__create_file()
        else:
            self.__read_head_file()

    def __create_file(self):
        self.f = open(self.f_name, mode="w")
        lines = [[], []]
        for key, val in self.struct.items():
            lines[0].append(key)
            lines[1].append(val)
        self.f.writelines([SEPARATOR.join(lines[0]) + "\n", SEPARATOR.join(lines[1]) + "\n"])
        self._close_file()

    def __read_head_file(self):
        self.f = open(self.f_name, mode="r")
        keys = self.f.readline().strip().split(SEPARATOR)
        self.struct_list = keys
        val = self.f.readline().strip().split(SEPARATOR)
        if any([i not in TABLE.keys() for i in val]):
            raise BaseException
        self.struct = {keys[i]: val[i] for i in range(len(keys))}
        self._close_file()

    def _open_file(self):
        self.f = open(self.f_name, mode=self.f_mode)
        if self.f_mode == "r":
            self.f.readline()
            self.f.readline()

    def _close_file(self):
        self.f.close()
