import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *

cachedTextures = {}
cachedTexturesData = {}
cachedTexturesHandles = {}


def drawImage2D(filename, x, y, tintColorR=1, tintColorG=1, tintColorB=1, scaleFactor=1):
    glLoadIdentity()
    global cachedTextures
    if filename in cachedTextures:
        textureSurface = cachedTextures[filename]
        textureData = cachedTexturesData[filename]
        texid = cachedTexturesHandles[filename]
    else:
        print("loading texture ..")
        textureSurface = pygame.image.load(filename)
        cachedTextures[filename] = textureSurface
        textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
        cachedTexturesData[filename] = textureData
        texid = glGenTextures(1)
        cachedTexturesHandles[filename] = texid

    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    glTranslate(x, y, 0)
    widthToHeight = width / height
    glColor3f(tintColorR, tintColorG, tintColorB)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0 * widthToHeight * scaleFactor, -1.0 * scaleFactor, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0 * widthToHeight * scaleFactor, -1.0 * scaleFactor, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0 * widthToHeight * scaleFactor, 1.0 * scaleFactor, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0 * widthToHeight * scaleFactor, 1.0 * scaleFactor, 1.0)
    glEnd()

    glDisable(GL_TEXTURE_2D)


font = None


def drawText2D(text, x, y, z=0, tintColorR=1, tintColorG=1, tintColorB=1, scaleFactor=1):
    glLoadIdentity()
    global font
    if font is None:
        pygame.font.init()
        font = pygame.font.Font(None, 100)
    global cachedTextures
    if text in cachedTextures:
        textureSurface = cachedTextures[text]
        textureData = cachedTexturesData[text]
        texid = cachedTexturesHandles[text]
    else:
        print("loading texture ..")
        textureSurface = font.render(text, True, (tintColorR * 255, tintColorG * 255, tintColorB * 255, 255),
                                     (0, 0, 0, 255))
        cachedTextures[text] = textureSurface
        textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
        cachedTexturesData[text] = textureData
        texid = glGenTextures(1)
        cachedTexturesHandles[text] = texid

    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    glTranslate(x, y, z)
    glScale(scaleFactor, scaleFactor, 1)
    widthToHeight = (width / height)
    glColor3f(tintColorR, tintColorG, tintColorB)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0 * widthToHeight * scaleFactor, -1.0 * scaleFactor, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0 * widthToHeight * scaleFactor, -1.0 * scaleFactor, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0 * widthToHeight * scaleFactor, 1.0 * scaleFactor, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0 * widthToHeight * scaleFactor, 1.0 * scaleFactor, 1.0)
    glEnd()

    glDisable(GL_TEXTURE_2D)
