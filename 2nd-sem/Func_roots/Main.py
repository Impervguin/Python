import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from FuncUI import Ui_MainWindow
import Math
from math import *


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calc_pushButton.clicked.connect(self.calculate)

    def calculate(self):
        rc, func_t, left, right, step, max_iter, eps = self.get_input()
        if rc == 1:
            return 1

        def f(x):
            return eval(func_t)

        roots = Math.find_roots(f, left, right, step, max_iter, eps)
        try:
            expr = Math.find_extr(func_t, left, right, step, max_iter, eps)
        except BaseException:
            expr = []
        try:
            infl = Math.find_inflection(func_t, left, right, step, max_iter, eps)
        except BaseException:
            infl = []
        self.fill_table(roots)
        self.plot(f, roots, expr, infl, left, right, step)

    def get_input(self):
        left = self.a_doubleSpinBox.value()
        right = self.b_doubleSpinBox.value()
        if left > right:
            self.error_textEdit.setText(self.error_textEdit.text() + "\n" + "Левая граница не модет быть больше правой")
            return 1
        step = self.h_doubleSpinBox.value()
        max_iter = self.maxn_spinBox.value()
        eps = self.eps_doubleSpinBox.value()
        if eps < 0.000000001:
            self.error_textEdit.setText(self.error_textEdit.text() + "\n" + "Точность не может быть нулевой")
            return 1
        func_t = self.func_lineEdit.text()
        return 0, func_t, left, right, step, max_iter, eps

    def fill_table(self, roots):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setRowCount(len(roots))
        for root in roots:
            self.tableWidget.setItem(root["num"] - 1, 0, QtWidgets.QTableWidgetItem(str(root["num"])))
            self.tableWidget.setItem(root["num"] - 1, 1,
                                     QtWidgets.QTableWidgetItem(f"[{root['left']:.2f}, {root['right']:.2f}]"))
            if root["error"] == 0:
                self.tableWidget.setItem(root["num"] - 1, 2, QtWidgets.QTableWidgetItem(f'{root["value"]:.6g}'))
                self.tableWidget.setItem(root["num"] - 1, 3, QtWidgets.QTableWidgetItem(f'{root["f_value"]:.6g}'))
                self.tableWidget.setItem(root["num"] - 1, 4, QtWidgets.QTableWidgetItem(str(root["iter"])))
            self.tableWidget.setItem(root["num"] - 1, 5, QtWidgets.QTableWidgetItem(str(root["error"])))

    def plot(self, f, roots, expr, infl,left, right, step):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        x = []
        y = []
        x_extr = []
        y_extr = []
        while left < right:
            x.append(left)
            y.append(f(left))
            left += min(step / 10, 0.01)
        x_extr = []
        y_extr = []
        # for i in range(1, len(x) - 1):
        #     if f(x[i - 1]) > f(x[i]) < f(x[i + 1]) or f(x[i - 1]) < f(x[i]) > f(x[i + 1]):
        #         x_extr.append(x[i])
        #         y_extr.append(f(x[i]))

        for ex in expr:
            if ex["error"] == 0:
                x_extr.append(ex["value"])
                y_extr.append(f(ex["value"]))

        x_infl = []
        y_infl = []
        for inf in infl:
            if inf["error"] == 0:
                x_infl.append(inf["value"])
                y_infl.append(f(inf["value"]))
        x_root = []
        y_root = []
        for root in roots:
            if root["error"] == 0:
                x_root.append(root["value"])
                y_root.append(root["f_value"])
        ax.scatter(x_root, y_root, color="blue")
        ax.scatter(x_extr, y_extr, color="red")
        ax.scatter(x_infl, y_infl, color="green")
        ax.plot(x, y)

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wind = MyMainWindow()
    wind.show()
    sys.exit(app.exec_())
