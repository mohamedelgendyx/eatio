from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
from random import *
from gameobject import *


class LightingObject(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)

    def draw(self):
        self.applyParentTransform()
        glColor3f(0.51, 0.72, 0.91)
        glScale(.4, 1, 0.5)
        glutSolidCube(0.5)

        self.applyParentTransform()
        glTranslate(0, 1.5, 0)
        glScale(.2, 5, 0.2)
        glutSolidCube(0.5)

        self.applyParentTransform()
        glTranslate(0.5, 2.65, 0)
        glScale(2, 0.1, 0.1)
        glutSolidCube(0.5)

        self.applyParentTransform()
        glTranslate(1.2, 2.58, 0)
        glScale(.9, 0.2, 0.5)
        glutSolidCube(0.5)


class ConeObject(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)

    def draw(self):
        self.applyParentTransform()
        glColor3f(0.89, 0.51, 0.1)
        glScale(1, 0.1, 1)
        glutSolidCube(.8)

        self.applyParentTransform()
        glRotate(-90, 1, 0, 0)
        glutSolidCone(.4, 1.5, 10, 10)


class CylinderObject_1(GameObject):
    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)

    def draw(self):
        self.applyParentTransform()
        glColor3f(0.67, 0.65, 0.54)
        glRotate(-90, 1, 0, 0)
        glutSolidCylinder(.12, .5, 10, 10)


class CylinderObject_2(GameObject):
    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)

    def draw(self):
        self.applyParentTransform()
        glColor3f(0.36, 0.59, 0.23)
        glRotate(-90, 1, 0, 0)
        glutSolidCylinder(0.5, 0.7, 6, 5)

        self.applyParentTransform()
        glColor3f(0.83, 1, 0.97)
        glTranslate(0, .8, 0)
        glRotate(-90, 1, 0, 0)
        glutSolidCylinder(0.5, 0.04, 6, 5)


class BarrierObject(GameObject):
    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)

    def draw(self):
        glColor3f(0.38, 0.58, 0.76)
        self.applyParentTransform()
        glTranslate(0, 1, 0)
        glScale(0.06, 2, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(0.4, 1, 0)
        glScale(0.06, 2, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(0.8, 1, 0)
        glScale(0.06, 2, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(1.2, 1, 0)
        glScale(0.06, 2, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(-0.4, 1, 0)
        glScale(0.06, 2, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(-0.8, 1, 0)
        glScale(0.06, 2, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(-1.2, 1, 0)
        glScale(0.06, 2, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(0, 0.2, 0)
        glRotate(-90, 0, 0, 1)
        glScale(0.06, 2.5, 0.06)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(0, 1.8, 0)
        glRotate(-90, 0, 0, 1)
        glScale(0.06, 2.5, 0.06)
        glutSolidCube(1)


class TrafficlightsObject(GameObject):
    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)

    def draw(self):
        glColor3f(0.38, 0.58, 0.76)
        self.applyParentTransform()
        glScale(0.2, 0.7, 0.2)
        glutSolidCube(1)

        self.applyParentTransform()
        glTranslate(0, 1.5, 0)
        glScale(0.1, 2.5, 0.1)
        glutSolidCube(1)

        glColor3f(0.68, 0.69, 0.73)
        self.applyParentTransform()
        glTranslate(0.1, 2, 0)
        glScale(0.1, 1, 0.4)
        glutSolidCube(1)

        glColor3f(0.32, 0.49, 0.17)
        self.applyParentTransform()
        glTranslate(0.2, 1.8, 0)
        glScale(0.1, 0.15, 0.15)
        glutSolidCube(1)

        glColor3f(0.77, 0.43, 0.07)
        self.applyParentTransform()
        glTranslate(0.2, 2.1, 0)
        glScale(0.1, 0.15, 0.15)
        glutSolidCube(1)

        glColor3f(0.46, 0.18, 0.19)
        self.applyParentTransform()
        glTranslate(0.2, 2.4, 0)
        glScale(0.1, 0.15, 0.15)
        glutSolidCube(1)


def draw_map_ligting():
    l = []
    for i in range(54):
        l.append(LightingObject(0, 0, 0))
    l[0].rotY = -90
    l[0].posX = -5
    l[0].posZ = -9
    l[0].draw()

    l[1].rotY = -90
    l[1].posX = -27
    l[1].posZ = -9
    l[1].draw()

    l[2].rotY = -90
    l[2].posX = -40
    l[2].posZ = -9
    l[2].draw()

    l[3].rotY = -90
    l[3].posX = -90
    l[3].posZ = -9
    l[3].draw()

    l[4].rotY = -90
    l[4].posX = 5
    l[4].posZ = -9
    l[4].draw()

    l[5].rotY = -90
    l[5].posX = 29
    l[5].posZ = -9
    l[5].draw()

    l[6].rotY = -90
    l[6].posX = 41
    l[6].posZ = -9
    l[6].draw()

    l[7].rotY = -90
    l[7].posX = 90
    l[7].posZ = -9
    l[7].draw()

    l[8].rotY = 90
    l[8].posX = -5
    l[8].posZ = -45
    l[8].draw()

    l[9].rotY = 90
    l[9].posX = -27
    l[9].posZ = -45
    l[9].draw()

    l[10].rotY = 1
    l[10].posX = -40
    l[10].posZ = -45
    l[10].draw()

    l[11].rotY = 90
    l[11].posX = -90
    l[11].posZ = -45
    l[11].draw()

    l[12].rotY = 90
    l[12].posX = 5
    l[12].posZ = -45
    l[12].draw()

    l[13].rotY = 90
    l[13].posX = 29
    l[13].posZ = -45
    l[13].draw()

    l[14].rotY = 90
    l[14].posX = 41
    l[14].posZ = -45
    l[14].draw()

    l[15].rotY = 90
    l[15].posX = 90
    l[15].posZ = -45
    l[15].draw()

    l[16].rotY = 90
    l[16].posX = -5
    l[16].posZ = -91
    l[16].draw()

    l[17].rotY = 90
    l[17].posX = -27
    l[17].posZ = -91
    l[17].draw()

    l[18].rotY = 90
    l[18].posX = -40
    l[18].posZ = -91
    l[18].draw()

    l[19].rotY = 90
    l[19].posX = -90
    l[19].posZ = -91
    l[19].draw()

    l[20].rotY = 90
    l[20].posX = 5
    l[20].posZ = -91
    l[20].draw()

    l[21].rotY = 90
    l[21].posX = 29
    l[21].posZ = -91
    l[21].draw()

    l[22].rotY = 90
    l[22].posX = 41
    l[22].posZ = -91
    l[22].draw()

    l[23].rotY = 90
    l[23].posX = 90
    l[23].posZ = -91
    l[23].draw()

    l[24].rotY = -90
    l[24].posX = -5
    l[24].posZ = -55
    l[24].draw()

    l[25].rotY = -90
    l[25].posX = -27
    l[25].posZ = -55
    l[25].draw()

    l[26].rotY = -90
    l[26].posX = -40
    l[26].posZ = -55
    l[26].draw()

    l[27].rotY = -90
    l[27].posX = -90
    l[27].posZ = -55
    l[27].draw()

    l[28].rotY = -90
    l[28].posX = 5
    l[28].posZ = -55
    l[28].draw()

    l[29].rotY = -90
    l[29].posX = 29
    l[29].posZ = -55
    l[29].draw()

    l[30].rotY = -90
    l[30].posX = 41
    l[30].posZ = -55
    l[30].draw()

    l[31].rotY = -90
    l[31].posX = 90
    l[31].posZ = -55
    l[31].draw()

    l[32].rotY = -180
    l[32].posX = -91.5
    l[32].posZ = -12
    l[32].draw()

    l[33].rotY = -180
    l[33].posX = -91.5
    l[33].posZ = -43
    l[33].draw()

    l[34].rotY = -180
    l[34].posX = -91.5
    l[34].posZ = -57
    l[34].draw()

    l[35].rotY = -180
    l[35].posX = -91.5
    l[35].posZ = -88
    l[35].draw()

    l[36].posX = -38
    l[36].posZ = -12
    l[36].draw()

    l[37].posX = -38
    l[37].posZ = -43
    l[37].draw()

    l[38].posX = -38
    l[38].posZ = -57
    l[38].draw()

    l[39].posX = -38
    l[39].posZ = -88
    l[39].draw()

    l[40].posX = 30.5
    l[40].posZ = -43
    l[40].draw()

    l[41].posX = 30.5
    l[41].posZ = -57
    l[41].draw()

    l[42].posX = 30.5
    l[42].posZ = -88
    l[42].draw()

    l[43].posX = 91.5
    l[43].posZ = -12
    l[43].draw()

    l[44].posX = 91.5
    l[44].posZ = -43
    l[44].draw()

    l[45].posX = 91.5
    l[45].posZ = -57
    l[45].draw()

    l[46].posX = 91.5
    l[46].posZ = -88
    l[46].draw()

    l[47].rotY = -180
    l[47].posX = 39.5
    l[47].posZ = -12
    l[47].draw()

    l[48].rotY = -180
    l[48].posX = 39.5
    l[48].posZ = -43
    l[48].draw()

    l[49].rotY = -180
    l[49].posX = 39.5
    l[49].posZ = -57
    l[49].draw()

    l[50].rotY = -180
    l[50].posX = 39.5
    l[50].posZ = -88
    l[50].draw()

    l[51].rotY = -180
    l[51].posX = -28.5
    l[51].posZ = -43
    l[51].draw()

    l[52].rotY = -180
    l[52].posX = -28.5
    l[52].posZ = -57
    l[52].draw()

    l[53].rotY = -180
    l[53].posX = -28.5
    l[53].posZ = -88
    l[53].draw()

    print("##############################")
    for i in l:
        print("LightingObject(", end='')
        print(i.posX, end='')
        print(",", end='')
        print("0", end='')
        print(",", end='')
        print(i.posZ, end='')
        print(", rotY=", end='')
        print(i.rotY, end='')
        print(")")
    print("##############################")


def draw_traffic_lights():
    t = []
    for i in range(24):
        t.append(TrafficlightsObject(0, 0, 0))
    t[0].posX = 30.5
    t[0].posZ = -9.5
    t[0].draw()

    t[1].posX = 30.5
    t[1].posZ = -45
    t[1].draw()

    t[2].posX = 30.5
    t[2].posZ = -55
    t[2].draw()

    t[3].posX = 30.5
    t[3].posZ = -90
    t[3].draw()

    t[4].posX = -37.5
    t[4].posZ = -9.5
    t[4].draw()

    t[5].posX = -37.5
    t[5].posZ = -45
    t[5].draw()

    t[6].posX = -37.5
    t[6].posZ = -55
    t[6].draw()

    t[7].posX = -37.5
    t[7].posZ = -90
    t[7].draw()

    t[8].posX = 91.5
    t[8].posZ = -9.5
    t[8].draw()

    t[9].posX = 91.5
    t[9].posZ = -45
    t[9].draw()

    t[10].posX = 91.5
    t[10].posZ = -55
    t[10].draw()

    t[11].posX = 91.5
    t[11].posZ = -90
    t[11].draw()

    t[12].rotY = 180
    t[12].posX = 39.5
    t[12].posZ = -9.5
    t[12].draw()

    t[13].rotY = 180
    t[13].posX = 39.5
    t[13].posZ = -45
    t[13].draw()

    t[14].rotY = 180
    t[14].posX = 39.5
    t[14].posZ = -55
    t[14].draw()

    t[15].rotY = 180
    t[15].posX = 39.5
    t[15].posZ = -90
    t[15].draw()

    t[16].rotY = 180
    t[16].posX = -28.5
    t[16].posZ = -9.5
    t[16].draw()

    t[17].rotY = 180
    t[17].posX = -28.5
    t[17].posZ = -45
    t[17].draw()

    t[18].rotY = 180
    t[18].posX = -28.5
    t[18].posZ = -55
    t[18].draw()

    t[19].rotY = 180
    t[19].posX = -28.5
    t[19].posZ = -90
    t[19].draw()

    t[20].rotY = 180
    t[20].posX = -91.5
    t[20].posZ = -9.5
    t[20].draw()

    t[21].rotY = 180
    t[21].posX = -91.5
    t[21].posZ = -45
    t[21].draw()

    t[22].rotY = 180
    t[22].posX = -91.5
    t[22].posZ = -55
    t[22].draw()

    t[23].rotY = 180
    t[23].posX = -91.5
    t[23].posZ = -90
    t[23].draw()

    print("##############################")
    for i in t:
        print("TrafficlightsObject(", end='')
        print(i.posX, end='')
        print(",", end='')
        print("0", end='')
        print(",", end='')
        print(i.posZ, end='')
        print(", rotY=", end='')
        print(i.rotY, end='')
        print(")")
    print("##############################")