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

    def draw(self):
        offsetFromTheGround = 1
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 1)
        glScalef(1, 0.25, 0.5)
        glutSolidCube(5)

        # Upper

        # Upper Body
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 1)
        glTranslate(0, 0.25 * 5, 0)
        glScalef(0.5, 0.25, 0.5)
        glutSolidCube(5)

        # front Glass
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glTranslate(1.3, 0.25 * 5, 0)
        glScalef(0, 0.25, 0.5)
        glutSolidCube(5)

        # left Glass
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glRotate(90, 0, 1, 0)
        glTranslate(1.3, 0.25 * 5, 0)
        glScalef(0, 0.25, 0.5)
        glutSolidCube(5)

        # Right Glass
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(1.3, 0.25 * 5, 0)
        glScalef(0, 0.25, 0.5)
        glutSolidCube(5)

        # back glass
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glRotate(180, 0, 1, 0)
        glTranslate(1.3, 0.25 * 5, 0)
        glScalef(0, 0.25, 0.5)
        glutSolidCube(5)

        # Wheels

        # Right front
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glTranslate(2, -2.5 * 0.2, 2.5 * 0.5)
        glScale(0.3, 0.3, 0.3)
        glutSolidCube(2)
        # inside
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(2, -2.5 * 0.2, 1.6)
        glScale(0.2, 0.2, 0)
        glutSolidCube(2)

        # Left front
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glTranslate(2, -2.5 * 0.2, -2.5 * 0.5)
        glScale(0.3, 0.3, 0.3)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(2, -2.5 * 0.2, -1.6)
        glScale(0.2, 0.2, 0)
        glutSolidCube(2)

        # Right back
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glTranslate(-2, -2.5 * 0.2, 2.5 * 0.5)
        glScale(0.3, 0.3, 0.3)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(-2, -2.5 * 0.2, 1.6)
        glScale(0.2, 0.2, 0)
        glutSolidCube(2)

        # Left back
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glTranslate(-2, -2.5 * 0.2, -2.5 * 0.5)
        glScale(0.3, 0.3, 0.3)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(-2, -2.5 * 0.2, -1.6)
        glScale(0.2, 0.2, 0)
        glutSolidCube(2)

        # Lamps
        # Right
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glTranslate(2.6, 1.5 * 0.25, 1)
        glScale(0, 0.2, 0.2)
        glutSolidCube(3)

        # Left
        self.applyParentTransform()
        glTranslate(0, offsetFromTheGround, 0)
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glTranslate(2.6, 1.5 * 0.25, -0.3)
        glScale(0, 0.2, 0.2)
        glutSolidCube(3)


class Car2(GameObject):
    def onFrameTick(self, dt):
        super().onFrameTick(dt)

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)

    def draw(self):
        # Lower
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 1)
        glScalef(1, 0.25, 0.5)
        glutSolidCube(5)

        # Upper

        # Upper Body
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 1)
        glTranslate(1, 0.25 * 5, 0)
        glScalef(0.3, 0.25, 0.5)
        glutSolidCube(5)

        # front Glass
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glTranslate(1.8, 0.25 * 5, 0)
        glScalef(0, 0.25, 0.5)
        glutSolidCube(5)

        # left Glass
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glRotate(90, 0, 1, 0)
        glTranslate(1.3, 0.25 * 5, 1)
        glScalef(0, 0.25, 0.3)
        glutSolidCube(5)

        # Right Glass
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(1.3, 0.25 * 5, -1)
        glScalef(0, 0.25, 0.3)
        glutSolidCube(5)

        # back glass
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glRotate(180, 0, 1, 0)
        glTranslate(-0.2, 0.25 * 5, 0)
        glScalef(0, 0.25, 0.5)
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
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glTranslate(2.6, 1.5 * 0.25, 1)
        glScale(0, 0.2, 0.2)
        glutSolidCube(3)

        # Left
        self.applyParentTransform()
        glRotate(0, 0, 0, 0)
        glColor3f(0, 0, 0)
        glTranslate(2.6, 1.5 * 0.25, -0.3)
        glScale(0, 0.2, 0.2)
        glutSolidCube(3)


class Car_bus(GameObject):
    def onFrameTick(self, dt):
        super().onFrameTick(dt)

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)

    def draw(self):
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 1)
        glScalef(2.5, 1, 1)
        glutSolidCube(5)

        # Glass
        # front
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(6.3, 1.5, 0)
        glScalef(0, 0.4, 1)
        glutSolidCube(5)

        # back
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(-6.3, 1.5, 0)
        glScalef(0, 0.4, 1)
        glutSolidCube(5)

        # right
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(2.6, 1.7, 4)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(2.6, 1.7, 1.5)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(2.6, 1.7, -1)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(2.6, 1.7, -3.5)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(2.6, 1.7, -5.4)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)

        # left
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(-2.6, 1.7, 4)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(-2.6, 1.7, 1.5)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(-2.6, 1.7, -1)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(-2.6, 1.7, -3.5)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glRotate(-90, 0, 1, 0)
        glTranslate(-2.6, 1.7, -5.4)
        glScalef(0, 0.3, 0.3)
        glutSolidCube(5)

        # Wheels

        # Right front
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(4, -2, 2.5)
        glScale(0.6, 0.6, 0.6)
        glutSolidCube(2)
        # inside
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(4, -2, 3.2)
        glScale(0.4, 0.4, 0)
        glutSolidCube(2)

        # Left front
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(4, -2, -2.5)
        glScale(0.6, 0.6, 0.6)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(4, -2, -3.2)
        glScale(0.4, 0.4, 0)
        glutSolidCube(2)

        # Right back
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(-4, -2, 2.5)
        glScale(0.6, 0.6, 0.6)
        glutSolidCube(2)
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(-2, -2, 2.5)
        glScale(0.6, 0.6, 0.6)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(-4, -2, 3.2)
        glScale(0.4, 0.4, 0)
        glutSolidCube(2)
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(-2, -2, 3.2)
        glScale(0.4, 0.4, 0)
        glutSolidCube(2)

        # Left back
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(-4, -2, -2.5)
        glScale(0.6, 0.6, 0.6)
        glutSolidCube(2)
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(-2, -2, -2.5)
        glScale(0.6, 0.6, 0.6)
        glutSolidCube(2)

        # inside
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(-4, -2, -3.2)
        glScale(0.4, 0.4, 0)
        glutSolidCube(2)
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0.6, 0.6, 0.6)
        glTranslate(-2, -2, -3.2)
        glScale(0.4, 0.4, 0)
        glutSolidCube(2)

        # Lamps
        # Right
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(2.6, 1.5 * 0.25, 1)
        glScale(0, 0.2, 0.2)
        glutSolidCube(3)

        # Left
        self.applyParentTransform()
        glRotate(180, 0, 1, 0)
        glColor3f(0, 0, 0)
        glTranslate(2.6, 1.5 * 0.25, -0.3)
        glScale(0, 0.2, 0.2)
        glutSolidCube(3)


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
