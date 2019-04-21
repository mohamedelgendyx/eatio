from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
from random import *
from gameobject import *


class HomeObject_1(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0, r1=1, g1=0.2, b1=0.6, r2=1, g2=0.7, b2=1):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.r1 = r1
        self.g1 = g1
        self.b1 = b1
        self.r2 = r2
        self.g2 = g2
        self.b2 = b2

    def block(self, r, b, g, x, y, z, s1, s2, s3, l):
        self.applyParentTransform()
        glColor3f(r, b, g)
        glTranslate(x, y, z)
        glScale(s1, s2, s3)
        glutSolidCube(l)

    def draw(self):
        self.block(self.r1, self.g1, self.b1, 0, 0, 0, 1, .2, 1, 2)
        self.block(self.r2, self.g2, self.b2, 0, 1.2, 0, 1, 1, 1, 2)
        self.block(.25, 0.25, 0.25, 0, 2.2, 0, 1.1, .1, 1.2, 2)  # roof
        self.block(.25, .25, .25, -.65, 1.3, -1.001, .5, .5, 0, 1)  # window
        self.block(.25, .25, .25, .65, 1.3, -1.001, .5, .5, 0, 1)
        self.block(.25, .25, .25, 0, 0.45, -1.001, .45, 1.3, 0, 1)  # door


class HomeObject_2(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)

    def block(self, r, b, g, x, y, z, s1, s2, s3, l):
        self.applyParentTransform()
        glColor3f(r, b, g)
        glTranslate(x, y, z)
        glScale(s1, s2, s3)
        glutSolidCube(l)

    def draw(self):
        self.block(1, .2, 0, 0, 0, 0, 1, .5, .5, 7)
        self.block(1, .35, 0, 0, 8.57, 0, 1, 2, .5, 7)
        self.block(.25, .25, .25, 0, 16.1, 0, 1.1, .1, .55, 7)  # roof
        self.block(1, 1, 1, -3.3, 8.57, -1.6, 1, 28, 1, .5)  # Right white part
        self.block(1, 1, 1, 3.3, 8.57, -1.6, 1, 28, 1, .5)  # Left white part
        self.block(.25, .25, .25, 0, .7, -2.25, 1, 4, 0, 1)  # door

        for i in np.arange(2.3, 13.8, 2.3):  # windows
            self.block(.25, .25, .25, 1.16, 2, -2.25, 1, 2, 0, 1)
            self.block(.25, .25, .25, 1.16, 2 + i, -2.25, 1, 2, 0, 1)

            self.block(.25, .25, .25, 2.28, 2, -2.25, 1, 2, 0, 1)
            self.block(.25, .25, .25, 2.28, 2 + i, -2.25, 1, 2, 0, 1)

            self.block(.25, .25, .25, -2.28, 2, -2.25, 1, 2, 0, 1)
            self.block(.25, .25, .25, -2.28, 2 + i, -2.25, 1, 2, 0, 1)

            self.block(.25, .25, .25, -1.16, 2, -2.25, 1, 2, 0, 1)
            self.block(.25, .25, .25, -1.16, 2 + i, -2.25, 1, 2, 0, 1)


class HomeObject_3(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0, r=0.8, g=1, b=0.4):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.r = r
        self.g = g
        self.b = b

    def block(self, r, b, g, x, y, z, s1, s2, s3, l):
        self.applyParentTransform()
        glColor3f(r, b, g)
        glTranslate(x, y, z)
        glScale(s1, s2, s3)
        glutSolidCube(l)

    def draw(self):
        self.block(self.r, self.g, self.b, 0, 0, 0, 1, 4, 1, 9)
        for i in np.arange(0, 29, 4):  # windows
            self.block(.25, .25, .25, 0, -12 + i, 0, .85, .3, 1.01, 9)
            self.block(.25, .25, .25, 4.6, -12 + i, 0, 0, .3, .85, 9)
            self.block(.25, .25, .25, -4.6, -12 + i, 0, 0, .3, .85, 9)


class HomeObject_4(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0, r=1, g=0, b=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.r = r
        self.g = g
        self.b = b

    def block(self, r, b, g, x, y, z, s1, s2, s3, l):
        self.applyParentTransform()
        glColor3f(r, b, g)
        glTranslate(x, y, z)
        glScale(s1, s2, s3)
        glutSolidCube(l)

    def draw(self):
        self.block(self.r, self.g, self.b, 0, 0, 0, 1, 1.5, 1, 5)
        self.block(.25, .25, .25, 0, 3.76, 0, .9, 0, .9, 5)
        self.block(1, 1, 1, 0, 3.76, -2.75, 1, 0, .3, 5)
        self.block(1, 1, 1, 0, 0, -.6, 1.2, .3, 1.2, 5)
        self.block(0.25, .25, 0.25, -1.1, 2.2, -2.6, 1.2, 1.4, 0, 1.5)
        self.block(0.25, .25, 0.25, 1.1, 2.2, -2.6, 1.2, 1.5, 0, 1.5)
