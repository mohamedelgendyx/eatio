from math import *

def testCube (playerRadius,playerCX,playerCZ,objectLength,objectWidth,objectCX,objectCZ):

    #ObjectDimensions
    objectLength = objectLength/2
    objectWidth = objectWidth/2
    rigthX = objectCX + objectWidth
    leftX = objectCX - objectWidth
    topZ = objectCZ + objectLength
    bottomZ = objectCZ - objectLength

    if playerCX <= leftX:
         collisionX= leftX
    else:
        if playerCX >= rigthX:
            collisionX = rigthX
        else:
            collisionX = playerCX

    if playerCZ <= bottomZ:
        collisionZ = bottomZ
    else:
        if playerCZ >= topZ:
            collisionZ = topZ
        else:
            collisionZ = playerCZ

    distanceX = playerCX - collisionX
    distanceZ = playerCZ - collisionZ
    distance = sqrt(distanceX ** 2 + distanceZ ** 2)

    if distance <= playerRadius:
        return True
    else:
        return False
