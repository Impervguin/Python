import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from CalcUI import Ui_MainWindow
import NumLib as nl


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_buttons()
        self.mode = "decimal"
        self.decimal_mode_buttons = \
            [
                self.pushButton_div,
                self.pushButton_mult,
                self.pushButton_plus,
                self.pushButton_minus,
                self.pushButton_1,
                self.pushButton_2,
                self.pushButton_3,
                self.pushButton_4,
                self.pushButton_5,
                self.pushButton_6,
                self.pushButton_7,
                self.pushButton_8,
                self.pushButton_9,
            ]
        self.text_in_field = False

    def connect_buttons(self):
        self.pushButton_0.clicked.connect(self.digit_push)
        self.pushButton_1.clicked.connect(self.digit_push)
        self.pushButton_2.clicked.connect(self.digit_push)
        self.pushButton_3.clicked.connect(self.digit_push)
        self.pushButton_4.clicked.connect(self.digit_push)
        self.pushButton_5.clicked.connect(self.digit_push)
        self.pushButton_6.clicked.connect(self.digit_push)
        self.pushButton_7.clicked.connect(self.digit_push)
        self.pushButton_8.clicked.connect(self.digit_push)
        self.pushButton_9.clicked.connect(self.digit_push)
        self.pushButton_tminus.clicked.connect(self.digit_push)
        self.pushButton_tplus.clicked.connect(self.digit_push)

        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_erase.clicked.connect(self.erase)

        self.pushButton_plus.clicked.connect(self.operator_push)
        self.pushButton_minus.clicked.connect(self.operator_push)
        self.pushButton_mult.clicked.connect(self.operator_push)
        self.pushButton_div.clicked.connect(self.operator_push)
        self.pushButton_eq.clicked.connect(self.eq_push)
        self.pushButton_dot.clicked.connect(self.point_push)

        self.radioButton_decimal.clicked.connect(self.dec_check)
        self.radioButton_thirth.clicked.connect(self.tern_check)

        self.lineEdit.textChanged.connect(self.text_change)

    def clear(self):
        self.lineEdit.setText("")

    def dec_check(self):
        if self.mode == "decimal":
            return 2
        t = self.lineEdit.text()
        if not nl.check_number(t, mode=self.mode):
            self.lineEdit.setText("Can't convert")
            self.radioButton_thirth.setChecked(True)
            self.text_in_field = True
            return 1

        self.lineEdit.setValidator(self.ternar_validator)
        for butt in self.decimal_mode_buttons:
            butt.setEnabled(True)

        self.pushButton_tplus.setDisabled(True)
        self.pushButton_tminus.setDisabled(True)
        self.mode = "decimal"

        new_t = nl.ternar_to_decimal(t)
        self.lineEdit.setText(new_t)
        return 0

    def tern_check(self):
        if self.mode == "ternar":
            return 2
        t = self.lineEdit.text()
        if not nl.check_number(t, mode=self.mode):
            self.lineEdit.setText("Can't convert.")
            self.radioButton_decimal.setChecked(True)
            self.text_in_field = True
            return 1

        for butt in self.decimal_mode_buttons:
            butt.setDisabled(True)

        self.pushButton_tplus.setEnabled(True)
        self.pushButton_tminus.setEnabled(True)
        self.mode = "ternar"

        new_t = nl.decimal_to_ternar(t)
        self.lineEdit.setText(new_t)
        self.lineEdit.setValidator(self.ternar_validator)
        return 0

    def digit_push(self):
        t = self.lineEdit.text()
        button = self.sender()
        t = t + button.text()
        self.lineEdit.setText(t)

    def erase(self):
        t = self.lineEdit.text()
        if len(t) > 0:
            self.lineEdit.setText(t[:-1])

    def operator_push(self):
        t = self.lineEdit.text()

        button = self.sender()
        t = t + button.text()
        if nl.check_expression(t, self.mode):
            self.lineEdit.setText(t)

    def point_push(self):
        t = self.lineEdit.text()

        button = self.sender()
        t = t + button.text()
        if nl.check_expression(t, self.mode):
            self.lineEdit.setText(t)

    def text_change(self):
        if self.text_in_field:
            self.lineEdit.setText("")
            self.text_in_field = False

    def eq_push(self):
        if self.mode != "ternar":
            t = self.lineEdit.text()
            new_t = nl.calc_expr(expr=t)
            self.lineEdit.setText(new_t)
            if new_t == "error":
                self.text_in_field = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wind = MyMainWindow()
    wind.show()
    sys.exit(app.exec_())
