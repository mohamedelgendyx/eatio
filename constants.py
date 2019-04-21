from enum import Enum


class AnimationParams(Enum):
    posX = "posX"
    posY = "posY"
    posZ = "posZ"

    scaleX = "scaleX"
    scaleY = "scaleY"
    scaleZ = "scaleZ"

    rotY = "rotY"


class AnimationPriority(Enum):
    Normal = 0
    High = 1
