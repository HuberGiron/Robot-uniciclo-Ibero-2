import numpy as np
import datetime
import random

import plot_graficas as pg
import funciones_auxiliares as aux
import control_robot as robot

#ITERACIONES DE SIMULACION
tfin=600

#INICIALIZACION DE VARIABLES
x,y,t,ex,ey =aux.inicializar_arreglos(tfin)
x[0]=random.randint(0, 9) #Valor inicial x
y[0]=random.randint(0, 9) #Valor inicial y

#VALORES CONTROL
xs=random.randint(0, 9) #valor esperado de x
ys=random.randint(0, 9) #valor y deseado
k=0.01 #ganancia del control

xr1=random.randint(0, 9) #valor repulsivo xr1
yr1=random.randint(0, 9) #valor repulsivo yr1
xr2=random.randint(0, 9) #valor repulsivo xr2
yr2=random.randint(0, 9) #valor repulsivo yr2
xr3=random.randint(0, 9) #valor repulsivo xr3
yr3=random.randint(0, 9)#valor repulsivo yr3

for i in range(0,tfin):
    ex[i],ey[i],x[i+1],y[i+1]=robot.convergencia_xyr3_espiral(x[i],y[i],xs,ys,k,xr1,yr1,xr2,yr2,xr3,yr3)

ex[tfin]=ex[tfin-1]
ey[tfin]=ey[tfin-1]

e = datetime.datetime.now()
pg.plot_xy_x0y0_xsys_xyr3(e,x,y,xs,ys,xr1,yr1,xr2,yr2,xr3,yr3)
pg.plot_error_x_(e,ex,t)
pg.plot_error_y_(e,ey,t)
pg.plot_x_(e,x,t)
pg.plot_y_(e,y,t)

