from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QSpinBox, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap
from PyQt5.QtCore import QRect
import sys
from math import ceil

class Canvas(QPixmap):
    def draw_point(self, x, y, color=QColor('black')):
        painter = QPainter(self)
        pen = QPen()
        pen.setWidth(10)
        pen.setColor(color)
        painter.setPen(pen)
        painter.drawPoint(x, y)
        painter.end()

    def draw_circle(self, x, y, r, color=QColor('black')):
        painter = QPainter(self)
        pen = QPen()
        pen.setWidth(10)
        pen.setColor(color)
        painter.setPen(pen)
        painter.drawEllipse(x - r, y - r, 2 * r, 2 * r)
        painter.end()


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1650, 1400)
        self.canvas = QLabel(self)
        self.canvas.setGeometry(QRect(10, 360, 1600, 900))
        self.xDotBox = QSpinBox(self)
        self.xDotBox.setGeometry(QRect(100, 90, 380, 50))
        self.xDotBox.setMinimum(0)
        self.xDotBox.setMaximum(self.canvas.size().width())
        self.yDotBox = QSpinBox(self)
        self.yDotBox.setGeometry(QRect(100, 210, 380, 50))
        self.yDotBox.setMinimum(0)
        self.yDotBox.setMaximum(self.canvas.size().height())
        self.calcButton = QPushButton(self)
        self.calcButton.setGeometry(QRect(700, 200, 200, 50))
        self.calcButton.setText("Рассчитать")
        self.calcButton.clicked.connect(self.calculate)
        self.canv = Canvas(self.canvas.size().width(), self.canvas.size().height())
        self.canv.fill(QColor('white'))
        self.canvas.setPixmap(self.canv)
        self.points = []

    def add_point(self, x, y):
        self.canv.draw_point(x, y)
        self.canvas.setPixmap(self.canv)
        self.points.append([x, y])

    def mousePressEvent(self, e):
        x, y = e.x() - self.canvas.x(), e.y() - self.canvas.y()
        if not (0 <= x < self.canvas.width() and 0 <= y < self.canvas.height()):
            return
        self.add_point(x, y)
        print(x, y)

    def calculate(self):

        best = [self.points[0][0], self.points[0][1], float('inf')]
        print(self.points)

        for i in range(len(self.points)):
            now = [self.points[i][0], self.points[i][1], 0]
            for j in range(len(self.points)):
                r = ((self.points[j][0] - self.points[i][0]) ** 2 + (self.points[j][1] - self.points[i][1]) ** 2) ** 0.5
                if r > now[2]:
                    now[2] = r
            if best[2] > now[2]:
                best = [now[0], now[1], now[2]]
        print(best)
        self.canv.draw_circle(best[0], best[1], ceil(best[2]), color=QColor('red'))
        self.canvas.setPixmap(self.canv)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    wind = MyMainWindow()
    wind.show()
    sys.exit(app.exec_())
