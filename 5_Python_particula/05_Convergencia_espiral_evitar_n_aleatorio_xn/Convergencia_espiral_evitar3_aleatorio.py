import numpy as np
import datetime
import random

import plot_graficas as pg
import funciones_auxiliares as aux
import control_robot as robot

def aleatorio_3_particula(iteration, aleatorios):
    #ITERACIONES DE SIMULACION
    tfin=600

    #NUMERO DE ELEMTOS REPULSIVOS ALEATORIOS
    vmin=2
    vmax=30
    xr = [random.randrange(vmin, vmax, 3) for i in range(aleatorios)]
    yr = [random.randrange(vmin, vmax, 3) for i in range(aleatorios)]

    #INICIALIZACION DE VARIABLES
    x,y,t,ex,ey =aux.inicializar_arreglos(tfin)
    x[0]=0 #Valor inicial x
    y[0]=0 #Valor inicial y

    #VALORES CONTROL
    xs=random.randint(vmin, vmax) #valor esperado de x
    ys=random.randint(vmax+2, vmax+5) #valor y deseado
    k=0.01 #ganancia del control

    for i in range(0,tfin):
        ex[i]=x[i]-xs
        ey[i]=y[i]-ys

        ax, ay =robot.potencial_atractivo_espiral(ex[i],ey[i],k,0.01)
        ux=ax
        uy=ay

        for j in range(aleatorios):
            RX, RY =robot.potencial_repulsivo(x[i],y[i],xr[j],yr[j],2,0.1)
            ux=ux+RX
            uy=uy+RY

        #Valores siguientes
        x[i+1]=x[i]+ux #X[1]=X(0)+V*t
        y[i+1]=y[i]+uy #Y[1]=Y(0)+V*t

    ex[tfin]=ex[tfin-1]
    ey[tfin]=ey[tfin-1]

    e = datetime.datetime.now()
    pg.plot_xy_x0y0_xsys_xyr(e,x, y, xs, ys, xr, yr, aleatorios, iteration)
    #pg.plot_error_x_(e,ex,t) #error en x vs tiempo
    #pg.plot_error_y_(e,ey,t) #error en y vs tiempo
    #pg.plot_x_(e,x,t) #posicion en x vs tiempo
    #pg.plot_y_(e,y,t) #posicion en y vs tiempo

