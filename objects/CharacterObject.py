from OpenGL.GLUT import *
from gameobject import *


class CharacterObject(GameObject):

    def __init__(self, posX, posY, posZ, scaleX=1, scaleY=1, scaleZ=1, rotY=0, r=0, g=0, b=0):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)
        self.Length=0
        self.width=0
        self.HeadDeltaY = 0
        self.HeadUpDown = 1
        self.r=r/255
        self.g=g/255
        self.b=b/255

    def draw(self):
        self.applyParentTransform()
        glColor3f(self.r, self.g, self.b)
        glTranslate(0, 1.5, 0)
        glScale(.6, .9, .4)
        glutSolidCube(.976)

        self.applyParentTransform()
        glColor3f(241 / 255, 195 / 255, 125 / 255)
        glTranslate(0, 2.0 + self.HeadDeltaY, 0)
        glScale(.6, .3, .4)
        glutSolidCube(1.03)

        self.applyParentTransform()
        glColor3f(0, 0, 0.1)
        glTranslate(0, 2.25 + self.HeadDeltaY, 0)
        glScale(.6, .2, .4)
        glutSolidCube(1.03)

    def onFrameTick(self, dt):
        super().onFrameTick(dt)
        if self.HeadDeltaY > 0.1:
            self.HeadUpDown = 0
        if self.HeadDeltaY < -0.1:
            self.HeadUpDown = 1
        if self.HeadUpDown:
            self.HeadDeltaY += dt * 0.3
        else:
            self.HeadDeltaY -= dt * 0.3
