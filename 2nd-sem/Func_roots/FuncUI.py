# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Python_labs/Func_roots/func.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1223, 988)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 1231, 991))
        self.tabWidget.setObjectName("tabWidget")
        self.input_tab = QtWidgets.QWidget()
        self.input_tab.setObjectName("input_tab")
        self.func_lineEdit = QtWidgets.QLineEdit(self.input_tab)
        self.func_lineEdit.setGeometry(QtCore.QRect(90, 100, 1041, 51))
        self.func_lineEdit.setObjectName("func_lineEdit")
        self.a_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.input_tab)
        self.a_doubleSpinBox.setGeometry(QtCore.QRect(90, 220, 461, 49))
        self.a_doubleSpinBox.setDecimals(4)
        self.a_doubleSpinBox.setMinimum(-10000000000.0)
        self.a_doubleSpinBox.setMaximum(100000000000.0)
        self.a_doubleSpinBox.setProperty("value", -3.0)
        self.a_doubleSpinBox.setObjectName("a_doubleSpinBox")
        self.maxn_spinBox = QtWidgets.QSpinBox(self.input_tab)
        self.maxn_spinBox.setGeometry(QtCore.QRect(90, 440, 1041, 49))
        self.maxn_spinBox.setMaximum(1000000)
        self.maxn_spinBox.setProperty("value", 10)
        self.maxn_spinBox.setObjectName("maxn_spinBox")
        self.error_textEdit = QtWidgets.QTextEdit(self.input_tab)
        self.error_textEdit.setGeometry(QtCore.QRect(90, 550, 1041, 201))
        self.error_textEdit.setReadOnly(True)
        self.error_textEdit.setObjectName("error_textEdit")
        self.calc_pushButton = QtWidgets.QPushButton(self.input_tab)
        self.calc_pushButton.setGeometry(QtCore.QRect(90, 800, 160, 60))
        self.calc_pushButton.setText("Рассчитать")
        self.calc_pushButton.setObjectName("calc_pushButton")
        self.label = QtWidgets.QLabel(self.input_tab)
        self.label.setGeometry(QtCore.QRect(90, 60, 1041, 34))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.input_tab)
        self.label_2.setGeometry(QtCore.QRect(90, 190, 451, 34))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.input_tab)
        self.label_3.setGeometry(QtCore.QRect(670, 190, 451, 34))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.input_tab)
        self.label_4.setGeometry(QtCore.QRect(670, 300, 451, 34))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.input_tab)
        self.label_5.setGeometry(QtCore.QRect(90, 300, 451, 34))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.input_tab)
        self.label_6.setGeometry(QtCore.QRect(90, 410, 511, 34))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.input_tab)
        self.label_7.setGeometry(QtCore.QRect(90, 520, 451, 34))
        self.label_7.setObjectName("label_7")
        self.b_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.input_tab)
        self.b_doubleSpinBox.setGeometry(QtCore.QRect(670, 230, 461, 49))
        self.b_doubleSpinBox.setDecimals(8)
        self.b_doubleSpinBox.setMinimum(-10000000000.0)
        self.b_doubleSpinBox.setMaximum(100000000000.0)
        self.b_doubleSpinBox.setProperty("value", 3.0)
        self.b_doubleSpinBox.setObjectName("b_doubleSpinBox")
        self.h_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.input_tab)
        self.h_doubleSpinBox.setGeometry(QtCore.QRect(90, 330, 461, 49))
        self.h_doubleSpinBox.setDecimals(8)
        self.h_doubleSpinBox.setMinimum(-10000000000.0)
        self.h_doubleSpinBox.setMaximum(100000000000.0)
        self.h_doubleSpinBox.setProperty("value", 1.5)
        self.h_doubleSpinBox.setObjectName("h_doubleSpinBox")
        self.eps_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.input_tab)
        self.eps_doubleSpinBox.setGeometry(QtCore.QRect(670, 340, 461, 49))
        self.eps_doubleSpinBox.setDecimals(8)
        self.eps_doubleSpinBox.setMinimum(0)
        self.eps_doubleSpinBox.setMaximum(100000000000.0)
        self.eps_doubleSpinBox.setProperty("value", 0.01)
        self.eps_doubleSpinBox.setObjectName("eps_doubleSpinBox")
        self.tabWidget.addTab(self.input_tab, "")
        self.table_tab = QtWidgets.QWidget()
        self.table_tab.setObjectName("table_tab")
        self.tableWidget = QtWidgets.QTableWidget(self.table_tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1231, 941))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tabWidget.addTab(self.table_tab, "")
        self.graph_tab = QtWidgets.QWidget()
        self.graph_tab.setObjectName("graph_tab")
        plt.rcParams.update({'font.size': 20})
        self.figure = plt.Figure()
        self.canvas = FigureCanvas(self.figure)

        self.graph = QtWidgets.QWidget(self.graph_tab)
        self.graph.setGeometry(QtCore.QRect(0, 100, 1221, 831))
        self.graph.setObjectName("graph")

        self.vpl = QtWidgets.QVBoxLayout()
        self.vpl.addWidget(self.canvas)
        self.graph.setLayout(self.vpl)


        self.toolbar = NavigationToolbar(self.canvas, self.graph_tab)
        self.toolbar.setGeometry(QtCore.QRect(0, 0, 1221, 101))
        self.toolbar.setObjectName("toolbar")
        self.tabWidget.addTab(self.graph_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.func_lineEdit.setText(_translate("MainWindow", "x**2 - 4"))
        self.label.setText(_translate("MainWindow", "Функция"))
        self.label_2.setText(_translate("MainWindow", "Левая граница"))
        self.label_3.setText(_translate("MainWindow", "Правая граница"))
        self.label_4.setText(_translate("MainWindow", "Точность Эпсилон"))
        self.label_5.setText(_translate("MainWindow", "Шаг деления"))
        self.label_6.setText(_translate("MainWindow", "Максимальное количество итераций"))
        self.label_7.setText(_translate("MainWindow", "Вывод ошибок"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.input_tab), _translate("MainWindow", "Ввод"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№ корня"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "[xi; xi+1]"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "x’"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "f(x’)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Количество\n"
"итераций"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Код ошибки"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.table_tab), _translate("MainWindow", "Таблица"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graph_tab), _translate("MainWindow", "График"))
