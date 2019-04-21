from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
from random import *
from gameobject import *


class CharacterObject(GameObject):

    def __init__(self, posX, posY, posZ, scaleX, scaleY, scaleZ, rotY):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.HeadDeltaY = 0
        self.HeadUpDown = 1

    def draw(self):
        self.applyParentTransform()
        glColor3f(0.1, 0, 0.2)
        glTranslate(0, 2, 0)
        glScale(.8, 1.5, .5)
        glutSolidCube(2)

        self.applyParentTransform()
        glColor3f(241 / 255, 195 / 255, 125 / 255)
        glTranslate(0, 3.5+self.HeadDeltaY, 0)
        glScale(.8, .5, .5)
        glutSolidCube(2)

        self.applyParentTransform()
        glColor3f(0.1, 0.2, 0.3)
        glTranslate(0, 4+self.HeadDeltaY, 0)
        glScale(.8, .2, .5)
        glutSolidCube(2)

    def onFrameTick(self, dt):
        super().onFrameTick(dt)
        if self.HeadDeltaY > 0.3:
            self.HeadUpDown = 0
        if self.HeadDeltaY < -0.3:
            self.HeadUpDown = 1
        if self.HeadUpDown:
            self.HeadDeltaY += dt*2
        else:
            self.HeadDeltaY -= dt*2
