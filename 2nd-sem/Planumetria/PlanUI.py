from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1612, 1466)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 60, 381, 34))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 180, 381, 34))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(750, 180, 381, 34))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(750, 60, 381, 34))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1190, 60, 381, 34))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1190, 180, 381, 34))
        self.label_6.setObjectName("label_6")
        self.addDot = QtWidgets.QPushButton(self.centralwidget)
        self.addDot.setGeometry(QtCore.QRect(160, 290, 241, 48))
        self.addDot.setObjectName("addDot")
        self.addLine = QtWidgets.QPushButton(self.centralwidget)
        self.addLine.setGeometry(QtCore.QRect(1020, 290, 261, 48))
        self.addLine.setObjectName("addLine")

        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(650, 290, 170, 50))



        self.outLabel = QtWidgets.QLabel(self.centralwidget)
        self.outLabel.setGeometry(QtCore.QRect(10, 1280, 1310, 171))
        self.outLabel.setText("")
        self.outLabel.setObjectName("outLabel")

        self.calcButton = QtWidgets.QPushButton(self.centralwidget)
        self.calcButton.setGeometry(QtCore.QRect(1320, 1340, 170, 50))

        self.graphWidget = QtWidgets.QLabel(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(10, 360, 1600, 900))
        self.graphWidget.setText("")
        self.graphWidget.setObjectName("graphWidget")
        self.xDotBox = QtWidgets.QSpinBox(self.centralwidget)
        self.xDotBox.setGeometry(QtCore.QRect(100, 90, 381, 49))
        self.xDotBox.setObjectName("xDotBox")
        self.xDotBox.setMinimum(0)
        self.xDotBox.setMaximum(self.graphWidget.size().width())
        self.yDotBox = QtWidgets.QSpinBox(self.centralwidget)
        self.yDotBox.setGeometry(QtCore.QRect(100, 210, 381, 49))
        self.yDotBox.setObjectName("yDotBox")
        self.yDotBox.setMinimum(0)
        self.yDotBox.setMaximum(self.graphWidget.size().height())

        self.y1DotBox = QtWidgets.QSpinBox(self.centralwidget)
        self.y1DotBox.setGeometry(QtCore.QRect(750, 210, 381, 49))
        self.y1DotBox.setObjectName("y1DotBox")
        self.y1DotBox.setMinimum(0)
        self.y1DotBox.setMaximum(self.graphWidget.size().height())
        self.x1DotBox = QtWidgets.QSpinBox(self.centralwidget)
        self.x1DotBox.setGeometry(QtCore.QRect(750, 90, 381, 49))
        self.x1DotBox.setObjectName("x1DotBox")
        self.x1DotBox.setMinimum(0)
        self.x1DotBox.setMaximum(self.graphWidget.size().width())


        self.y2DotBox = QtWidgets.QSpinBox(self.centralwidget)
        self.y2DotBox.setGeometry(QtCore.QRect(1190, 210, 381, 49))
        self.y2DotBox.setObjectName("y2DotBox")
        self.y2DotBox.setMinimum(0)
        self.y2DotBox.setMaximum(self.graphWidget.size().height())
        self.x2DotBox = QtWidgets.QSpinBox(self.centralwidget)
        self.x2DotBox.setGeometry(QtCore.QRect(1190, 90, 381, 49))
        self.x2DotBox.setObjectName("x2DotBox")
        self.x2DotBox.setMinimum(0)
        self.x2DotBox.setMaximum(self.graphWidget.size().width())

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Planumetria"))
        self.label.setText(_translate("MainWindow", "X точки"))
        self.label_2.setText(_translate("MainWindow", "Y точки"))
        self.label_3.setText(_translate("MainWindow", "Y точки 1"))
        self.label_4.setText(_translate("MainWindow", "X точки 1"))
        self.label_5.setText(_translate("MainWindow", "X точки 2"))
        self.label_6.setText(_translate("MainWindow", "Y точки 2"))
        self.addDot.setText(_translate("MainWindow", "Добавить точку"))
        self.addLine.setText(_translate("MainWindow", "Добавить прямую"))
        self.clearButton.setText(_translate("MainWindow", "Очистить"))
        self.calcButton.setText(_translate("MainWindow", "Рассчитать"))

