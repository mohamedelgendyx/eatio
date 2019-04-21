from time import time
from winsound import PlaySound, SND_ASYNC, SND_LOOP, SND_FILENAME

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def initCamera():
    #glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 50)
    gluLookAt(10, 10, 10,
              0, 0, 0,
              0, 1, 0)
    glMatrixMode(GL_MODELVIEW)


def displayFunction():
    global draw
    draw()


def initOpenGl(drawParameter, onMouseKey, onKeyboardKey, onSpecialKey):
    global currentTime
    global draw

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"EAT.io")

    PlaySound("resources/sounds/bg_music.wav", SND_FILENAME | SND_LOOP | SND_ASYNC)

    initCamera()
    currentTime = time()
    draw = drawParameter

    glutDisplayFunc(displayFunction)
    glutIdleFunc(displayFunction)

    glutMouseFunc(onMouseKey)
    glutKeyboardFunc(onKeyboardKey)
    glutSpecialFunc(onSpecialKey)

    glutMainLoop()
