from time import time

from CharacterObject import CharacterObject
from gameobject import *

from gametextures import drawImage2D, drawText2D
from initopengl import initOpenGl, initCamera
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from gamestatus import *
from MainMap import drawMap
deltaTime = 0
currentTime = 0

currentGameStatus = 0
currentGameScore = 1997

p = CharacterObject(0, 0, 0,
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
    glClear(GL_COLOR_BUFFER_BIT)
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
        # player.onFrameTick(deltaTime)
        # player.draw()
        drawMap()
        glLoadIdentity()
        p.onFrameTick(deltaTime)
        p.draw()

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
        a1 = DeltaAnimation(AnimationParams.posX, 3, 1, onAnimationFinished=lambda:  p.startAnimation(a2), priority=AnimationPriority.High)
        a2 = DeltaAnimation(AnimationParams.posX, -3, 1, onAnimationFinished=lambda: p.startAnimation(a1), priority=AnimationPriority.High)
        p.startAnimation(a1)
    if key == GLUT_KEY_DOWN:
        p.startAnimation(DeltaAnimation(AnimationParams.rotY, 90, 1, priority=AnimationPriority.High))


def onMouseKeyDown(button, state, x, y):
    global currentGameStatus

    if button == GLUT_LEFT_BUTTON and currentGameStatus == GAME_STATUS_MAINMENU:
        currentGameStatus = GAME_STATUS_COUNTDOWN


initOpenGl(draw, onMouseKeyDown, onKeyboardKeyDown, onSpecialKeyDown)
