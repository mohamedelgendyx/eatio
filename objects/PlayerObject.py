from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
from random import *
from gameobject import *


def draw_circle(r=0.5,z=0):
    glBegin(GL_POLYGON)

    for theta in np.arange(0, 2 * pi, .1):
        x =  r * sin(theta)
        y =  r * cos(theta)
        glVertex(x, 0.05+z, y)
    glEnd()

class PlayerObject(GameObject):

    def __init__(self, posX=randrange(-100, 100), posY=0, posZ= randrange(-100, 0), scaleX=1, scaleY=1, scaleZ=1, rotY=0,  radius=1, r=0, g=1, b=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.radius = radius
        self. xdis = randrange(-100, 100)
        self. zdis = randrange(-100, 0)
        self.r = r
        self.g = g
        self.b = b
        self.x = 0
        self.z = 0
        self.area = pi * self.radius *self.radius
    def update_area(self):
        self.area = pi * self.radius *self.radius
    def draw(self):
        self.applyParentTransform()
        glColor(0, 0, 0)
        draw_circle(self.radius, 0.03)
        draw_circle(self.radius)

        glColor(0, 1, 0)
        draw_circle(self.radius + self.radius * 0.1, -0.02)

        glLoadIdentity()
        glTranslate(self.posX + self.x, 0.05, self.posZ + self.z)
        glRotate(self.rotY, 0, 1, 0)
        glBegin(GL_POLYGON)
        glColor(0, 1, 0)
        glVertex(.2 + self.radius * 0.1, 0, self.radius * 0.1 * 2)
        glVertex(- .2 - self.radius * 0.1, 0, self.radius * 0.1 * 2)
        glVertex(0, 0, .346 + self.radius * 0.1 * 4)
        glEnd()
others = 3
list = []

for i in range(others):
        list.append(PlayerObject())

for i in range(others):
        list.append(PlayerObject())
        list[i].posZ=randrange(-100,0)
        list[i].posX=randrange(-100,100)

def draw_others():
        global others
        global list
        for i in range(others):
            if list[i].posX == list[i].xdis and list[i].posZ== list[i].zdis:
                list[i].xdis = randrange(-100, 100)
                list[i].zdis = randrange(-100, 0)
            else:
                if list[i].posX < list[i].xdis:
                    list[i].posX += .5
                    if list[i].posZ < list[i].zdis:
                        list[i].posZ += .5
                        list[i].rotY = 45
                        list[i].x = list[i].radius+.2
                        list[i].z = list[i].radius+.2
                    elif list[i].posZ > list[i].zdis:
                        list[i].posZ -= .5
                        list[i].rotY = 135
                        list[i].x =list[i].radius+.2
                        list[i].z = -list[i].radius-.2
                    else:
                        list[i].rotY = 90
                        list[i].x = list[i].radius+.2
                        list[i].z = 0

                elif list[i].posX > list[i].xdis:
                    list[i].posX -= .5
                    if list[i].posZ> list[i].zdis:
                        list[i].posZ-= .5
                        list[i].rotY = 225
                        list[i].x =-list[i].radius-.2
                        list[i].z = -list[i].radius-.2
                    elif list[i].posZ< list[i].zdis:
                        list[i].posZ+= .5
                        list[i].rotY = -45
                        list[i].x =-list[i].radius-.2
                        list[i].z = list[i].radius+.2
                    else:
                        list[i].rotY = - 90
                        list[i].x = -list[i].radius-.2
                        list[i].z = 0
                else:
                    if list[i].posZ > list[i].zdis:
                        list[i].posZ -= .5
                        list[i].rotY = 180
                        list[i].x = 0
                        list[i].z = -list[i].radius-.2
                    elif list[i].posZ < list[i].zdis:
                        list[i].posZ += .5
                        list[i].rotY = 0
                        list[i].x = 0
                        list[i].z =list[i].radius+.2

            list[i].draw()