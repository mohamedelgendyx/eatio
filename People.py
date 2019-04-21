from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
from random import *

Y=0
angle=0
upAdown=1
forward=1
X=0
rand=1.5

class people:

    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
        self.sx = 0
        self.sy = 0
        self.sz = 0
        self.rotAngle=0
        self.R=0
        self.G=0
        self.B=0

    def applyParentTransform(self):
        glLoadIdentity()
        glColor3f(self.R, self.G, self.B)
        glRotate(self.rotAngle+angle, 0, 1, 0)
        glTranslate(self.x,self.y,self.z+X)
        glScale(self.sx,self.sy,self.sz)


    def draw(self):
        self.applyParentTransform()
        glutSolidCube(2)

    def fe4ar(self):
        global Y
        global upAdown
        if Y > 0.3:
            upAdown = 0
        if Y < -0.3:
            upAdown = 1
        if upAdown:
            Y += 0.008
        else:
            Y -= 0.008

    def movement(self):
        global X
        global forward
        global rand
        global angle

        if X > rand:
            forward = False
            angle =  randrange(0, 9, 3)
        if X < -rand:
            forward = True
            #angle =  randrange(0, -90, -30)
        if forward:
            X += 0.008
        else:
            X -= 0.008

def drawA(p,x,y,z,sx,sy,sz,r,g,b):
    p = people()
    p.x = x
    p.y = y
    p.z = z
    p.sx = sx
    p.sy =sy
    p.sz = sz
    p.R = r
    p.G = g
    p.B = b
    p.draw()
    p.fe4ar()
    p.movement()


def Draww():

    global Y
    global X
    global forward
    global rand

    h=[]
    for i in range(22):
       h.append(people())

    drawA(h[0], -50, 2, -35, .8, 1.5, .5, 0.1, 0, 0.2)
    drawA(h[0], -50, 3.5 + Y, -35, .8, .5, .5, 241 / 255, 195 / 255, 125 / 255)
    drawA(h[0], -50, 4 + Y, -35, .8, .2, .5, 0.1, 0.2, 0.3)

    drawA(h[1], -60, 2, -35, .8, 1.5, .5, 0.5, .2, 0.2)
    drawA(h[1], -60, 3.5 + Y, -35, .8, .5, .5, 230 / 255, 135 / 255, 105 / 255)
    drawA(h[1], -60, 4 + Y, -35, .8, .2, .5, 0.1, 0.2, 0.3)
