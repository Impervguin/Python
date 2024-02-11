import sys

from PyQt5 import QtCore, QtGui, QtWidgets

def pol_met(f, a, b, h, e, m):
    left = a
    right = b
    middle = (a + b) / 2
    n = 1
    if f(a) * f(b) < 0:
        while f(middle) > e and n < m:
            middle = (a + b) / 2
            f_m = f(middle)
            if f_m > 0:
                a = middle
            else:
                b = middle
            n += 1
        return (0, middle, n)
    else:
        return (1, 0)
class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupui()

    def setupui(self):
        self.resize(1000, 1000)
        self.tab_W = QtWidgets.QTabWidget(self)
        self.tab_W.setGeometry(0, 0, 1000, 1000)
        self.tab1 = QtWidgets.QWidget()
        self.tab_W.addTab(self.tab1, "Ввод")
        self.tab_W.setTabText(0, "Ввод")
        self.tab2 = QtWidgets.QWidget()
        self.tab_W.addTab(self.tab2, "Таблица")
        self.tab_W.setTabText(1, "Таблица")
        self.func_field = QtWidgets.QLineEdit(self.tab1)
        self.func_field.setGeometry(100, 100, 800, 50)

        self.a_field = QtWidgets.QDoubleSpinBox(self.tab1)
        self.a_field.setGeometry(100, 250, 300, 50)

        self.b_field = QtWidgets.QDoubleSpinBox(self.tab1)
        self.b_field.setGeometry(500, 250, 300, 50)

        self.h_field = QtWidgets.QDoubleSpinBox(self.tab1)
        self.h_field.setGeometry(100, 400, 300, 50)

        self.e_field = QtWidgets.QDoubleSpinBox(self.tab1)
        self.e_field.setGeometry(500, 400, 300, 50)

        self.maxn = QtWidgets.QSpinBox(self.tab1)
        self.maxn.setGeometry(100, 550, 300, 50)

        self.butt = QtWidgets.QPushButton(self.tab1)
        self.butt.setGeometry(500, 550, 300, 50)
        self.butt.clicked.connect(self.calc)

        self.table = QtWidgets.QTableWidget(self.tab2)
        self.table.setGeometry(0, 0, 900, 900)
        self.table.setColumnCount(4)


    def calc(self):
        a,b,h,e,maxn = self.a_field.value(), self.b_field.value(), self.h_field.value(), self.e_field.value(), self.maxn.value()
        func_t = self.func_field.text()
        def f(x):
            return eval(func_t)
        maxx = b
        minn = a
        roots = []
        while a + h < b:
            root = pol_met(f, a, a + h,h, e, maxn)
            if root[0] == 0:
                roots.append(root)

        self.table.setRowCount(len(roots))
        for i in range(len(roots)):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(roots[i][1]))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(f(roots[i][1])))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(roots[i][2]))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(roots[i][0]))









if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MyMainWindow()
    mw.show()
    sys.exit(app.exec_())
