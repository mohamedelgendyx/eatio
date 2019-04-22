from math import *

import numpy as np
from OpenGL.GL import *

z = 0
x = 0
y = 0
c = 0


def draw_circle(r=0.5, xc=0, yc=0, R=1, g=1, b=1, start=0, end=2 * pi):
    glBegin(GL_LINE_LOOP)
    glColor(R, g, b)
    for theta in np.arange(start, end, .03):
        x = xc + r * cos(theta)
        y = yc + r * sin(theta)
        glVertex(x, 0, y)
    glEnd()


class Road:
    def __init__(self):
        self.x = 0
        self.z = 0
        self.rotAngle = 0

    def applyParentTransform(self):
        glLoadIdentity()
        glTranslate(self.x, 0, self.z)
        glRotate(self.rotAngle * 90, 0, 1, 0)

    def draw(self):
        self.applyParentTransform()

        glBegin(GL_POLYGON)
        glColor(0.25, 0.3, 0.25)
        glVertex(-4, 0, -34)
        glVertex(-4, 0, 0)
        glVertex(4, 0, 0)
        glVertex(4, 0, -34)
        glEnd()
        for i in range(9, 29, 5):
            glColor(0.8, 0.8, 0.8)
            glBegin(GL_QUADS)
            glVertex(-0.4, 0, -1 * i + -1.5)
            glVertex(-0.4, 0, -1 * i + 1.5)
            glVertex(0.4, 0, -1 * i + 1.5)
            glVertex(0.4, 0, -1 * i + -1.5)
            glEnd()

        self.applyParentTransform()

    def draw1(self):
        self.applyParentTransform()
        glBegin(GL_LINES)
        glColor(0.95, 0.95, 0.95)
        glVertex(-4, 0, -34)
        glVertex(-4, 0, 0)
        glVertex(4, 0, 0)
        glVertex(4, 0, -34)
        glEnd()


def draw_roads():
    r = []
    b = []
    for i in range(31):
        r.append(Road())
    r[30].draw1()
    for i in range(24, 30):
        r[i].rotAngle = 1
        r[i].z = -50
        r[i].x = i % 24 * 33 - 65
        r[i].draw1()
    for i in range(6):
        r[i].rotAngle = 1
        r[i].z = -96
        r[i].x = i * 33 - 65
        r[i].draw1()
    for i in range(6, 12):
        r[i].rotAngle = 1
        r[i].z = -4
        r[i].x = i % 6 * 33 - 65
        r[i].draw1()
    for i in range(12, 15):
        r[i].z = -(i % 12) * 33
        r[i].x = 35
        r[i].draw1()

    for i in range(15, 18):
        r[i].z = -(i % 15) * 33
        r[i].x = -96
        r[i].draw1()

    for i in range(18, 21):
        r[i].z = -(i % 18) * 33
        r[i].x = 96
        r[i].draw1()
    for i in range(21, 24):
        r[i].z = -(i % 21) * 33
        r[i].x = -33
        r[i].draw1()
    for i in range(31):
        r[i].draw()


class betch():
    def __init__(self):
        self.x = 0
        self.z = 0
        self.rotAngle = 0

    def applyParentTransform(self):
        glLoadIdentity()
        glTranslate(self.x, 0, self.z)
        glRotate(self.rotAngle * 90, 0, 1, 0)

    def draw(self):
        self.applyParentTransform()
        glColor(.5, .8, .2)
        glBegin(GL_POLYGON)
        glVertex(12, 0, 0)
        glVertex(-12, 0, 0)
        glVertex(-12, 0, -38)
        glVertex(12, 0, -38)
        glEnd()
        glColor(1, 1, 1)
        glLineWidth(5)
        glBegin(GL_LINE_LOOP)
        glVertex(12, 0, 0)
        glVertex(-12, 0, 0)
        glVertex(-12, 0, -38)
        glVertex(12, 0, -38)
        glEnd()
        draw_circle(4.5, 0, -19)
        draw_circle(4, 0, 0, 1, 1, 1, pi)
        draw_circle(4, 0, -38, 1, 1, 1, 0, pi)
        glBegin(GL_LINES)
        glVertex(-12, 0, -19)
        glVertex(12, 0, -19)
        glEnd()


def draw_car_park():
    glColor(0.25, 0.3, 0.25)
    glBegin(GL_POLYGON)
    glVertex(-30, 0, -10)
    glVertex(-30, 0, -40)
    glVertex(32, 0, -40)
    glVertex(32, 0, -10)
    glEnd()
    glColor(0.95, 0.95, 0.95)
    glBegin(GL_LINE_LOOP)
    glVertex(-30, 0, -10)
    glVertex(-30, 0, -40)
    glVertex(32, 0, -40)
    glVertex(32, 0, -10)
    glEnd()
    glBegin(GL_LINES)
    glVertex(-30, 0, -15)
    glVertex(-14, 0, -15)
    glVertex(-30, 0, -20)
    glVertex(-14, 0, -20)
    glVertex(-30, 0, -25)
    glVertex(-14, 0, -25)
    glVertex(-30, 0, -30)
    glVertex(-14, 0, -30)
    glVertex(-30, 0, -35)
    glVertex(-14, 0, -35)
    glVertex(32, 0, -15)
    glVertex(14, 0, -15)
    glVertex(32, 0, -20)
    glVertex(14, 0, -20)
    glVertex(32, 0, -25)
    glVertex(14, 0, -25)
    glVertex(32, 0, -30)
    glVertex(14, 0, -30)
    glVertex(32, 0, -35)
    glVertex(14, 0, -35)
    glEnd()


class map():
    def __init__(self):
        pass

    def draw(self):
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        glColor(0.8, 0.8, 0.8)
        glBegin(GL_POLYGON)
        glVertex(-100, 0, 0)
        glVertex(-100, 0, -100)
        glVertex(100, 0, -100)
        glVertex(100, 0, 0)
        glEnd()
        glDisable(GL_DEPTH_TEST)
        draw_car_park()
        draw_roads()
        r = betch()
        r.z = -54
        r.x = 57
        r.draw()
        r1 = betch()
        r1.x = -55
        r1.z = -8
        r1.draw()


def drawMap():
    mainMap = map()
    mainMap.draw()
