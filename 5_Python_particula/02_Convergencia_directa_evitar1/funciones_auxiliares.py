
#Funcion para inicializar los arreglos vacios
def inicializar_arreglos(j):
    x=[]
    y=[]
    t=[]
    ex=[]
    ey=[]

    x = [0.0 for i in range(j+1)]
    y = [0.0 for i in range(j+1)]
    t = [i for i in range(j+1)]
    ex = [0.0 for i in range(j+1)]
    ey= [0.0 for i in range(j+1)]

    return x,y,t,ex,ey
