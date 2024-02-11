from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1046, 757)
        MainWindow.setStyleSheet("\n"
                                 "QTabWidget {\n"
                                 "  color:#018185;\n"
                                 "  background-color:#d7d5d9;\n"
                                 "  font: bold;\n"
                                 "  font-size:30px;\n"
                                 "}\n"
                                 "QWidget\n"
                                 "{\n"
                                 "   background-color:#292b2f;\n"
                                 "   color:#018185;\n"
                                 "   font: bold;\n"
                                 "   font-size:30px;\n"
                                 "   border-color:#d7d5d9;\n"
                                 "   border-width:3px;\n"
                                 "   border-style: solid;\n"
                                 "}\n"
                                 "QLabel\n"
                                 "{\n"
                                 "border:none;\n"
                                 "}\n"
                                 "QTextEdit\n"
                                 "{\n"
                                 "  background-color:#d7d5d9;\n"
                                 "   color: black;\n"
                                 "   font: italic;\n"
                                 "   font-size:30px;\n"
                                 "   border-color:#018185;\n"
                                 "   border-width:3px;\n"
                                 "   border-style: solid;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 " background-color:#393b3f;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1051, 761))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.encode_QTextEdit = QtWidgets.QTextEdit(self.tab)
        self.encode_QTextEdit.setGeometry(QtCore.QRect(30, 70, 971, 151))
        self.encode_QTextEdit.setStyleSheet("color:#018185;")
        self.encode_QTextEdit.setObjectName("encode_QTextEdit")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 30, 961, 34))
        self.label.setObjectName("label")
        self.decode_QTextEdit = QtWidgets.QTextEdit(self.tab)
        self.decode_QTextEdit.setGeometry(QtCore.QRect(30, 490, 971, 151))
        self.decode_QTextEdit.setStyleSheet("color:#018185;")
        self.decode_QTextEdit.setObjectName("decode_QTextEdit")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 450, 961, 34))
        self.label_2.setObjectName("label_2")
        self.encode_QPushButton = QtWidgets.QPushButton(self.tab)
        self.encode_QPushButton.setGeometry(QtCore.QRect(60, 280, 231, 111))
        self.encode_QPushButton.setObjectName("encode_QPushButton")
        self.decode_QPushButton = QtWidgets.QPushButton(self.tab)
        self.decode_QPushButton.setGeometry(QtCore.QRect(750, 280, 231, 111))
        self.decode_QPushButton.setObjectName("decode_QPushButton")
        self.error_QTextEdit = QtWidgets.QTextEdit(self.tab)
        self.error_QTextEdit.setGeometry(QtCore.QRect(320, 280, 401, 111))
        self.error_QTextEdit.setObjectName("error_QTextEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.orig_im_QLabel = QtWidgets.QLabel(self.tab_3)
        self.orig_im_QLabel.setGeometry(QtCore.QRect(30, 30, 961, 621))
        self.orig_im_QLabel.setText("")
        self.orig_im_QLabel.setObjectName("orig_im_QLabel")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 961, 621))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.error_QTextEdit.setEnabled(False)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Текст для шифрования"))
        self.label_2.setText(_translate("MainWindow", "Расшифрованный текст"))
        self.encode_QPushButton.setText(_translate("MainWindow", " Зашифровать"))
        self.decode_QPushButton.setText(_translate("MainWindow", "Расшифровать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Ввод"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Исходное"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Модифицированное"))
