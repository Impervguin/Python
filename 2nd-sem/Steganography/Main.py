import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from StenUI import Ui_MainWindow
from PIL import Image, ImageQt
import ImLib as il


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.encode_QPushButton.clicked.connect(self.encode)
        self.decode_QPushButton.clicked.connect(self.decode)

    def encode(self):
        t = self.encode_QTextEdit.toPlainText()
        if t == "":
            self.error_QTextEdit.setText("Не найдено текста для кодирования.")
            return
        fileName, _ = QFileDialog.getOpenFileName(self,
                                                  "Open Image",
                                                  "/home/impervguin/Projects/Programmin-Practice-2-sem/Python_labs/Steganography",
                                                  "Image Files (*.png *.jpg *.bmp)")
        im_before = Image.open(fileName)
        rc, im = il.encode_in_image(t, fileName)
        if rc == il.SMALL_FILE:
            self.error_QTextEdit.setText("Файл слишком маленький для кодирования.")
            return
        fn = os.path.split(fileName)
        new_name = os.path.join(*fn[:-1], "encoded_" + fn[-1])
        im.save(new_name, format="bmp")
        im_before = im_before.resize(size=(self.orig_im_QLabel.size().width(), self.orig_im_QLabel.size().height()))
        im = im.resize(size=(self.label_4.size().width(), self.label_4.size().height()))
        self.orig_im_QLabel.setPixmap(QtGui.QPixmap.fromImage(ImageQt.ImageQt(im_before)))
        self.label_4.setPixmap(QtGui.QPixmap.fromImage(ImageQt.ImageQt(im)))

    def decode(self):
        fileName, _ = QFileDialog.getOpenFileName(self,
                                                  "Open Image",
                                                  "/home/impervguin/Projects/Programmin-Practice-2-sem/Python_labs/Steganography",
                                                  "Image Files (*.png *.jpg *.bmp)")
        try:
            rc, t = il.decode_image(fileName)
        except BaseException:
            self.error_QTextEdit.setText("Ошибка, возможно в файле ничего не закодировано.")

        self.decode_QTextEdit.setText(t)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wind = MyMainWindow()
    wind.show()
    sys.exit(app.exec_())
