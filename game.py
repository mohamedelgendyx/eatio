from abc import ABC, abstractmethod
from time import time

from gametextures import drawImage2D, drawText2D
from initopengl import initOpenGl, initCamera
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from gamestatus import *

currentGameStatus = 0
currentGameScore = 1997

ANIMATION_PRIORITY_NORMAL = 0
ANIMATION_PRIORITY_IGNORE_OTHERS = 1997


class Animation:

    def __init__(self, valueName, fromValue, toValue, animationTime, priority=ANIMATION_PRIORITY_NORMAL):
        self.valueName = valueName
        self.fromValue = fromValue
        self.toValue = toValue
        self.animationTime = animationTime
        self.priority = priority
        self.currentProgress = 0


class DeltaAnimation:

    def __init__(self, valueName, deltaValue, animationTime, priority=ANIMATION_PRIORITY_NORMAL):
        self.valueName = valueName
        self.deltaValue = deltaValue
        self.animationTime = animationTime
        self.priority = priority
        self.currentProgress = 0
        self.fromValue = None


class GameObject(ABC):

    def __init__(self, posX, posY, posZ, scaleX, scaleY, scaleZ, rotAngle, rotX, rotY, rotZ):
        self.posX = posX
        self.posY = posY
        self.posZ = posZ

        self.scaleX = scaleX
        self.scaleY = scaleY
        self.scaleZ = scaleZ

        self.rotAngle = rotAngle
        self.rotX = rotX
        self.rotY = rotY
        self.rotZ = rotZ

        self.animationList = []
        super().__init__()

    def applyParentTransform(self):
        glLoadIdentity()
        glTranslate(self.posX, self.posY, self.posZ)
        glScale(self.scaleX, self.scaleY, self.scaleZ)
        glRotate(self.rotAngle, self.rotX, self.rotY, self.rotZ)

    @abstractmethod
    def draw(self):
        pass

    @staticmethod
    def _calculateNextValue(currentValue, animation):

        if isinstance(animation, Animation):
            if animation.fromValue is None:
                animation.fromValue = currentValue
                if animation.fromValue == animation.toValue:
                    animation.currentProgress = 1
            if animation.currentProgress >= 1:
                return animation.toValue
            return animation.fromValue + ((animation.toValue - animation.fromValue) * animation.currentProgress)
        elif isinstance(animation, DeltaAnimation):
            if animation.fromValue is None:
                animation.fromValue = currentValue
            if animation.currentProgress >= 1:
                return animation.fromValue + animation.deltaValue
            return animation.fromValue + (animation.deltaValue * animation.currentProgress)

    def onFrameTick(self, dt):
        highPriority = []
        for anim in self.animationList:
            if anim.priority == ANIMATION_PRIORITY_IGNORE_OTHERS:
                highPriority.append(anim)

        if len(highPriority) > 0:
            self.animationList.clear()
            for anim in highPriority:
                self.animationList.append(anim)

        toBeRemoved = []
        for anim in self.animationList:

            if anim.currentProgress >= 1:
                toBeRemoved.append(anim)

            if anim.valueName == "posX":
                self.posX = self._calculateNextValue(self.posX, anim)
            elif anim.valueName == "posY":
                self.posY = self._calculateNextValue(self.posY, anim)
            elif anim.valueName == "posZ":
                self.posZ = self._calculateNextValue(self.posZ, anim)
            elif anim.valueName == "scaleX":
                self.scaleX = self._calculateNextValue(self.scaleX, anim)
            elif anim.valueName == "scaleY":
                self.scaleY = self._calculateNextValue(self.scaleY, anim)
            elif anim.valueName == "scaleZ":
                self.scaleZ = self._calculateNextValue(self.scaleZ, anim)

            anim.currentProgress += (dt / anim.animationTime)

        for tbr in toBeRemoved:
            self.animationList.remove(tbr)
            print("removed aniamtion !!")

    def startAnimation(self, animation):
        self.animationList.append(animation)


class SimpleObj(GameObject):

    def __init__(self, posX, posY, posZ, scaleX, scaleY, scaleZ, rotAngle, rotX, rotY, rotZ):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotAngle, rotX, rotY, rotZ)

    def draw(self):
        self.applyParentTransform()
        glColor3f(0, 0, 1)
        glScale(1, 0.01, 1)
        glutSolidCube(2)

        self.applyParentTransform()
        glColor3f(1, 0, 0)
        glutWireCube(2)


deltaTime = 0
currentTime = 0

player = SimpleObj(1, 0, 0,
                   1, 1, 1,
                   0, 0, 0, 0)


def draw():
    global currentTime
    global deltaTime
    newTime = time()
    frameTime = newTime - currentTime
    currentTime = newTime
    deltaTime = frameTime

    global currentGameStatus
    global currentGameScore

    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0, 0, 1)
    glLoadIdentity()

    if currentGameStatus >= GAME_STATUS_SCORE:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-5, 5, -5, 5)
        glMatrixMode(GL_MODELVIEW)
        drawImage2D("resources/images/score_title.png", 0, 2.5)
        drawText2D(str(currentGameScore), 0, -1, scaleFactor=1)

    if GAME_STATUS_PLAYING < currentGameStatus < GAME_STATUS_SCORE:
        initCamera()
        glLoadIdentity()
        player.onFrameTick(deltaTime)
        player.draw()

    if GAME_STATUS_COUNTDOWN <= currentGameStatus < GAME_STATUS_PLAYING:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-5, 5, -5, 5)
        glMatrixMode(GL_MODELVIEW)
        if currentGameStatus > 3:
            drawImage2D("resources/images/countdown_1.png", 0, 0, scaleFactor=0.5 + (currentGameStatus - GAME_STATUS_COUNTDOWN - 2))
        elif currentGameStatus > 2:
            drawImage2D("resources/images/countdown_2.png", 0, 0, scaleFactor=0.5 + (currentGameStatus - GAME_STATUS_COUNTDOWN - 1))
        else:
            drawImage2D("resources/images/countdown_3.png", 0, 0, scaleFactor=0.5 + (currentGameStatus - GAME_STATUS_COUNTDOWN))

    if currentGameStatus == GAME_STATUS_MAINMENU:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-5, 5, -5, 5)
        glMatrixMode(GL_MODELVIEW)
        drawText2D("CLICK TO PLAY!", 0, 0, scaleFactor=0.5)
        # drawImage2D("resources/images/clicktoplay.png", 0, 0)

    if not currentGameStatus == GAME_STATUS_MAINMENU:
        currentGameStatus += deltaTime

    glFlush()


def onKeyboardKeyDown(key, x, y):
    global currentGameStatus
    if key == b'r':
        print('Restarting the game..')
    currentGameStatus = GAME_STATUS_MAINMENU


def onSpecialKeyDown(key, x, y):
    if key == GLUT_KEY_UP:
        player.startAnimation(DeltaAnimation("posX", 10, 3))

    if key == GLUT_KEY_DOWN:
        player.startAnimation(Animation("posX", None, 5, 3, ANIMATION_PRIORITY_IGNORE_OTHERS))


def onMouseKeyDown(button, state, x, y):
    global currentGameStatus

    if button == GLUT_LEFT_BUTTON and currentGameStatus == GAME_STATUS_MAINMENU:
        currentGameStatus = GAME_STATUS_COUNTDOWN


initOpenGl(draw, onMouseKeyDown, onKeyboardKeyDown, onSpecialKeyDown)
