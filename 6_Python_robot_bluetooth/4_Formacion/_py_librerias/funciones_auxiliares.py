
#Funcion para inicializar los arreglos vacios
def inicializar_arreglos(j):
    x=[]
    y=[]
    t=[]
    ex=[]
    ey=[]
    ux=[]
    uy=[]
    th=[]

    x = [0.0 for i in range(j+1)]
    y = [0.0 for i in range(j+1)]
    t = [i for i in range(j+1)]
    ex = [0.0 for i in range(j+1)]
    ey= [0.0 for i in range(j+1)]
    ux = [0.0 for i in range(j+1)]
    uy = [0.0 for i in range(j+1)]
    th = [i for i in range(j+1)]

    return x,y,th,t,ex,ey,ux,uy

def inicializar_arreglos2(j):
    x=[]
    y=[]
    t=[]
    ex=[]
    ey=[]
    ux=[]
    uy=[]
    th=[]
    mx=[]
    my=[]

    x = [0.0 for i in range(j+1)]
    y = [0.0 for i in range(j+1)]
    t = [i for i in range(j+1)]
    ex = [0.0 for i in range(j+1)]
    ey= [0.0 for i in range(j+1)]
    ux = [0.0 for i in range(j+1)]
    uy = [0.0 for i in range(j+1)]
    th = [i for i in range(j+1)]
    mx = [0.0 for i in range(j+1)]
    my = [0.0 for i in range(j+1)]

    return x,y,th,t,ex,ey,ux,uy,mx,my
