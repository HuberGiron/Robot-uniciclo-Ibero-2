import numpy as np
import datetime
import random

import plot_graficas as pg
import funciones_auxiliares as aux
import control_robot as robot

#ITERACIONES DE SIMULACION
tfin=600

#INICIALIZACION DE VARIABLES
x,y,t,ex,ey,mcirc_x,mcirc_y =aux.inicializar_arreglos(tfin)
x[0]=0 #Valor inicial x
y[0]=0 #Valor inicial y

#VALORES CONTROL
k=0.1 #ganancia del control

#VALORES TRAYECTORIA
T=100
w=(2*3.1416)/T
cx=0
cy=0
rad=3

for i in range(0,tfin):

    mx=cx+rad*np.cos(w*t[i])
    mcirc_x[i]=mx
    my=cy+rad*np.sin(w*t[i])
    mcirc_y[i]=my
    mxp=-rad*w*np.sin(w*t[i])
    myp=rad*w*np.cos(w*t[i])

    ex[i]=x[i]-mx
    ey[i]=y[i]-my

    ux=-k*ex[i]+mxp
    uy=-k*ey[i]+myp

    #Valores siguientes
    x[i+1]=x[i]+ux #X[1]=X(0)+V*t
    y[i+1]=y[i]+uy #Y[1]=Y(0)+V*t

ex[tfin]=ex[tfin-1]
ey[tfin]=ey[tfin-1]
mcirc_x[tfin]=mcirc_x[tfin-1]
mcirc_y[tfin]=mcirc_y[tfin-1]

print(mcirc_x)
e = datetime.datetime.now()
pg.plot_xy_x0y0_trayectoria(e,x, y, mcirc_x, mcirc_y)
pg.plot_error_x_(e,ex,t)
pg.plot_error_y_(e,ey,t)
pg.plot_x_(e,x,t)
pg.plot_y_(e,y,t)

