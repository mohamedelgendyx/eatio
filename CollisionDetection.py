from gameobject import *
from math import *
def test_cu (r,center_x,center_y,l,w,ce_x,ce_y):
    L = l/2
    W = w/2
    r_x = ce_x + W
    #l_x = ce_x
    l_x = ce_x - W
    t_y = ce_y + L
    #b_y = ce_y
    b_y = ce_y - L
    if center_x <= l_x:
        test_x = l_x
    else:
        if center_x >= (r_x):
            test_x = r_x
        else:
            test_x = center_x

    if center_y <= b_y:
        test_y = b_y
    else:
        if center_y >= (t_y):
            test_y = t_y
        else:
            test_y = center_y

    dist_x = center_x - test_x
    dist_y = center_y - test_y
    distance = sqrt((dist_x * dist_x) + (dist_y * dist_y))

    if distance <= r:
        return True
    else:
        return False