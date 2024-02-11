import sys

from PyQt5 import QtWidgets, QtCore, QtGui


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupui(self)

    def setupui(self, mw):
        mw.resize(800, 600)
        self.inp1 = QtWidgets.QLineEdit(mw)
        self.inp1.setGeometry(100, 100, 500, 50)
        self.inp1_label = QtWidgets.QLabel(mw)
        self.inp1_label.setGeometry(100, 50, 500, 50)
        self.inp1_label.setText("Введите первое число: ")

        self.inp2 = QtWidgets.QLineEdit(mw)
        self.inp2.setGeometry(100, 200, 500, 50)
        self.inp2_label = QtWidgets.QLabel(mw)
        self.inp2_label.setGeometry(100, 150, 500, 50)
        self.inp2_label.setText("Введите второе число: ")

        self.output = QtWidgets.QLineEdit(mw)
        self.output.setGeometry(100, 400, 500, 50)
        self.output.setReadOnly(True)
        self.out_label = QtWidgets.QLabel(mw)
        self.out_label.setGeometry(100, 350, 500, 50)
        self.out_label.setText("Сумма: ")

        self.eq_but = QtWidgets.QPushButton(mw)
        self.eq_but.setText("=")
        self.eq_but.setGeometry(100, 275, 50, 50)

        self.val = QtGui.QRegExpValidator(QtCore.QRegExp("^[01]*$"))
        self.inp1.setValidator(self.val)
        self.inp2.setValidator(self.val)

        self.eq_but.clicked.connect(self.calc)

    def calc(self):
        num1 = self.inp1.text()
        num2 = self.inp2.text()
        if num1 == "" or num2 == "":
            self.output.setText("Error")
            return 1
        res = 0
        mod = 1
        for i in num1[::-1]:
            if i == "1":
                res += mod
            mod *= 2
        mod = 1
        for i in num2[::-1]:
            if i == "1":
                res += mod
            mod *= 2

        bin_res = ""
        if res == 0:
            bin_res = "0"
        while res > 0:
            bin_res = str(res % 2) + bin_res
            res //= 2

        self.output.setText(bin_res)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    wind = MyMainWindow()
    wind.show()
    sys.exit(app.exec_())
