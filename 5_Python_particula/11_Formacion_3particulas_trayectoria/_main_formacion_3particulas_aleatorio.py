import numpy as np
import datetime
import random

import plot_graficas as pg
import funciones_auxiliares as aux
import control_robot as robot

#ITERACIONES DE SIMULACION
tfin=800

#INICIALIZACION DE VARIABLES
x1,y1,x2,y2,x3,y3 =aux.inicializar_3particulas(tfin)
ex1,ey1,ex2,ey2,ex3,ey3=aux.inicializar_3errores(tfin)
mcirc_x,mcirc_y=aux.inicializar_circulo(tfin)
t =aux.inicializar_tiempo(tfin)
x1[0]=0 #Valor inicial x particula1
y1[0]=0#Valor inicial y particula1
x2[0]=5#Valor inicial x particula1
y2[0]=0 #Valor inicial y particula1
x3[0]=10 #Valor inicial x particula1
y3[0]=0 #Valor inicial y particula1

#VALORES CONTROL y FORMACION
k=0.1 #ganancia del control
a=5 #Distancia entre particulas
C21x=a/2
C21y=np.sqrt((3*a*a)/4)
C32x=-a
C32y=0
C13x=a/2
C13y=-np.sqrt((3*a*a)/4)

#VALORES TRAYECTORIA
T=100
w=(2*3.1416)/T
cx=0
cy=0
rad=3

for i in range(0,tfin):

    #Posiciones Deseadas formacion
    x2s=x3[i]+C32x
    y2s=y3[i]+C32y
    x3s=x1[i]+C13x
    y3s=y1[i]+C13y

    #Convergencia directa
    ex1[i],ey1[i],x1[i+1],y1[i+1],mcirc_x[i],mcirc_y[i]= robot.trayectoria_xyr2(x1[i],y1[i],k,cx,cy,rad,w,t[i],x3[i],y3[i],x2[i],y2[i])
    ex2[i],ey2[i],x2[i+1],y2[i+1]= robot.convergencia_xyr2(x2[i],y2[i],x2s,y2s,k*4,x3[i],y3[i],x1[i],y1[i])
    ex3[i],ey3[i],x3[i+1],y3[i+1]= robot.convergencia_xyr2(x3[i],y3[i],x3s,y3s,k*4,x2[i],y2[i],x1[i],y1[i])

ex1[tfin]=ex1[tfin-1]
ey1[tfin]=ey1[tfin-1]
mcirc_x[tfin]=mcirc_x[tfin-1]
mcirc_y[tfin]=mcirc_y[tfin-1]


e = datetime.datetime.now()
pg.plot_xy_3particulas_trayectoria(e,x1,y1,x2,y2,x3,y3,mcirc_x,mcirc_y,1)
#pg.plot_error_x_(e,ex,t)
#pg.plot_error_y_(e,ey,t)
#pg.plot_x_(e,x,t)
#pg.plot_y_(e,y,t)

