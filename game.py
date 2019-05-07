from time import time

from CollisionDetection import isCollided
from OpenGL.GLU import *
from OpenGL.GLUT import *

from MainMap import drawMap
from gamestatus import *
from gametextures import drawImage2D, drawText2D
from initopengl import initOpenGl
from intractable_objects import createMapObjects
from objects.PlayerObject import *

player = PlayerObject()

deltaTime = 0
currentTime = 0
currentGameStatus = 0

cameraZoom = 0
currentGameScore = 0
intractableObjects = []
needToBeRemoved = []


def initCamera():
    global player, cameraZoom
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.001, 100000)
    gluLookAt(player.posX + 0, 10 + cameraZoom, player.posZ + 10 + cameraZoom,
              player.posX + 0, 0, player.posZ + 0,
              0, 1, 0)
    glMatrixMode(GL_MODELVIEW)


referenceGameScore = 0
toMakeBigger = 10


def Score_update(currGameScore):
    global referenceGameScore, toMakeBigger
    global currentGameScore
    if currGameScore - referenceGameScore >= toMakeBigger:
        player.radius += 1
        player.update_area()
        referenceGameScore = currGameScore
        drawText2D("Size Up!", player.posX, 2, player.posZ, scaleFactor=0.6)
        toMakeBigger *= 3
        return True
    return False


currentlyEating = []


def eatObject(i):
    global player
    global currentlyEating
    if not currentlyEating.__contains__(i):
        i.animationList = []
        i.startAnimation(Animation(AnimationParams.posX, None, player.posX, 0.4, priority=AnimationPriority.High))
        i.startAnimation(
            Animation(AnimationParams.posZ, None, player.posZ, 0.4, priority=AnimationPriority.High))
        global intractableObjects
        global needToBeRemoved
        i.startAnimation(DeltaAnimation(AnimationParams.posY, -5, 0.4, priority=AnimationPriority.High,
                                        onAnimationFinished=lambda: needToBeRemoved.append(i)))
        currentlyEating.append(i)


def draw():
    # Delta Time
    global cameraZoom
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

    glClearColor(0, 0.49, 0.76, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0, 0, 1)
    glLoadIdentity()

    if currentGameStatus >= GAME_STATUS_SCORE:
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-5, 5, -5, 5)
        glMatrixMode(GL_MODELVIEW)
        drawImage2D("resources/images/score_title.png", 0, 2.5)
        drawText2D(str(round(currentGameScore)), 0, -1, scaleFactor=1)

    if GAME_STATUS_PLAYING < currentGameStatus < GAME_STATUS_SCORE:
        global intractableObjects
        initCamera()
        glLoadIdentity()

        # glDisable(GL_BLEND)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_CULL_FACE)
        drawMap()
        glLoadIdentity()
        glEnable(GL_BLEND)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        player.onFrameTick(deltaTime)

        player.draw()
        draw_others()

        # collision
        for i in intractableObjects:
            if isCollided(player, i):
                if player.area > i.area:
                    eatObject(i)
                else:
                    # decrease opacity
                    i.alpha = 0.4
            else:
                # revert opacity
                i.alpha = 1

        global needToBeRemoved
        for tbr in needToBeRemoved:
            intractableObjects.remove(tbr)
            currentGameScore += tbr.area // AREA_TO_SCORE_RATIO

        needToBeRemoved.clear()

        # draw + frameTick
        for o in intractableObjects:
            o.onFrameTick(deltaTime)
            o.draw()
        if Score_update(currentGameScore):
            cameraZoom += 5

    if GAME_STATUS_COUNTDOWN <= currentGameStatus < GAME_STATUS_PLAYING:
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-5, 5, -5, 5)
        glMatrixMode(GL_MODELVIEW)
        if currentGameStatus > 3:
            drawImage2D("resources/images/countdown_1.png", 0, 0,
                        scaleFactor=0.5 + (currentGameStatus - GAME_STATUS_COUNTDOWN - 2))
        elif currentGameStatus > 2:
            drawImage2D("resources/images/countdown_2.png", 0, 0,
                        scaleFactor=0.5 + (currentGameStatus - GAME_STATUS_COUNTDOWN - 1))
        else:
            drawImage2D("resources/images/countdown_3.png", 0, 0,
                        scaleFactor=0.5 + (currentGameStatus - GAME_STATUS_COUNTDOWN))
    if currentGameStatus == GAME_STATUS_MAINMENU:
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
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
        quit()
    global cameraZoom
    if key == b'[':
        cameraZoom += 1
    if key == b']':
        cameraZoom -= 1


def onSpecialKeyDown(key, x, y):
    global player
    global angle

    speed = min(max(15 / player.radius, PLAYER_MINIMUM_SPEED), PLAYER_MAXIMUM_SPEED) * PLAYER_SPEED_FACTOR

    if key == GLUT_KEY_RIGHT:
        if player.posX < 100 - player.radius:
            # player.startAnimation(DeltaAnimation(AnimationParams.posX,+PLAYER_MINIMUM_MOVEMENT ,.001))
            player.posX += speed * deltaTime
        player.rotY = 90
        player.x = player.radius + .2
        player.z = 0


    elif key == GLUT_KEY_LEFT:
        if player.posX > -100 + player.radius:
            # player.startAnimation(DeltaAnimation(AnimationParams.posX,-PLAYER_MINIMUM_MOVEMENT ,.001))
            player.posX -= speed * deltaTime
        player.rotY = -90
        player.x = -player.radius - .2
        player.z = 0

    elif key == GLUT_KEY_DOWN:
        if player.posZ < -player.radius:
            # player.startAnimation(DeltaAnimation(AnimationParams.posZ, +PLAYER_MINIMUM_MOVEMENT , .001))
            player.posZ += speed * deltaTime
        player.rotY = 0
        player.z = player.radius + .2
        player.x = 0
    elif key == GLUT_KEY_UP:

        if player.posZ > -100 + player.radius:
            # player.startAnimation(DeltaAnimation(AnimationParams.posZ, -PLAYER_MINIMUM_MOVEMENT, .001))
            player.posZ -= speed * deltaTime
        player.rotY = 180
        player.z = - player.radius - .2
        player.x = 0


def onMouseKeyDown(button, state, x, y):
    global currentGameStatus
    if button == GLUT_LEFT_BUTTON and currentGameStatus == GAME_STATUS_MAINMENU:
        currentGameStatus = GAME_STATUS_COUNTDOWN
        global intractableObjects
        global currentGameScore
        currentGameScore = 0
        intractableObjects = createMapObjects()


initOpenGl(draw, onMouseKeyDown, onKeyboardKeyDown, onSpecialKeyDown)
