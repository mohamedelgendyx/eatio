from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
from random import *

from gameobject import *


class Car1(GameObject):
    def onFrameTick(self, dt):
        super().onFrameTick(dt)

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.a=1
        self.Length=0
        self.width=0
    def draw(self):
        # Lower
        self.applyParentTransform()
        glColor3f(1, 0.15, 0.3)
        glScalef(1, 0.25, 0.5)
        glutSolidCube(5)
        glColor3f(0, 0, 0)
        glutWireCube(5)
        # Upper

        # Upper Body
        self.applyParentTransform()
        glColor3f(1, 0.15, 0.3)
        glTranslate(0, 1.25, 0)
        glScalef(0.5, 0.25, 0.5)
        glutSolidCube(5)
        glColor3f(0, 0, 0)
        glutWireCube(5)

        # front Glass
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(1.3, 1.3, 0)
        glScalef(0, 0.22, 0.43)
        glutSolidCube(5)

        # left Glass
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glRotate(90, 0, 1, 0)
        glTranslate(1.3, 1.3, 0)
        glScalef(0, 0.21, 0.42)
        glutSolidCube(5)

        # Right Glass
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(1.3, 1.3, 0)
        glScalef(0, 0.21, 0.42)
        glutSolidCube(5)

        # back glass
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glRotate(180, 0, 1, 0)
        glTranslate(1.3, 1.3, 0)
        glScalef(0, 0.22, 0.43)
        glutSolidCube(5)

        # Wheels

        # Right front
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(2, -2.5 * 0.2, 2.5 * 0.5)
        glScale(0.3, 0.3, 0.3)
        glutSolidCube(2)
        # inside
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(2, -2.5 * 0.2, 1.6)
        glScale(0.2, 0.2, 0)
        glutSolidCube(2)

        # Left front
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(2, -2.5 * 0.2, -2.5 * 0.5)
        glScale(0.3, 0.3, 0.3)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(2, -2.5 * 0.2, -1.6)
        glScale(0.2, 0.2, 0)
        glutSolidCube(2)

        # Right back
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(-2, -2.5 * 0.2, 2.5 * 0.5)
        glScale(0.3, 0.3, 0.3)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(-2, -2.5 * 0.2, 1.6)
        glScale(0.2, 0.2, 0)
        glutSolidCube(2)

        # Left back
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(-2, -2.5 * 0.2, -2.5 * 0.5)
        glScale(0.3, 0.3, 0.3)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(-2, -2.5 * 0.2, -1.6)
        glScale(0.2, 0.2, 0)
        glutSolidCube(2)

        # Lamps
        # Right
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(2.52, 0.2, 0.7)
        glScale(0, 0.2, 0.2)
        glutSolidCube(3)

        # Left
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(2.52, 0.2, -0.7)
        glScale(0, 0.2, 0.2)
        glutSolidCube(3)


class Car2(GameObject):
    def onFrameTick(self, dt):
        super().onFrameTick(dt)

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.a=1
        self.Length=0
        self.width=0
    def draw(self):
        # Lower
        self.applyParentTransform()
        glColor3f(0.19, 0.8, 0.65)
        glScalef(1, 0.25, 0.5)
        glutSolidCube(5)
        glColor3f(0, 0, 0)
        glutWireCube(5)

        # Upper

        # Upper Body
        self.applyParentTransform()
        glColor3f(0.19, 0.8, 0.65)
        glTranslate(1, 1.26, 0)
        glScalef(0.3, 0.25, 0.5)
        glutSolidCube(5)
        glColor3f(0, 0, 0)
        glutWireCube(5)

        # front Glass
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(1.8, 1.3, 0)
        glScalef(0, 0.22, 0.43)
        glutSolidCube(5)

        # left Glass
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(1, 1.3, -1.3)
        glRotate(90, 0, 1, 0)
        glScalef(0, 0.2, 0.23)
        glutSolidCube(5)

        # Right Glass
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(1.1, 1.3, 1.35)
        glRotate(-90, 0, 1, 0)
        glScalef(0, 0.2, 0.23)
        glutSolidCube(5)

        # back glass
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(0.2, 1.3, 0)
        glScalef(0, 0.22, 0.43)
        glutSolidCube(5)

        # Wheels

        # Right front
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glTranslate(2, -2.5 * 0.2, 2.5 * 0.5)
        glScale(0.3, 0.3, 0.3)
        glutSolidCube(2)
        # inside
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(2, -2.5 * 0.2, 1.6)
        glScale(0.2, 0.2, 0)
        glutSolidCube(2)

        # Left front
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glTranslate(2, -2.5 * 0.2, -2.5 * 0.5)
        glScale(0.3, 0.3, 0.3)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(2, -2.5 * 0.2, -1.6)
        glScale(0.2, 0.2, 0)
        glutSolidCube(2)

        # Right back
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glTranslate(-2, -2.5 * 0.2, 2.5 * 0.5)
        glScale(0.3, 0.3, 0.3)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(-2, -2.5 * 0.2, 1.6)
        glScale(0.2, 0.2, 0)
        glutSolidCube(2)

        # Left back
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glTranslate(-2, -2.5 * 0.2, -2.5 * 0.5)
        glScale(0.3, 0.3, 0.3)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(-2, -2.5 * 0.2, -1.6)
        glScale(0.2, 0.2, 0)
        glutSolidCube(2)

        # Lamps
        # Right
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(2.52, 0.2, 0.7)
        glScale(0, 0.2, 0.2)
        glutSolidCube(3)

        # Left
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(2.52, 0.2, -0.7)
        glScale(0, 0.2, 0.2)
        glutSolidCube(3)


class Car_bus(GameObject):
    def onFrameTick(self, dt):
        super().onFrameTick(dt)

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.a = 1
        self.Length=5
        self.width=12.5
    def draw(self):
        # Body
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(self.a, 0.8, 0.5)
        glScalef(2.5, 1, 1)
        glutSolidCube(5)
        glColor3f(0, 0, 0)
        glutWireCube(5)

        # Glass
        # front
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(6.3, 1.3, 0)
        glScalef(0, 0.4, 0.9)
        glutSolidCube(5)

        # back
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glTranslate(-6.3, 1.3, 0)
        glScalef(0, 0.4, 0.9)
        glutSolidCube(5)

        # right
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(2.6, 1.7, 5)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(2.6, 1.7, 2.5)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(2.6, 1.7, 0)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(2.6, 1.7, -2.5)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(2.6, 1.7, -5)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)

        # left
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(-2.6, 1.7, 5)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(-2.6, 1.7, 2.5)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(-2.6, 1.7, 0)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(-2.6, 1.7, -2.5)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(-2.6, 1.7, -5)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)

        # Wheels

        # Right front
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(4, -2, 2.5)
        glScale(0.6, 0.6, 0.6)
        glutSolidCube(2)
        # inside
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(4, -2, 3.2)
        glScale(0.4, 0.4, 0)
        glutSolidCube(2)

        # Left front
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(4, -2, -2.5)
        glScale(0.6, 0.6, 0.6)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(4, -2, -3.2)
        glScale(0.4, 0.4, 0)
        glutSolidCube(2)

        # Right back
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(-4, -2, 2.5)
        glScale(0.6, 0.6, 0.6)
        glutSolidCube(2)
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(-2, -2, 2.5)
        glScale(0.6, 0.6, 0.6)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(-4, -2, 3.2)
        glScale(0.4, 0.4, 0)
        glutSolidCube(2)
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(-2, -2, 3.2)
        glScale(0.4, 0.4, 0)
        glutSolidCube(2)

        # Left back
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(-4, -2, -2.5)
        glScale(0.6, 0.6, 0.6)
        glutSolidCube(2)
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(-2, -2, -2.5)
        glScale(0.6, 0.6, 0.6)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(-4, -2, -3.2)
        glScale(0.4, 0.4, 0)
        glutSolidCube(2)
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(-2, -2, -3.2)
        glScale(0.4, 0.4, 0)
        glutSolidCube(2)

        # Lamps
        # Left
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(6.3, -1, -1.5)
        glScale(0, 0.3, 0.4)
        glutSolidCube(3)

        # Right
        self.applyParentTransform()
        glRotate(0, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(6.3, -1, 1.5)
        glScale(0, 0.3, 0.4)
        glutSolidCube(3)


class CarTaxi(GameObject):
    def onFrameTick(self, dt):
        super().onFrameTick(dt)

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.a=0
        self.Length =0
        self.width =0

    def draw(self):
        # windshield
        self.applyParentTransform()
        glColor3f(.171, .171, .167)
        glTranslate(1.05, 1.5, 0)
        glRotate(20, 0, 0, 1)
        glScale(.02, 0.22, 0.45)
        glLineWidth(1.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(.171, .171, .167)
        glTranslate(-2, 1.5, 0)
        glRotate(-20, 0, 0, 1)
        glScale(.02, 0.22, 0.45)
        glLineWidth(1.3)
        glutSolidCube(5)

        # sidewindows
        self.applyParentTransform()
        glColor3f(.171, .171, .167)
        glTranslate(-.472, 1.55, 1.125)
        glRotate(90, 0, 1, 0)
        glScale(.02, 0.18, 0.538)
        glLineWidth(1.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(.171, .171, .167)
        glTranslate(-.472, 1.55, -1.125)
        glRotate(90, 0, 1, 0)
        glScale(.02, 0.18, 0.538)
        glLineWidth(1.3)
        glutSolidCube(5)

        # innerfill
        for i in range(60, 0, -1):
            self.applyParentTransform()
            glColor3f(.8203, .832, .8671)
            glTranslate(-.48, 2 - (i / 68), 0)
            glRotate(90, 0, 0, 1)
            glScale(.0, .515 + (i / 390), 0.45)
            glLineWidth(1.3)
            glutSolidCube(5)

        # bottom cabin
        # mid
        self.applyParentTransform()
        glColor3f(.99609, .8007, .18359)
        glTranslate(-.4, .7, 0)
        glScale(.7, 0.18, 0.45)
        glutSolidCube(5)

        # front
        self.applyParentTransform()
        glColor3f(.2, .2, .2)
        glTranslate(1.95, .7, 0)
        glScale(.3, 0.19, 0.45)
        glLineWidth(1.3)
        glutWireCube(5)
        self.applyParentTransform()
        glColor3f(.99609, .8007, .18359)
        glTranslate(1.95, .7, 0)
        glScale(.3, 0.19, 0.45)
        glutSolidCube(5)

        # rear
        self.applyParentTransform()
        glColor3f(.2, .2, .2)
        glTranslate(-2.6, .7, 0)
        glScale(.25, 0.19, 0.45)
        glLineWidth(1.3)
        glutWireCube(5)
        self.applyParentTransform()
        glColor3f(.99609, .8007, .18359)
        glTranslate(-2.6, .7, 0)
        glScale(.25, 0.19, 0.45)
        glutSolidCube(5)

        # wheels
        self.applyParentTransform()
        glColor3f(.0, .0, .0)
        glTranslate(1.5, .5, 0)
        glScale(.13, 0.13, .495)
        glLineWidth(1.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(.0, .0, .0)
        glTranslate(-1.9, .5, 0)
        glScale(.13, 0.13, .495)
        glLineWidth(1.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(.6796, .6953, .7304)
        glTranslate(1.5, .5, 0)
        glScale(.07, 0.07, .535)
        glLineWidth(1.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(.6796, .6953, .7304)
        glTranslate(-1.9, .5, 0)
        glScale(.07, 0.07, .535)
        glLineWidth(1.3)
        glutSolidCube(5)

        # taxilable
        self.applyParentTransform()
        glColor3f(.9648, .9609, .8789)
        glTranslate(-.1, 2.4, -.38)
        glScale(.03, .03, 0.1)
        glLineWidth(1.3)
        glutSolidCube(5)

        # top
        self.applyParentTransform()
        glColor3f(.99609, .8007, .18359)
        glTranslate(-.48, 2.01, 0)
        glRotate(90, 0, 0, 1)
        glScale(.1, .515, 0.45)
        glLineWidth(1.3)
        glutSolidCube(5)

        # headlights
        self.applyParentTransform()
        glColor3f(1, 1, 1)
        glTranslate(2.58, .7, .6)
        glRotate(90, 0, 1, 0)
        glScale(.06, 0.06, 0.09)
        glLineWidth(1.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(1, 1, 1)
        glTranslate(2.58, .7, -.6)
        glRotate(90, 0, 1, 0)
        glScale(.06, 0.06, 0.09)
        glLineWidth(1.3)
        glutSolidCube(5)

        # taillights
        self.applyParentTransform()
        glColor3f(.54296, 0, 0)
        glTranslate(-3.06, .7, .6)
        glRotate(90, 0, 1, 0)
        glScale(.06, 0.06, 0.09)
        glLineWidth(1.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(.54296, 0, 0)
        glTranslate(-3.06, .7, -.6)
        glRotate(90, 0, 1, 0)
        glScale(.06, 0.06, 0.09)
        glLineWidth(1.3)
        glutSolidCube(5)


class CarPolice(GameObject):
    def onFrameTick(self, dt):
        super().onFrameTick(dt)

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.a=0
        self.Length =0
        self.width =0

    def draw(self):
        # windshield
        self.applyParentTransform()
        glColor3f(.171, .171, .167)
        glTranslate(1.05, 1.4, 0)
        glRotate(20, 0, 0, 1)
        glScale(.02, 0.22, 0.45)
        glLineWidth(1.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(.171, .171, .167)
        glTranslate(-2, 1.4, 0)
        glRotate(-20, 0, 0, 1)
        glScale(.02, 0.22, 0.45)
        glLineWidth(1.3)
        glutSolidCube(5)

        # sidewindows
        self.applyParentTransform()
        glColor3f(.171, .171, .167)
        glTranslate(-.472, 1.45, 1.125)
        glRotate(90, 0, 1, 0)
        glScale(.02, 0.18, 0.538)
        glLineWidth(1.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(.171, .171, .167)
        glTranslate(-.472, 1.45, -1.125)
        glRotate(90, 0, 1, 0)
        glScale(.02, 0.18, 0.538)
        glLineWidth(1.3)
        glutSolidCube(5)

        # innerfill
        for i in range(60, 0, -1):
            self.applyParentTransform()
            glColor3f(.8203, .832, .8671)
            glTranslate(-.48, 1.9 - (i / 68), 0)
            glRotate(90, 0, 0, 1)
            glScale(.0, .515 + (i / 390), 0.45)
            glLineWidth(1.3)
            glutSolidCube(5)

        # sirens
        self.applyParentTransform()
        glColor3f(.148, .527, .781)
        glTranslate(-.31, 2, .38)
        glScale(.1, .1, 0.145)
        glLineWidth(1.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(.85, .269, .199)
        glTranslate(-.31, 2, -.38)
        glScale(.1, .1, 0.145)
        glLineWidth(1.3)
        glutSolidCube(5)

        # bottom cabin
        # mid
        self.applyParentTransform()
        glColor3f(.8203, .832, .8671)
        glTranslate(-.3, .6, 0)
        glScale(.6, 0.18, 0.45)
        glutSolidCube(5)

        # front
        self.applyParentTransform()
        glColor3f(.2, .2, .2)
        glTranslate(1.95, .6, 0)
        glScale(.3, 0.19, 0.45)
        glLineWidth(1.3)
        glutWireCube(5)
        self.applyParentTransform()
        glColor3f(.2734, .2773, .2578)
        glTranslate(1.95, .6, 0)
        glScale(.3, 0.19, 0.45)
        glutSolidCube(5)

        # rear
        self.applyParentTransform()
        glColor3f(.2, .2, .2)
        glTranslate(-2.6, .6, 0)
        glScale(.25, 0.19, 0.45)
        glLineWidth(1.3)
        glutWireCube(5)
        self.applyParentTransform()
        glColor3f(.2734, .2773, .2578)
        glTranslate(-2.6, .6, 0)
        glScale(.25, 0.19, 0.45)
        glutSolidCube(5)

        # wheels
        self.applyParentTransform()
        glColor3f(.0, .0, .0)
        glTranslate(1.5, .5, 0)
        glScale(.13, 0.13, .495)
        glLineWidth(1.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(.0, .0, .0)
        glTranslate(-1.9, .5, 0)
        glScale(.13, 0.13, .495)
        glLineWidth(1.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(.6796, .6953, .7304)
        glTranslate(1.5, .5, 0)
        glScale(.07, 0.07, .535)
        glLineWidth(1.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glColor3f(.6796, .6953, .7304)
        glTranslate(-1.9, .5, 0)
        glScale(.07, 0.07, .535)
        glLineWidth(1.3)
        glutSolidCube(5)

        # headlights
        self.applyParentTransform()
        glColor3f(1, 1, 1)
        glTranslate(2.58, .6, .6)
        glRotate(90, 0, 1, 0)
        glScale(.06, 0.06, 0.09)
        glLineWidth(1.3)
        glutSolidCube(5)

        self.applyParentTransform()
        glColor3f(1, 1, 1)
        glTranslate(2.58, .6, -.6)
        glRotate(90, 0, 1, 0)
        glScale(.06, 0.06, 0.09)
        glLineWidth(1.3)
        glutSolidCube(5)

        # taillights

        self.applyParentTransform()
        glColor3f(.54296, 0, 0)
        glTranslate(-3.06, .6, .6)
        glRotate(90, 0, 1, 0)
        glScale(.06, 0.06, 0.09)
        glLineWidth(1.3)
        glutSolidCube(5)

        self.applyParentTransform()
        glColor3f(.54296, 0, 0)
        glTranslate(-3.06, .6, -.6)
        glRotate(90, 0, 1, 0)
        glScale(.06, 0.06, 0.09)
        glLineWidth(1.3)
        glutSolidCube(5)

# first cycle
def fourthPart_1(obj):
    obj.rotY = 270
    # a7 = Animation(AnimationParams.posX, None, -94.25, 3)
    a8 = Animation(AnimationParams.posZ, None, -52.75, 3)
    a8.onAnimationFinished = lambda: startCycle_1(obj)
    # obj.startAnimation(a7)
    obj.startAnimation(a8)


def thirdPart_1(obj):
    obj.rotY = 180
    a5 = Animation(AnimationParams.posX, None, -96, 3)
    # a6 = Animation(AnimationParams.posZ, None, -93.5, 3)
    a5.onAnimationFinished = lambda: fourthPart_1(obj)
    obj.startAnimation(a5)
    # obj.startAnimation(a6)


def secondPart_1(obj):
    obj.rotY = 90
    # a3 = Animation(AnimationParams.posX, None, -35, 3)
    a4 = Animation(AnimationParams.posZ, None, -96, 3)
    a4.onAnimationFinished = lambda: thirdPart_1(obj)
    # obj.startAnimation(a3)
    obj.startAnimation(a4)


def startCycle_1(obj, offsetTime=0):
    obj.posX = -96
    obj.posZ = -52.75
    obj.rotY = 0
    a1 = Animation(AnimationParams.posX, None, -34, 3)
    a2 = Animation(AnimationParams.posZ, None, -52.75, 3)
    a1.onAnimationFinished = lambda: secondPart_1(obj)
    obj.startAnimation(a1)
    a1.currentProgress = (offsetTime / 3)
    obj.startAnimation(a2)
    a2.currentProgress = (offsetTime / 3)


# first cycle
def fourthPart_2(obj):
    obj.rotY = 270
    # a7 = Animation(AnimationParams.posX, None, -94.25, 3)
    a8 = Animation(AnimationParams.posZ, None, -52.75, 3)
    a8.onAnimationFinished = lambda: startCycle_2(obj)
    # obj.startAnimation(a7)
    obj.startAnimation(a8)


def thirdPart_2(obj):
    obj.rotY = 180
    a5 = Animation(AnimationParams.posX, None, 96, 3)
    # a6 = Animation(AnimationParams.posZ, None, -93.5, 3)
    a5.onAnimationFinished = lambda: fourthPart_2(obj)
    obj.startAnimation(a5)
    # obj.startAnimation(a6)


def secondPart_2(obj):
    obj.rotY = 90
    # a3 = Animation(AnimationParams.posX, None, -35, 3)
    a4 = Animation(AnimationParams.posZ, None, -96, 3)
    a4.onAnimationFinished = lambda: thirdPart_2(obj)
    # obj.startAnimation(a3)
    obj.startAnimation(a4)


def startCycle_2(obj, offsetTime=0):
    obj.posX = 96
    obj.posZ = -52.75
    obj.rotY = 0
    a1 = Animation(AnimationParams.posX, None, 34, 3 + offsetTime)
    a2 = Animation(AnimationParams.posZ, None, -52.75, 3 + offsetTime)
    a1.onAnimationFinished = lambda: secondPart_2(obj)
    obj.startAnimation(a1)
    obj.startAnimation(a2)
