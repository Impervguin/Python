from Classes import Point, Line
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap


class Canvas(QPixmap):
    def draw_point(self, point: Point, color=QColor('black'), width=3):
        painter = QPainter(self)
        pen = QPen()
        pen.setColor(color)
        pen.setWidth(width)
        painter.setPen(pen)
        painter.drawPoint(*point.get_coords())
        painter.end()

    def draw_line(self, line: Line, color=QColor('black'), width=3):
        painter = QPainter(self)
        pen = QPen()
        pen.setColor(color)
        pen.setWidth(width)
        painter.setPen(pen)
        painter.drawLine(*line.get_bord_coords(self.width(), self.height()))
        painter.end()