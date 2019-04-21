from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
from random import *
from gameobject import *


class PlayerObject(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0, radius=1, r=0, g=1, b=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.radius = radius
        self.r = r
        self.g = g
        self.b = b

    def draw(self):
        self.applyParentTransform()
        glColor3f(self.r, self.g, self.b)
        glutSolidCube(1)
