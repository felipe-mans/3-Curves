from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    f = open( fname )
    data = f.read()
    data = data.split("\n")
    i = 0
    while i < len(data):
        if data[i] == "line":
            param = data[i+1].split(' ')
            add_edge( points, float(param[0]), float(param[1]), float(param[2]), float(param[3]), float(param[4]), float(param[5]) )
            i += 2
        elif data[i] == "circle":
            param = data[i+1].split(' ')
            add_circle( points, float(param[0]), float(param[1]), 0, float(param[2]), 1 )
            i += 2
        elif data[i] == "hermite":
            param = data[i+1].split(' ')
            add_curve( points, float(param[0]), float(param[1]), float(param[2]), float(param[3]), float(param[4]), float(param[5]), float(param[6]), float(param[7]), 0.001, "hermite" )
            i += 2
        elif data[i] == "bezier":
            param = data[i+1].split(' ')
            add_curve( points, float(param[0]), float(param[1]), float(param[2]), float(param[3]), float(param[4]), float(param[5]), float(param[6]), float(param[7]), 0.001, "bezier" )
            i += 2
        elif data[i] == "xrotate":
            param = data[i+1]
            trans = make_rotX(math.radians(float(param)))
            matrix_mult(trans, transform)
            i += 2
        elif data[i] == "yrotate":
            param = data[i+1]
            trans = make_rotY(math.radians(float(param)))
            i += 2
        elif data[i] == "zrotate":
            param = data[i+1]
            trans = make_rotZ(math.radians(float(param)))
            i += 2
        elif data[i] == "ident":
            ident( transform )
        elif data[i] == "apply":
            matrix_mult( transform, points )
        elif data[i] == "scale":
            param = data[i+1].split( " " )
            m = make_scale(float(prama[0]), float(param[1]), float(param[2]), transform )
            matrix_mult( m, transform )
        elif data[i] == "translate":
            param = data[i+1].split(' ')
            matrix_mult( make_translate(float(param[0]), float(param[1]), float(param[2]), transform ) )
        elif data[i] == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display( screen )
            i += 1
        elif data[i] == "save":
            fname = data[i+1]
            save_ppm( screen, fname )
            i += 2
        elif data[i] == "quit":
            return

        else:
            print ""
