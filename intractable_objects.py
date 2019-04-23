from objects.CarObject import Car1, startCycle_1, startCycle_2
from objects.CharacterObject import CharacterObject
from objects.HomeObject import HomeObject_3, HomeObject_2, HomeObject_1
from objects.StreetObject import LightingObject, TrafficlightsObject, CylinderObject_1, CylinderObject_2, ConeObject, BarrierObject

p = CharacterObject(0, 0, -2)
c1 = Car1(0, 0, 0)
c2 = Car1(0, 0, 0)
c3 = Car1(0, 0, 0)
c4 = Car1(0, 0, 0)
h1 = HomeObject_3(0, 0, 0, rotY=90)


def createMapObjects():
    objs = [
        p, c1, c2, c3, c4,
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
        TrafficlightsObject(-91.5, 0, -90, rotY=180),
        # cylinders_1
        CylinderObject_1(-89, 0, -9),
        CylinderObject_1(-88.5, 0, -9),
        CylinderObject_1(-88, 0, -9),
        CylinderObject_1(-87.5, 0, -9),
        CylinderObject_1(-26, 0, -9),
        CylinderObject_1(-25.5, 0, -9),
        CylinderObject_1(-25, 0, -9),
        CylinderObject_1(-24.5, 0, -9),
        CylinderObject_1(27, 0, -9),
        CylinderObject_1(26.5, 0, -9),
        CylinderObject_1(26, 0, -9),
        CylinderObject_1(25.5, 0, -9),
        CylinderObject_1(89, 0, -9),
        CylinderObject_1(88.5, 0, -9),
        CylinderObject_1(88, 0, -9),
        CylinderObject_1(87.5, 0, -9),
        CylinderObject_1(-89, 0, -45),
        CylinderObject_1(-88.5, 0, -45),
        CylinderObject_1(-88, 0, -45),
        CylinderObject_1(-87.5, 0, -45),
        CylinderObject_1(-26, 0, -45),
        CylinderObject_1(-25.5, 0, -45),
        CylinderObject_1(-25, 0, -45),
        CylinderObject_1(-24.5, 0, -45),
        CylinderObject_1(27, 0, -45),
        CylinderObject_1(26.5, 0, -45),
        CylinderObject_1(26, 0, -45),
        CylinderObject_1(25.5, 0, -45),
        CylinderObject_1(89, 0, -45),
        CylinderObject_1(88, 0, -45),
        CylinderObject_1(87.5, 0, -45),
        CylinderObject_1(-89, 0, -55),
        CylinderObject_1(-88.5, 0, -55),
        CylinderObject_1(-88, 0, -55),
        CylinderObject_1(-87.5, 0, -55),
        CylinderObject_1(-26, 0, -55),
        CylinderObject_1(-25.5, 0, -55),
        CylinderObject_1(-25, 0, -55),
        CylinderObject_1(-24.5, 0, -55),
        CylinderObject_1(27, 0, -55),
        CylinderObject_1(26.5, 0, -55),
        CylinderObject_1(26, 0, -55),
        CylinderObject_1(25.5, 0, -55),
        CylinderObject_1(89, 0, -55),
        CylinderObject_1(88.5, 0, -55),
        CylinderObject_1(88, 0, -55),
        CylinderObject_1(87.5, 0, -55),
        CylinderObject_1(-89, 0, -91),
        CylinderObject_1(-88.5, 0, -91),
        CylinderObject_1(-88, 0, -91),
        CylinderObject_1(-87.5, 0, -91),
        CylinderObject_1(-26, 0, -91),
        CylinderObject_1(-25.5, 0, -91),
        CylinderObject_1(-25, 0, -91),
        CylinderObject_1(-24.5, 0, -91),
        CylinderObject_1(27, 0, -91),
        CylinderObject_1(26.5, 0, -91),
        CylinderObject_1(26, 0, -91),
        CylinderObject_1(25.5, 0, -91),
        CylinderObject_1(89, 0, -91),
        CylinderObject_1(88.5, 0, -91),
        CylinderObject_1(88, 0, -91),
        CylinderObject_1(87.5, 0, -91),
        # cylinders_2
        CylinderObject_2(-7, 0, -9),
        CylinderObject_2(7, 0, -9),
        CylinderObject_2(-85, 0, -9),
        CylinderObject_2(85, 0, -9),
        CylinderObject_2(-7, 0, -44.5),
        CylinderObject_2(7, 0, -44.5),
        CylinderObject_2(-85, 0, -44.5),
        CylinderObject_2(85, 0, -44.5),
        CylinderObject_2(-7, 0, -55),
        CylinderObject_2(7, 0, -55),
        CylinderObject_2(85, 0, -55),
        CylinderObject_2(-7, 0, -91),
        CylinderObject_2(7, 0, -91),
        CylinderObject_2(-85, 0, -91),
        CylinderObject_2(85, 0, -91),
        # cones
        ConeObject(0, 0, -9),
        ConeObject(-14, 0, -15),
        ConeObject(-14, 0, -20),
        ConeObject(-14, 0, -25),
        ConeObject(-14, 0, -30),
        ConeObject(-14, 0, -35),
        ConeObject(14, 0, -15),
        ConeObject(14, 0, -20),
        ConeObject(14, 0, -25),
        ConeObject(14, 0, -30),
        ConeObject(14, 0, -35),
        # barrier
        BarrierObject(-47.5, 0, -8),
        BarrierObject(49.5, 0, -54),
        BarrierObject(52, 0, -54),
        BarrierObject(54.5, 0, -54),
        BarrierObject(57, 0, -54),
        BarrierObject(59.5, 0, -54),
        BarrierObject(62, 0, -54),
        BarrierObject(64.5, 0, -54),
        BarrierObject(67, 0, -54),
        BarrierObject(47, 0, -92),
        BarrierObject(49.5, 0, -92),
        BarrierObject(52, 0, -92),
        BarrierObject(54.5, 0, -92),
        BarrierObject(57, 0, -92),
        BarrierObject(59.5, 0, -92),
        BarrierObject(62, 0, -92),
        BarrierObject(64.5, 0, -92),
        BarrierObject(67, 0, -92),
        BarrierObject(47, 0, -54),
    ]
    startCycle_1(c1)
    startCycle_1(c2, 3)
    startCycle_2(c3)
    startCycle_2(c4, 3)
    return objs


def draw_barriers():
    b = []
    for i in range(40):
        b.append(BarrierObject(0, 0, 0))
    b[0].posZ = -8
    b[0].posX = -45
    b[0].draw()

    b[0].posZ = -8
    b[0].posX = -47.5
    b[0].draw()

    b[2].posZ = -8
    b[2].posX = -50
    b[2].draw()

    b[3].posZ = -8
    b[3].posX = -52.5
    b[3].draw()

    b[4].posZ = -8
    b[4].posX = -55
    b[4].draw()

    b[5].posZ = -8
    b[5].posX = -57.5
    b[5].draw()

    b[6].posZ = -8
    b[6].posX = -60
    b[6].draw()

    b[7].posZ = -8
    b[7].posX = -62.5
    b[7].draw()

    b[8].posZ = -8
    b[8].posX = -65
    b[8].draw()

    b[9].posZ = -46
    b[9].posX = -45
    b[9].draw()

    b[10].posZ = -46
    b[10].posX = -47.5
    b[10].draw()

    b[11].posZ = -46
    b[11].posX = -50
    b[11].draw()

    b[12].posZ = -46
    b[12].posX = -52.5
    b[12].draw()

    b[13].posZ = -46
    b[13].posX = -55
    b[13].draw()

    b[14].posZ = -46
    b[14].posX = -57.5
    b[14].draw()

    b[15].posZ = -46
    b[15].posX = -60
    b[15].draw()

    b[16].posZ = -46
    b[16].posX = -62.5
    b[16].draw()

    b[17].posZ = -46
    b[17].posX = -65
    b[17].draw()

    b[18].posZ = -54
    b[18].posX = 47
    b[18].draw()

    b[1].posZ = -54
    b[1].posX = 49.5
    b[1].draw()

    b[2].posZ = -54
    b[2].posX = 52
    b[2].draw()

    b[3].posZ = -54
    b[3].posX = 54.5
    b[3].draw()

    b[4].posZ = -54
    b[4].posX = 57
    b[4].draw()

    b[5].posZ = -54
    b[5].posX = 59.5
    b[5].draw()

    b[6].posZ = -54
    b[6].posX = 62
    b[6].draw()

    b[7].posZ = -54
    b[7].posX = 64.5
    b[7].draw()

    b[8].posZ = -54
    b[8].posX = 67
    b[8].draw()

    b[9].posZ = -92
    b[9].posX = 47
    b[9].draw()

    b[10].posZ = -92
    b[10].posX = 49.5
    b[10].draw()

    b[11].posZ = -92
    b[11].posX = 52
    b[11].draw()

    b[12].posZ = -92
    b[12].posX = 54.5
    b[12].draw()

    b[13].posZ = -92
    b[13].posX = 57
    b[13].draw()

    b[14].posZ = -92
    b[14].posX = 59.5
    b[14].draw()

    b[15].posZ = -92
    b[15].posX = 62
    b[15].draw()

    b[16].posZ = -92
    b[16].posX = 64.5
    b[16].draw()

    b[17].posZ = -92
    b[17].posX = 67
    b[17].draw()
    print("###################################")
    for i in b:
        print("BarrierObject(", end='')
        print(i.posX, end='')
        print(",0,", end='')
        print(i.posZ, end='')
        print(")")
    print("###################################")
    return b
