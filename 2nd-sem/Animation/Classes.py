import math as m
import random

import pygame
import random as r


class Plane:
    def __init__(self, x, y_stat, phi, Ay, vx, omega, image):
        super().__init__()
        self.image = image
        self.x = x
        self.y_stat = y_stat
        self.phi = phi
        self.A = Ay
        self.vx = vx
        self.omega = omega

    def get_coords(self):
        return (self.x, self.y_stat + self.A * m.sin(m.radians(self.phi)))

    def move(self, secs):
        self.x += self.vx * secs
        self.phi += secs * self.omega
        if (self.phi > 2 * m.pi):
            self.phi -= 2 * m.pi

    def draw(self, surface):
        surface.blit(self.image, self.get_coords())


class Bomb:
    def __init__(self, x, y, vy, ay, image):
        super().__init__()
        self.image = image
        self.x = x
        self.y = y
        self.vy = vy
        self.ay = ay

    def get_coords(self):
        return self.x, self.y

    def move(self, secs):
        self.y += self.vy * secs

    def draw(self, surface):
        surface.blit(self.image, self.get_coords())


class Objs:
    def __init__(self, max_l, max_r):
        self.objs_l = []
        self.objs_r = []
        self.objs_v = []
        self.max_l = max_l
        self.max_r = max_r
        self.max_v = 5

    def move(self, secs, surface):
        x, y, xsize, ysize = surface.get_rect()
        # print(x, y, xsize, ysize)
        i = 0
        while i < len(self.objs_l):
            obj = self.objs_l[i]
            obj.move(secs)
            ox, oy = obj.get_coords()
            if not (x <= ox <= x + xsize and y <= oy <= y + ysize):
                self.delete_obj_l(i)
                i -= 1
            i += 1

        i = 0
        while i < len(self.objs_r):
            obj = self.objs_r[i]
            obj.move(secs)
            ox, oy = obj.get_coords()
            # print(ox, oy)
            if not (x < ox < x + xsize and y < oy < y + ysize):
                self.delete_obj_r(i)
                i -= 1
            i += 1

        i = 0
        while i < len(self.objs_v):
            obj = self.objs_v[i]
            obj.move(secs)
            ox, oy = obj.get_coords()
            # print(ox, oy)
            if not (x < ox < x + xsize and y < oy < y + ysize):
                self.delete_obj_v(i)
                i -= 1
            i += 1

    def draw(self, surface, image, image_r, image_v):
        while (len(self.objs_l) < self.max_l):
            self.create_obj(Plane, 'l', image)

        while (len(self.objs_r) < self.max_r):
            self.create_obj(Plane, 'r', image_r)

        while (len(self.objs_v) < self.max_v):
            obj = random.choice(self.objs_l + self.objs_r)
            self.create_v_obj(Bomb, *obj.get_coords(), image_v)

        for i in range(len(self.objs_l)):
            self.objs_l[i].draw(surface)

        for i in range(len(self.objs_r)):
            self.objs_r[i].draw(surface)

        for i in range(len(self.objs_v)):
            self.objs_v[i].draw(surface)

    def delete_obj_l(self, index):
        del self.objs_l[index]

    def delete_obj_r(self, index):
        del self.objs_r[index]

    def delete_obj_v(self, index):
        del self.objs_v[index]

    def create_obj(self, _class, typ, image):
        if typ == "l":
            new_obj = _class(0, r.randint(200, 300), r.randint(-90, 90), r.randint(10, 30), r.random() / 2 + 0.1,
                             r.random() / 3 * 2 + 0.1, image)
            self.objs_l.append(new_obj)
        if typ == "r":
            new_obj = _class(1599, r.randint(200, 300), r.randint(-90, 90), r.randint(10, 30), -(r.random() / 2 + 0.1),
                             r.random() / 3 * 2 + 0.1, image)
            self.objs_r.append(new_obj)


    def create_v_obj(self, _class, x, y, image):
        new_obj = _class(x, y, r.random() + 0.15, 0, image)
        self.objs_v.append(new_obj)
