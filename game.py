from time import time

from gameobject import *

from gametextures import drawImage2D, drawText2D
from initopengl import initOpenGl, initCamera
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from gamestatus import *

deltaTime = 0
currentTime = 0

currentGameStatus = 0
currentGameScore = 1997


class SimpleObj(GameObject):

    def __init__(self, posX, posY, posZ, scaleX, scaleY, scaleZ, rotY):
        super().__init__(posX, posY, posZ, scaleX, scaleY, scaleZ, rotY)

    def draw(self):
        self.applyParentTransform()
        glColor3f(0, 0, 1)
        glScale(1, 0.01, 1)
        glutSolidCube(2)

        self.applyParentTransform()
        glColor3f(1, 0, 0)
        glutWireCube(2)


player = SimpleObj(0, 0, 0,
                   1, 1, 1,
                   0)


def draw():
    # Delta Time
    global currentTime
    global deltaTime
    newTime = time()
    frameTime = newTime - currentTime
    currentTime = newTime
    deltaTime = frameTime

    # Speed Factor
    deltaTime *= GAME_SPEED_FACTOR

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
        drawText2D("CLICK TO PLAY !", 0, 0, scaleFactor=0.5)
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
        player.startAnimation(Animation(AnimationParams.posY, None, 3, 3, onAnimationFinished=lambda: print("callback!!")))
    if key == GLUT_KEY_DOWN:
        player.startAnimation(DeltaAnimation(AnimationParams.posX, 5, 3, priority=AnimationPriority.High))
        player.startAnimation(
            Animation(AnimationParams.posY, None, 0, 3, priority=AnimationPriority.High, onAnimationFinished=lambda: print("callback!!")))


def onMouseKeyDown(button, state, x, y):
    global currentGameStatus

    if button == GLUT_LEFT_BUTTON and currentGameStatus == GAME_STATUS_MAINMENU:
        currentGameStatus = GAME_STATUS_COUNTDOWN


initOpenGl(draw, onMouseKeyDown, onKeyboardKeyDown, onSpecialKeyDown)
