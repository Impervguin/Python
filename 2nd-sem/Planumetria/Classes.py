EPS = 1e-3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    def get_coords(self):
        return *self.p1.get_coords(), *self.p2.get_coords()

    def get_bord_coords(self, bord_x, bord_y):
        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y

        x1, y1 = self.p1.x, self.p1.y
        while (x1 > 0 and y1 > 0) and (x1 < bord_x and y1 < bord_y):
            x1 -= dx
            y1 -= dy

        x2, y2 = self.p2.x, self.p2.y
        while (x2 > 0 and y2 > 0) and (x2 < bord_x and y2 < bord_y):
            x2 += dx
            y2 += dy

        return x1, y1, x2, y2

    def get_angle_coef(self):
        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y
        if dx == 0:
            return float('+inf')
        return dy / dx

    def parallel(self, other):
        if (self.get_angle_coef() == float('inf') and other.get_angle_coef() == float('inf')):
            return True
        return (abs(self.get_angle_coef() - other.get_angle_coef())) < EPS

    def __eq__(self, other):
        a1 = self.get_angle_coef()
        a2 = other.get_angle_coef()
        if a1 == a2 and a1 == float('inf'):
            if self.p1.x != other.p1.x:
                return False
            else:
                return True
        b1 = self.p1.y - a1 * self.p1.x
        b2 = other.p1.y - a1 * other.p1.x
        return a1 == a2 and b1 == b2


