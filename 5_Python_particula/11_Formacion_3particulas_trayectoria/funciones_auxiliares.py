
#Funcion para inicializar los arreglos vacios
def inicializar_circulo(j):

    mcirc_x= [0.0 for i in range(j+1)]
    mcirc_y= [0.0 for i in range(j+1)]

    return mcirc_x,mcirc_y

def inicializar_arreglos(j):

    x = [0.0 for i in range(j+1)]
    y = [0.0 for i in range(j+1)]
    t = [i for i in range(j+1)]
    ex = [0.0 for i in range(j+1)]
    ey= [0.0 for i in range(j+1)]
    mcirc_x= [0.0 for i in range(j+1)]
    mcirc_y= [0.0 for i in range(j+1)]

    return x,y,t,ex,ey,mcirc_x,mcirc_y

def inicializar_3particulas(j):

    x1 = [0.0 for i in range(j+1)]
    y1 = [0.0 for i in range(j+1)]
    x2 = [0.0 for i in range(j+1)]
    y2 = [0.0 for i in range(j+1)]
    x3 = [0.0 for i in range(j+1)]
    y3 = [0.0 for i in range(j+1)]

    return x1,y1,x2,y2,x3,y3

def inicializar_3errores(j):

    ex1 = [0.0 for i in range(j+1)]
    ey1 = [0.0 for i in range(j+1)]
    ex2 = [0.0 for i in range(j+1)]
    ey2 = [0.0 for i in range(j+1)]
    ex3 = [0.0 for i in range(j+1)]
    ey3 = [0.0 for i in range(j+1)]

    return ex1,ey1,ex2,ey2,ex3,ey3

def inicializar_tiempo(j):

    t = [i for i in range(j+1)]

    return t