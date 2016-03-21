from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    f = open( fname )
    data = f.read()
    data = b.split("\n")
    i = 0
    while i < len(data):
        if (data[i] == "line"):
            param = data[i+1]
            add_edge( points, param[0], param[1], param[2], param[3], param[4], param[5] )
            i += 2
        elif (data[i] == "circle"):
            param = data[i+1]
            add_circle( points, param[0], param[1], param[2], param[3], 0.001 )
            i += 2
        elif (data[i] == "hermite"):
            param = data[i+1]
            add_curve( points, param[0], param[1], param[2], param[3], param[4], param[5], param[6], pram[7], 0.001, "hermite" )
            i += 2
        elif (data[i] == "bezier"):
            param = data[i+1]
            add_curve( points, param[0], param[1], param[2], param[3], param[4], param[5], param[6], pram[7], 0.001, "bezier")
            i += 2
        elif (data[i] == "xrotate"):
            param = data[i+1]
            transform = make_rotX(param[0])
            i += 2
        elif (data[i] == "yrotate"):
            param = data[i+1]
            transform = make_rotY(param[0])
            i += 2
        elif (data[i] == "zrotate"):
            param = data[i+1]
            transform = make_rotZ(param[0])
            i += 2
