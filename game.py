from time import time

from objects.CarObject import *
from objects.CharacterObject import *
from objects.HomeObject import *
from objects.PlayerObject import PlayerObject
from objects.StreetObject import draw_map_ligting, draw_traffic_lights, TrafficlightsObject, LightingObject
from gameobject import *

from gametextures import drawImage2D, drawText2D
from initopengl import initOpenGl
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from gamestatus import *
from MainMap import drawMap

deltaTime = 0
currentTime = 0

currentGameStatus = 0
currentGameScore = 1997

p = CharacterObject(0, 0, -2)
c1 = Car1(0, 0, 0)

h1 = HomeObject_3(0, 0, 0, rotY=90)

intractableObjects = [
    p, c1,
    # lighting
    LightingObject(-5, 0, -9, rotY=-90),
    LightingObject(-27, 0, -9, rotY=-90),
    LightingObject(-40, 0, -9, rotY=-90),
    LightingObject(-90, 0, -9, rotY=-90),
    LightingObject(5, 0, -9, rotY=-90),
    LightingObject(29, 0, -9, rotY=-90),
    LightingObject(41, 0, -9, rotY=-90),
    LightingObject(90, 0, -9, rotY=-90),
    LightingObject(-5, 0, -45, rotY=90),
    LightingObject(-27, 0, -45, rotY=90),
    LightingObject(-40, 0, -45, rotY=1),
    LightingObject(-90, 0, -45, rotY=90),
    LightingObject(5, 0, -45, rotY=90),
    LightingObject(29, 0, -45, rotY=90),
    LightingObject(41, 0, -45, rotY=90),
    LightingObject(90, 0, -45, rotY=90),
    LightingObject(-5, 0, -91, rotY=90),
    LightingObject(-27, 0, -91, rotY=90),
    LightingObject(-40, 0, -91, rotY=90),
    LightingObject(-90, 0, -91, rotY=90),
    LightingObject(5, 0, -91, rotY=90),
    LightingObject(29, 0, -91, rotY=90),
    LightingObject(41, 0, -91, rotY=90),
    LightingObject(90, 0, -91, rotY=90),
    LightingObject(-5, 0, -55, rotY=-90),
    LightingObject(-27, 0, -55, rotY=-90),
    LightingObject(-40, 0, -55, rotY=-90),
    LightingObject(-90, 0, -55, rotY=-90),
    LightingObject(5, 0, -55, rotY=-90),
    LightingObject(29, 0, -55, rotY=-90),
    LightingObject(41, 0, -55, rotY=-90),
    LightingObject(90, 0, -55, rotY=-90),
    LightingObject(-91.5, 0, -12, rotY=-180),
    LightingObject(-91.5, 0, -43, rotY=-180),
    LightingObject(-91.5, 0, -57, rotY=-180),
    LightingObject(-91.5, 0, -88, rotY=-180),
    LightingObject(-38, 0, -12, rotY=0),
    LightingObject(-38, 0, -43, rotY=0),
    LightingObject(-38, 0, -57, rotY=0),
    LightingObject(-38, 0, -88, rotY=0),
    LightingObject(30.5, 0, -43, rotY=0),
    LightingObject(30.5, 0, -57, rotY=0),
    LightingObject(30.5, 0, -88, rotY=0),
    LightingObject(91.5, 0, -12, rotY=0),
    LightingObject(91.5, 0, -43, rotY=0),
    LightingObject(91.5, 0, -57, rotY=0),
    LightingObject(91.5, 0, -88, rotY=0),
    LightingObject(39.5, 0, -12, rotY=-180),
    LightingObject(39.5, 0, -43, rotY=-180),
    LightingObject(39.5, 0, -57, rotY=-180),
    LightingObject(39.5, 0, -88, rotY=-180),
    LightingObject(-28.5, 0, -43, rotY=-180),
    LightingObject(-28.5, 0, -57, rotY=-180),
    LightingObject(-28.5, 0, -88, rotY=-180),
    # traficlights
    TrafficlightsObject(30.5, 0, -9.5, rotY=0),
    TrafficlightsObject(30.5, 0, -45, rotY=0),
    TrafficlightsObject(30.5, 0, -55, rotY=0),
    TrafficlightsObject(30.5, 0, -90, rotY=0),
    TrafficlightsObject(-37.5, 0, -9.5, rotY=0),
    TrafficlightsObject(-37.5, 0, -45, rotY=0),
    TrafficlightsObject(-37.5, 0, -55, rotY=0),
    TrafficlightsObject(-37.5, 0, -90, rotY=0),
    TrafficlightsObject(91.5, 0, -9.5, rotY=0),
    TrafficlightsObject(91.5, 0, -45, rotY=0),
    TrafficlightsObject(91.5, 0, -55, rotY=0),
    TrafficlightsObject(91.5, 0, -90, rotY=0),
    TrafficlightsObject(39.5, 0, -9.5, rotY=180),
    TrafficlightsObject(39.5, 0, -45, rotY=180),
    TrafficlightsObject(39.5, 0, -55, rotY=180),
    TrafficlightsObject(39.5, 0, -90, rotY=180),
    TrafficlightsObject(-28.5, 0, -9.5, rotY=180),
    TrafficlightsObject(-28.5, 0, -45, rotY=180),
    TrafficlightsObject(-28.5, 0, -55, rotY=180),
    TrafficlightsObject(-28.5, 0, -90, rotY=180),
    TrafficlightsObject(-91.5, 0, -9.5, rotY=180),
    TrafficlightsObject(-91.5, 0, -45, rotY=180),
    TrafficlightsObject(-91.5, 0, -55, rotY=180),
    TrafficlightsObject(-91.5, 0, -90, rotY=180)
]

player = PlayerObject(0, 0, 0)

cameraZoom = 0
startCycle(c1)


def initCamera():
    global player, cameraZoom
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70, 1, 0.001, 100000)
    gluLookAt(player.posX + 0, 10 + cameraZoom, player.posZ + 10 + cameraZoom,
              player.posX + 0, 0, player.posZ + 0,
              0, 1, 0)
    glMatrixMode(GL_MODELVIEW)


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
        global intractableObjects
        initCamera()
        glLoadIdentity()

        glDisable(GL_BLEND)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_CULL_FACE)
        drawMap()
        glLoadIdentity()

        glEnable(GL_BLEND)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        for o in intractableObjects:
            o.onFrameTick(deltaTime)
            o.draw()
        # p.onFrameTick(deltaTime)
        # p.draw()
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

    if not currentGameStatus == GAME_STATUS_MAINMENU:
        currentGameStatus += deltaTime

    glutSwapBuffers()


def onKeyboardKeyDown(key, x, y):
    global currentGameStatus
    if key == b'r':
        print('Restarting the game..')
        currentGameStatus = GAME_STATUS_MAINMENU

    if key == b'p':
        print('Player position : ', end='')
        print(player.posX, end='')
        print(player.posZ)

    global cameraZoom
    if key == b'[':
        cameraZoom += 5
    if key == b']':
        cameraZoom -= 5


def onSpecialKeyDown(key, x, y):
    if key == GLUT_KEY_UP:
        player.startAnimation(DeltaAnimation(AnimationParams.posZ, -PLAYER_MINIMUM_MOVEMENT, 0.2))
    if key == GLUT_KEY_DOWN:
        player.startAnimation(DeltaAnimation(AnimationParams.posZ, +PLAYER_MINIMUM_MOVEMENT, 0.2))
    if key == GLUT_KEY_RIGHT:
        player.startAnimation(DeltaAnimation(AnimationParams.posX, +PLAYER_MINIMUM_MOVEMENT, 0.2))
    if key == GLUT_KEY_LEFT:
        player.startAnimation(DeltaAnimation(AnimationParams.posX, -PLAYER_MINIMUM_MOVEMENT, 0.2))


def onMouseKeyDown(button, state, x, y):
    global currentGameStatus

    if button == GLUT_LEFT_BUTTON and currentGameStatus == GAME_STATUS_MAINMENU:
        currentGameStatus = GAME_STATUS_COUNTDOWN


initOpenGl(draw, onMouseKeyDown, onKeyboardKeyDown, onSpecialKeyDown)
