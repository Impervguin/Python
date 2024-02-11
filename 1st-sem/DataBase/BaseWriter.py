import BaseWorker as bw
import SomeFuncs as funcs
# дан текстовый файл переписать строки из исходного в другой в обратном порядке. нельзя сохранять файл в память

class BaseWriter(bw.BaseWorker):
    def __init__(self, f_name, base_struct={}, reset=False):
        super(BaseWriter, self).__init__(f_name, base_struct, reset)
        self.f_mode = "a"

    def get_input_from_console(self):
        entry = {}
        for key in self.struct_list:
            while True:
                try:
                    el = input(f"Введите поле {key}({self.struct[key]}): ")
                    entry[key] = bw.TABLE[self.struct[key]](el)
                    break
                except ValueError:
                    print("Некорректный ввод. ")
        return entry

    def append(self, entry):
        self._open_file()
        entry_list = [funcs.to_str(entry[key]) for key in self.struct_list]
        self.f.write(bw.SEPARATOR.join(entry_list) + "\n")
        self._close_file()


if __name__ == "__main__":
    b = BaseWriter("Example.csv")
    b.append(
        {'id': 4, 'name': 'aaaa', 'developer': 'Wube Software LTD', 'year': 20202, 'price': 4.99, 'purchased': True})
