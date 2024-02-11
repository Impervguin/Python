import sys
from Math import find_parallel_lines
from PyQt5 import QtCore, QtGui, QtWidgets
from Classes import Point, Line
from Graph import Canvas
from PyQt5.QtWidgets import QMainWindow, QApplication
from PlanUI import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.canvas = Canvas(self.graphWidget.width(), self.graphWidget.height())

        self.points = [Point(400, 800), Point(800, 800)]
        self.tmp_point = None
        self.lines = [Line(100, 100, 10, 100)]
        self.clear_graph()
        self.calculated = False
        self.addLine.clicked.connect(self.line_but_push)
        self.clearButton.clicked.connect(self.clear_graph)
        self.addDot.clicked.connect(self.point_but_push)
        self.calcButton.clicked.connect(self.calculate)

    def redraw_screen(self):
        p = self.points.copy()
        l = self.lines.copy()
        self.clear_graph()
        for ps in p:
            self.add_point(ps.x, ps.y)

        for ls in l:
            self.add_line(ls.p1.x, ls.p1.y, ls.p2.x, ls.p2.y)

        self.calculated = False

    def calculate(self):
        if len(self.points) < 2 or len(self.lines) == 0:
            self.outLabel.setText("Недостаточно данных")
            return 1
        p = find_parallel_lines(self.points, self.lines)
        if isinstance(p, int) and p == 2:
            self.outLabel.setText("Нет искомых параллельных линий")
            return
        self.draw_point(p[0], QtGui.QColor('blue'))
        self.draw_point(p[1], QtGui.QColor('blue'))
        self.draw_line(Line(p[0].x, p[0].y, p[1].x, p[1].y), QtGui.QColor('green'))
        self.outLabel.setText(f"Выделенной прямой паралльны {p[2]} прямых")
        self.calculated = True



    def add_line(self, x1, y1, x2, y2, color=QtGui.QColor('black')):
        if x1 == x2 and y1 == y2:
            self.outLabel.setText("Неверно задана точка.")
            return
        line = Line(x1, y1, x2, y2)
        if line not in self.lines:
            self.draw_line(line, color)
            self.lines.append(line)


    def draw_line(self, line, color):
        if self.calculated:
            self.redraw_screen()
        self.canvas.draw_line(line, width=5, color=color)
        self.refresh_graph()

    def add_point(self, x, y, color=QtGui.QColor('black')):
        point = Point(x, y)
        print(self.points)
        if point not in self.points:
            self.draw_point(point, color=color)
            self.points.append(point)


    def draw_point(self, point, color):
        if self.calculated:
            self.redraw_screen()
        self.canvas.draw_point(point, width=10, color=color)
        self.refresh_graph()

    def point_but_push(self):
        x, y = self.xDotBox.value(), self.yDotBox.value()
        self.add_point(x, y)

    def line_but_push(self):
        x1, y1, x2, y2 = self.x1DotBox.value(), self.y1DotBox.value(), self.x2DotBox.value(), self.y2DotBox.value()
        self.add_line(x1, y1, x2, y2)



    def refresh_graph(self):
        self.graphWidget.setPixmap(self.canvas)

    def clear_graph(self):
        self.canvas.fill(QtGui.QColor('white'))
        self.calculated = False
        self.refresh_graph()
        self.points.clear()
        self.lines.clear()

    def mousePressEvent(self, e):
        x, y = e.x() - self.graphWidget.x(), e.y() - self.graphWidget.y()
        if not (0 <= x < self.graphWidget.width() and 0 <= y < self.graphWidget.height()):
            return
        if (e.buttons() == QtCore.Qt.RightButton):
            self.line_click(x, y)
        if (e.buttons() == QtCore.Qt.LeftButton):
            self.point_click(x, y)

    def point_click(self, x, y):
        self.add_point(x, y)

    def line_click(self, x, y):
        if self.tmp_point is None:
            p = Point(x, y)
            self.draw_point(p, QtGui.QColor('red'))
            self.tmp_point = p
        else:
            self.draw_point(self.tmp_point, QtGui.QColor('white'))
            self.add_line(self.tmp_point.x, self.tmp_point.y, x, y)
            self.tmp_point = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wind = MyMainWindow()
    wind.show()
    sys.exit(app.exec_())
