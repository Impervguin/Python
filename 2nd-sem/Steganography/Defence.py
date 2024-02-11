

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from PIL import Image, ImageDraw

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(445, 349)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(80, 40, 271, 48))
        self.pushButton.setText("Выберите котика!")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 120, 421, 201))
        self.label.setText("")
        self.pushButton.clicked.connect(self.choose_kotik)

    def choose_kotik(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                  "Open Image",
                                                  "/home/impervguin/Projects/Programmin-Practice-2-sem/Python_labs/Steganography",
                                                  "Image Files (*.png *.jpg *.bmp)")
        im = Image.open(fileName)
        draw = ImageDraw.Draw(im)
        w, h = im.size
        thicc = min(w, h) // 200 if min(w, h) // 200 > 0 else 1
        w_lines = w // 50
        line_width = w / w_lines
        for i in range(w_lines):
            draw.rectangle((line_width * i, 0, line_width * i + thicc, h), fill=(0, 0, 0), outline=(0, 0, 0))
        h_lines = h // 20
        line_height = h / h_lines
        for i in range(h_lines):

            draw.rectangle((0, line_height * i, w, line_height * i + thicc), fill=(0, 0, 0), outline=(0, 0, 0))
        fn = os.path.split(fileName)
        new_name = os.path.join(*fn[:-1], "jailed_" + fn[-1])
        im.save(new_name, format="bmp")
        self.label.setText("Котик в тюрьме(")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    wind = MyMainWindow()
    wind.show()
    sys.exit(app.exec_())