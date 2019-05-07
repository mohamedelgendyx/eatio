from OpenGL.GLUT import *
import numpy as np
from gameobject import *


class HomeObject_1(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=2.5, scaleY=1.5, scaleZ=2, rotY=0, r1=1, g1=0.2, b1=0.6, r2=1, g2=0.7,
                 b2=1, al=1):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.r1 = r1
        self.g1 = g1
        self.b1 = b1
        self.r2 = r2
        self.g2 = g2
        self.b2 = b2
        self.alpha = al
        self.Length = 5
        self.width = 4
        self.area = 20

    def block(self, r, b, g, x, y, z, s1, s2, s3, l, a):
        self.applyParentTransform()
        glColor4f(r, b, g, a)
        glTranslate(x, y, z)
        glScale(s1, s2, s3)
        glutSolidCube(l)

    def draw(self):
        self.block(self.r1, self.g1, self.b1, 0, .2, 0, 1, .2, 1, 2, a=self.alpha)
        self.block(self.r2, self.g2, self.b2, 0, 1.2 + .2, 0, 1, 1, 1, 2, a=self.alpha)
        self.block(.25, 0.25, 0.25, 0, 2.4, 0, 1.1, .1, 1.1, 2, a=self.alpha)  # roof
        self.block(.25, .25, .25, -.65, 1.3 + .2, -1.0001, .5, .5, 0, 1, a=self.alpha)  # window
        self.block(.25, .25, .25, .65, 1.3 + .2, -1.0001, .5, .5, 0, 1, a=self.alpha)
        self.block(.25, .25, .25, 0, 0.45 + .2, -1.0001, .45, 1.3, 0, 1, a=self.alpha)  # door


class HomeObject_2(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=0.85, scaleY=0.7, scaleZ=1, rotY=0, al=1):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.Length = 3.5
        self.width = 5.95
        self.alpha = al
        self.area = 20.825

    def block(self, r, b, g, x, y, z, s1, s2, s3, l, a):
        self.applyParentTransform()
        glColor4f(r, b, g, a)
        glTranslate(x, y, z)
        glScale(s1, s2, s3)
        glutSolidCube(l)

    def draw(self):
        self.block(1, .2, 0, 0, 1.8, 0, 1, .5, .5, 7, a=self.alpha)
        self.block(1, .35, 0, 0, 8.57 + 1.8, 0, 1, 2, .5, 7, a=self.alpha)
        self.block(.25, .25, .25, 0, 16.1 + 1.8, 0, 1.1, .1, .55, 7, a=self.alpha)  # roof
        self.block(1, 1, 1, -3.3, 8.57 + 1.8, -1.6, 1, 28, 1, .5, a=self.alpha)  # Right white part
        self.block(1, 1, 1, 3.3, 8.57 + 1.8, -1.6, 1, 28, 1, .5, a=self.alpha)  # Left white part
        self.block(.25, .25, .25, 0, .7 + 1.8, -1.79, 1, 4, 0, 1, a=self.alpha)  # door

        # windows
        for i in np.arange(2.3, 13.8, 2.3):
            self.block(.25, .25, .25, 1.16, 2 + 1.8, -1.79, 1, 2, 0, 1, a=self.alpha)
            self.block(.25, .25, .25, 1.16, 2 + 1.8 + i, -1.79, 1, 2, 0, 1, a=self.alpha)

            self.block(.25, .25, .25, 2.28, 2 + 1.8, -1.79, 1, 2, 0, 1, a=self.alpha)
            self.block(.25, .25, .25, 2.28, 2 + 1.8 + i, -1.79, 1, 2, 0, 1, a=self.alpha)

            self.block(.25, .25, .25, -2.28, 2 + 1.8, -1.79, 1, 2, 0, 1, a=self.alpha)
            self.block(.25, .25, .25, -2.28, 2 + 1.8 + i, -1.79, 1, 2, 0, 1, a=self.alpha)

            self.block(.25, .25, .25, -1.16, 2 + 1.8, -1.79, 1, 2, 0, 1, a=self.alpha)
            self.block(.25, .25, .25, -1.16, 2 + 1.8 + i, -1.79, 1, 2, 0, 1, a=self.alpha)


class HomeObject_3(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0, r=0.8, g=1, b=0.4, al=1):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.r = r
        self.g = g
        self.b = b
        self.alpha = al
        self.Length = 9
        self.width = 9
        self.area = 81

    def block(self, r, b, g, x, y, z, s1, s2, s3, l, a):
        self.applyParentTransform()
        glColor4f(r, b, g, a)
        glTranslate(x, y, z)
        glScale(s1, s2, s3)
        glutSolidCube(l)

    def draw(self):
        self.block(self.r, self.g, self.b, 0, 18, 0, 1, 4, 1, 9, a=self.alpha)

        # windows
        for i in np.arange(0, 29, 4):
            self.block(.25, .25, .25, 0, -12 + 18 + i, 0, .85, .3, 1.001, 9, a=self.alpha)
            self.block(.25, .25, .25, 4.55, -12 + 18 + i, 0, 0, .3, .85, 9, a=self.alpha)
            self.block(.25, .25, .25, -4.55, -12 + 18 + i, 0, 0, .3, .85, 9, a=self.alpha)


class HomeObject_4(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0, r=1, g=0, b=0, al=1):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.r = r
        self.g = g
        self.b = b
        self.alpha = al
        self.Length = 5
        self.width = 5
        self.area = 25

    def block(self, r, b, g, x, y, z, s1, s2, s3, l, a):
        self.applyParentTransform()
        glColor4f(r, b, g, a)
        glTranslate(x, y, z)
        glScale(s1, s2, s3)
        glutSolidCube(l)

    def draw(self):
        self.block(self.r, self.g, self.b, 0, 3.75, 0, 1, 1.5, 1, 5, a=self.alpha)
        self.block(.25, .25, .25, 0, 3.8 + 3.75, 0, .9, 0, .9, 5, a=self.alpha)
        self.block(1, 1, 1, 0, 3.76 + 3.75, -2.75, 1, 0, .3, 5, a=self.alpha)
        self.block(1, 1, 1, 0, 3.75, -.6, 1.2, .3, 1.2, 5, a=self.alpha)
        self.block(0.25, .25, 0.25, -1.1, 2.2 + 3.75, -2.6, 1.2, 1.4, 0, 1.5, a=self.alpha)
        self.block(0.25, .25, 0.25, 1.1, 2.2 + 3.75, -2.6, 1.2, 1.5, 0, 1.5, a=self.alpha)


class HomeObject_5(GameObject):
    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0, al=1):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.Length = 3.8
        self.width = 4
        self.alpha = al
        self.area = 15.2

    def block(self, r, b, g, x, y, z, s1, s2, s3, l, a):
        self.applyParentTransform()
        glColor4f(r, b, g, a)
        glTranslate(x, y, z)
        glScale(s1, s2, s3)
        glutSolidCube(l)

    def draw(self):
        self.block(0.4, 0.1, 0.4, 0, 0, 0, 1, 2, 1, 4, a=self.alpha)
        self.block(1, 0.6, 0, 0, 0, 2.1, 3.7, .5, 0, 1, a=self.alpha)
        self.block(0.9, 0.1, 0.4, -1.2, 2.2, 2.1, .5, .9, 0, 2, a=self.alpha)
        self.block(0.9, 0.1, 0.4, 0, 2.2, 2.1, .5, .9, 0, 2, a=self.alpha)
        self.block(0.9, 0.1, 0.4, 1.2, 2.2, 2.1, .5, .9, 0, 2, a=self.alpha)
        self.block(.3, .3, .6, -1.2, -1.6, 2.1, .5, .8, 0, 2, a=self.alpha)
        self.block(.3, .3, .6, 1.2, -1.6, 2.1, .5, .8, 0, 2, a=self.alpha)
        self.block(0, 0, 0, 0, -2.4, 2.1, .5, 1.1, 0, 2, a=self.alpha)
        self.block(0.3, 0.8, 1, 0, 4, 0, 4, .5, 4, 1, a=self.alpha)
        self.block(0, 0, .4, 2, 0, 0, .1, 2, 1, 4, a=self.alpha)
        self.block(0, 0, .4, -2, 0, 0, .1, 2, 1, 4, a=self.alpha)


class HomeObject_6(GameObject):
    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0, al=1):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.Length = 8.000008
        self.width = 8.000008
        self.alpha = al
        self.area = 64

    def block(self, r, b, g, x, y, z, s1, s2, s3, l, a):
        self.applyParentTransform()
        glColor4f(r, b, g, a)
        glTranslate(x, y, z)
        glScale(s1, s2, s3)
        glutSolidCube(l)

    def draw(self):
        self.block(0, 0, 0, 0, 5.2, 0, 8.000008, .25, 8.00008, 1, a=self.alpha)
        self.block(0, 0, 0, 0, 2.5, 0, 8.000008, .25, 8.00008, 1, a=self.alpha)
        self.block(0, 0, 0, 0, -.2, 0, 8.000008, .25, 8.00008, 1, a=self.alpha)
        self.block(0, 0, 0, 0, -2.7, 0, 8.000008, .25, 8.00008, 1, a=self.alpha)
        self.block(0, 0, 0, 0, 8, 0, 8.000008, .25, 8.00008, 1, a=self.alpha)
        self.block(0, 0, 0, 0, -5.2, 0, 8.000008, .25, 8.00008, 1, a=self.alpha)
        self.block(0, 0, 0, 0, -8, 0, 8.000008, .25, 8.00008, 1, a=self.alpha)
        self.block(0, 0, 0, 2, 0, 0, .125, 16, 8, 1, a=self.alpha)
        self.block(0, 0, 0, 0, 0, 0, .125, 16, 8, 1, a=self.alpha)
        self.block(0, 0, 0, -2, 0, 0, .125, 16, 8, 1, a=self.alpha)
        self.block(0, 0, 0, 0, 0, 2, 8, 16, .125, 1, a=self.alpha)
        self.block(0, 0, 0, 0, 0, 0, 8, 16, .125, 1, a=self.alpha)
        self.block(0, 0, 0, 0, 0, -2, 8, 16, .125, 1, a=self.alpha)
        self.block(0.4, 0.2, 0.9, 0, 0, 0, 2, 4, 2, 4, a=self.alpha)
