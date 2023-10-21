#LIBRERIAS
import cv2
import numpy as np

from _py_librerias import Bluetooth as Bt
from _py_librerias import Camera as cam
from _py_librerias import xbox as xb

from _py_librerias import funciones_auxiliares as aux
from _py_librerias import control_robot as robotx
from _py_librerias import plot_graficas as pg

#------INICIALIZACION CAMARA------
#HD
resolucionx=1280
resoluciony=720
#Full HD
#resolucionx=1920
#resoluciony=1080
camara=cam.initialize(0,resolucionx,resoluciony)
texto_titulo=""
color=(0, 0, 255)

#------CONTROL XBOX------
control=xb.XboxController()

#------INICIALIZACION ROBOT------
print("Conectando Robot 0.....")
robot0=Bt.connect("98:D3:21:F7:B5:70")
print("Robot 0 OK")

print("Conectando Robot 1.....")
robot1=Bt.connect("98:D3:31:FA:17:5B")
print("Robot 1 OK")

print("Conectando Robot 2.....")
robot2=Bt.connect("98:D3:71:F6:63:9C")
print("Robot 2 OK")

print("Conectando Robot 3.....")
robot3=Bt.connect("98:D3:21:F7:B4:86")
print("Robot 3 OK")

# print("Conectando Robot 4.....")
# robot4=Bt.connect("00:21:06:08:16:21")
# print("Robot 4 OK")

# print("Conectando Robot 5.....")
# robot5=Bt.connect("00:21:06:08:18:AD")
# print("Robot 5 OK")

# print("Conectando Robot 7.....")
# robot7=Bt.connect("98:D3:31:F6:AC:8F")
# print("Robot 7 OK")

#robot4=Bt.connect("00:21:06:08:16:21")
#robot5=Bt.connect("00:21:06:08:18:AD")
#robot6=Bt.connect("00:21:06:08:17:60")
#robot7=Bt.connect("98:D3:31:F6:AC:8F")

robot_bt1=robot0
id_robot_bt1=0

robot_bt2=robot1
id_robot_bt2=1

robot_bt3=robot2
id_robot_bt3=2

robot_bt4=robot3
id_robot_bt4=3

robot=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
wmax=150 #Velocidad angular robot maxima
wmaxl=50 #Velocidad angular robot maxima
wmaxs=150 #Velocidad angular robot maxima
l=50 #distancia del centro del robot al centro de las llantas
r=58 #radio llanta (pixeles)
L=120 #distancia entre centros de llantas (pixeles)
a=250

#INICIALIZACION DE VALORES ROBOT FISICO 1
wd1=0
wi1=0
x1s=0
y1s=0

#INICIALIZACION DE VALORES ROBOT FISICO 2
wd2=0
wi2=0
xs2=0
ys2=0
C12x=-a/2
C12y=-np.sqrt((3*a*a)/4)
C32x=-a
C32y=0

#INICIALIZACION DE VALORES ROBOT FISICO 3
wd3=0
wi3=0
xs3=0
ys3=0
C13x=a/2
C13y=-np.sqrt((3*a*a)/4)
C23x=a
C23y=0

#INICIALIZACION DE VALORES ROBOT FISICO 3
wd4=0
wi4=0
xs4=0
ys4=0
C14x=0
C14y=-2*np.sqrt((3*a*a)/4)

#INICIALIZACION DE VARIABLES DE CONTROL ROBOT 1
x1=0
y1=0
th1=0
ex1=0
ey1=0
ux1=0
uy1=0

#INICIALIZACION DE VARIABLES DE CONTROL ROBOT 2
x2=0
y2=0
th2=0
ex2=0
ey2=0
ux2=0
uy2=0

#INICIALIZACION DE VARIABLES DE CONTROL ROBOT 3
x3=0
y3=0
th3=0
ex3=0
ey3=0
ux3=0
uy3=0

#INICIALIZACION DE VARIABLES DE CONTROL ROBOT 4
x4=0
y4=0
th4=0
ex4=0
ey4=0
ux4=0
uy4=0

#INICIALIZACION DE VARIABLES DE CONTROL GENERAL
i=0
t=0 #Tiempo

#------VALORES CONTROL------
k=100 #ganancia del control


while (True):

    #-------BUSQUEDA DE QR´s------
    #print("Buscamos aruco")
    frame, points, ids =cam.buscar_Aruco(camara, resolucionx, resoluciony)
    #print(ids)

    if len(points)>0:
        robot=cam.buscar_robots(points, ids, robot)
        #print("robot0(x="+str(robot[0][0])+",y="+str(robot[0][1])+",th="+str(robot[0][2])+")")

        #------LEY DE CONTROL TRAYECTORIA------

        #ROBOT LIDER 1
        x1=robot[id_robot_bt1][0]-(resolucionx/2) #Obtenemos valor X de QR robot 
        y1=robot[id_robot_bt1][1]-(resoluciony/2) #Obtenemos valor Y de QR robot 
        th1=robot[id_robot_bt1][2] #Obtenemos valor Th de robot 
        x1=x1+(l*np.cos(th1))
        y1=y1+(l*np.sin(th1))
        V1=0
        W1=0

        #ROBOT SEGUIDOR 2 posición
        x2=robot[id_robot_bt2][0]-(resolucionx/2) #Obtenemos valor X de QR robot 
        y2=robot[id_robot_bt2][1]-(resoluciony/2) #Obtenemos valor Y de QR robot 
        th2=robot[id_robot_bt2][2] #Obtenemos valor Th de robot 
        x2=x2+(l*np.cos(th2))
        y2=y2+(l*np.sin(th2))

        A2=np.array([[np.cos(th2), -l*np.sin(th2)],
            [np.sin(th2), l*np.cos(th2)]])
        
        #ROBOT SEGUIDOR 3 posición
        x3=robot[id_robot_bt3][0]-(resolucionx/2) #Obtenemos valor X de QR robot 
        y3=robot[id_robot_bt3][1]-(resoluciony/2) #Obtenemos valor Y de QR robot 
        th3=robot[id_robot_bt3][2] #Obtenemos valor Th de robot 
        x3=x3+(l*np.cos(th3))
        y3=y3+(l*np.sin(th3))

        A3=np.array([[np.cos(th3), -l*np.sin(th3)],
            [np.sin(th3), l*np.cos(th3)]])
        
        #ROBOT SEGUIDOR 4 posición
        x4=robot[id_robot_bt4][0]-(resolucionx/2) #Obtenemos valor X de QR robot 
        y4=robot[id_robot_bt4][1]-(resoluciony/2) #Obtenemos valor Y de QR robot 
        th4=robot[id_robot_bt4][2] #Obtenemos valor Th de robot 
        x4=x4+(l*np.cos(th4))
        y4=y4+(l*np.sin(th4))

        A4=np.array([[np.cos(th4), -l*np.sin(th4)],
            [np.sin(th4), l*np.cos(th4)]])

        #ROBOT SEGUIDOR 2 control       
        xs2=x1+C12x
        ys2=y1+C12y
        # xs2=(x1+C12x+x3+C32x)/2
        # ys2=(y1+C12y+y3+C32y)/2

        ex2=x2-xs2
        ey2=y2-ys2
        ux2=-k*ex2
        uy2=-k*ey2

        B2=np.array([ux2,uy2]) #Arreglo de Vector velocidad

        U2=np.linalg.solve(A2,B2)
        #U=np.linalg.inv(A)*B  No sirve

        V2=U2[0] #Velocidad Lineal
        W2=U2[1]  #Velocidad Angular

        #ROBOT SEGUIDOR 3 control       
        xs3=x1+C13x
        ys3=y1+C13y
        # xs3=(x1+C13x+x2+C23x)/2
        # ys3=(y1+C13y+y2+C23y)/2

        ex3=x3-xs3
        ey3=y3-ys3
        ux3=-k*ex3
        uy3=-k*ey3

        B3=np.array([ux3,uy3]) #Arreglo de Vector velocidad

        U3=np.linalg.solve(A3,B3)
        #U=np.linalg.inv(A)*B  No sirve

        V3=U3[0] #Velocidad Lineal
        W3=U3[1]  #Velocidad Angular

        #ROBOT SEGUIDOR 4 control       
        xs4=x1+C14x
        ys4=y1+C14y
        # xs4=(x1+C14x+x2+C24x)/2
        # ys4=(y1+C14y+y2+C24y)/2

        ex4=x4-xs4
        ey4=y4-ys4
        ux4=-k*ex4
        uy4=-k*ey4

        B4=np.array([ux4,uy4]) #Arreglo de Vector velocidad

        U4=np.linalg.solve(A4,B4)
        #U=np.linalg.inv(A)*B  No sirve

        V4=U4[0] #Velocidad Lineal
        W4=U4[1]  #Velocidad Angular
        
        #-------CONTROL REMOTO XBOX--------
        #Detectamos tecla presionada en control xbox
        xbox_a, xbox_b, xbox_x, xbox_y, xbox_rb =control.read_abxy()
        xbox_lb=control.read_lb()

        if xbox_y==1:  #Adelante
            V1=8700
            W1=0
            texto_titulo="RC CONTROL (adelante)"
            color=(35, 239, 11)
        elif xbox_a==1: #Atras
            V1=-8700
            W1=0
            texto_titulo="RC CONTROL (reversa)"
            color=(35, 239, 11)
        elif xbox_b==1: #Derecha
            V1=0
            W1=70
            texto_titulo="RC CONTROL (derecha)"
            color=(35, 239, 11)
        elif xbox_x==1: #Izquierda
            V1=0
            W1=-70
            texto_titulo="RC CONTROL (izquierda)"
            color=(35, 239, 11)
        elif xbox_rb==1:
            V1=0
            W1=0
            V2=0
            W2=0
            V3=0
            W3=0
            V4=0
            W4=0
            break
        else:
            V1=0
            W1=0
            texto_titulo="RC CONTROL (detener)"
            color=(35, 239, 11)

        if xbox_lb==1:
            texto_titulo="FORMACION 3-robots (auto)"
            color=(0, 0, 255)
            cam.draw_punto(frame,"X2s,Y2s",(0,0,255), int(xs2)+(int(resolucionx/2)), int(ys2)+(int(resoluciony/2)),resolucionx,resoluciony)
            cam.draw_punto(frame,"X3s,Y3s",(0,0,255), int(xs3)+(int(resolucionx/2)), int(ys3)+(int(resoluciony/2)),resolucionx,resoluciony)
            cam.draw_punto(frame,"X4s,Y4s",(0,0,255), int(xs4)+(int(resolucionx/2)), int(ys4)+(int(resoluciony/2)),resolucionx,resoluciony)
    
        else:
            V2=0
            W2=0
            V3=0
            W3=0
            V4=0
            W4=0

        #-------MODELO CINEMATICO ROBOT 1-------- 
        wd1= (V1/r)+((L*W1)/(2*r)) #Calulo de wd robot unicilo
        wi1= (V1/r)-((L*W1)/(2*r)) #Calulo de wi robot unicilo

        if(wd1>wmaxl):
            wd1=wmaxl
        elif(wd1<-wmaxl):
            wd1=-wmaxl

        if(wi1>wmaxl):
            wi1=wmaxl
        elif(wi1<-wmaxl):
            wi1=-wmaxl

        #print("wd="+str(wd)+"wi="+str(wi))
        #print("robot0(x="+str("%.0f" % x[i])+"y="+str("%.0f" % y[i])+"th="+str("%.2f" % th[i])+", ux="+str("%.0f" % ux[i])+", uy="+str("%.0f" % uy[i])+", V="+str("%.0f" % V)+", W="+str("%.0f" % W)+", wd="+str("%.0f" % wd)+"wi="+str("%.0f" % wi))
        Bt.move(robot_bt1,wd1, wi1)

        #-------MODELO CINEMATICO ROBOT 2-------- 
        wd2= (V2/r)+((L*W2)/(2*r)) #Calulo de wd robot unicilo
        wi2= (V2/r)-((L*W2)/(2*r)) #Calulo de wi robot unicilo

        if(wd2>wmaxs):
            wd2=wmaxs
        elif(wd2<-wmaxs):
            wd2=-wmaxs

        if(wi2>wmaxs):
            wi2=wmaxs
        elif(wi2<-wmaxs):
            wi2=-wmaxs

        #print("wd="+str(wd)+"wi="+str(wi))
        #print("robot0(x="+str("%.0f" % x[i])+"y="+str("%.0f" % y[i])+"th="+str("%.2f" % th[i])+", ux="+str("%.0f" % ux[i])+", uy="+str("%.0f" % uy[i])+", V="+str("%.0f" % V)+", W="+str("%.0f" % W)+", wd="+str("%.0f" % wd)+"wi="+str("%.0f" % wi))
        Bt.move(robot_bt2,wd2, wi2)

        #-------MODELO CINEMATICO ROBOT 3-------- 
        wd3= (V3/r)+((L*W3)/(2*r)) #Calulo de wd robot unicilo
        wi3= (V3/r)-((L*W3)/(2*r)) #Calulo de wi robot unicilo

        if(wd3>wmaxs):
            wd3=wmaxs
        elif(wd3<-wmaxs):
            wd3=-wmaxs

        if(wi3>wmaxs):
            wi3=wmaxs
        elif(wi3<-wmaxs):
            wi3=-wmaxs

        #print("wd="+str(wd)+"wi="+str(wi))
        #print("robot0(x="+str("%.0f" % x[i])+"y="+str("%.0f" % y[i])+"th="+str("%.2f" % th[i])+", ux="+str("%.0f" % ux[i])+", uy="+str("%.0f" % uy[i])+", V="+str("%.0f" % V)+", W="+str("%.0f" % W)+", wd="+str("%.0f" % wd)+"wi="+str("%.0f" % wi))
        Bt.move(robot_bt3,wd3, wi3)

        #-------MODELO CINEMATICO ROBOT 4-------- 
        wd4= (V4/r)+((L*W4)/(2*r)) #Calulo de wd robot unicilo
        wi4= (V4/r)-((L*W4)/(2*r)) #Calulo de wi robot unicilo

        if(wd4>wmaxs):
            wd4=wmaxs
        elif(wd4<-wmaxs):
            wd4=-wmaxs

        if(wi4>wmaxs):
            wi4=wmaxs
        elif(wi4<-wmaxs):
            wi4=-wmaxs

        #print("wd="+str(wd)+"wi="+str(wi))
        #print("robot0(x="+str("%.0f" % x[i])+"y="+str("%.0f" % y[i])+"th="+str("%.2f" % th[i])+", ux="+str("%.0f" % ux[i])+", uy="+str("%.0f" % uy[i])+", V="+str("%.0f" % V)+", W="+str("%.0f" % W)+", wd="+str("%.0f" % wd)+"wi="+str("%.0f" % wi))
        Bt.move(robot_bt4,wd4, wi4)

    #-------VENTANA DE CAMARA-------- 
    cam.dibujar_aruco(frame, points, ids, resolucionx,resoluciony)
    cam.draw_texto_titulo(frame, texto_titulo,color)
    cam.draw_punto(frame,"X1,Y1",(0,0,255), int(x1)+(int(resolucionx/2)), int(y1)+(int(resoluciony/2)),resolucionx,resoluciony)
    #cam.draw_punto(frame,"X2s,Y2s",(0,0,255), int(xs2)+(int(resolucionx/2)), int(ys2)+(int(resoluciony/2)),resolucionx,resoluciony)
    cv2.imshow('Camara detector qr', frame) #Despliega la ventana 

    if cv2.waitKey(1) & 0xFF == 27: #Presiona esc para salir 
        break

#-------RUTINA DE CIERRE-------- 
Bt.move(robot_bt1,0,0)  #Apagamos motores en Robot 1
Bt.disconnect(robot_bt1) #Desconectamos Bluetooth 1
Bt.move(robot_bt2,0,0)  #Apagamos motores en Robot 2
Bt.disconnect(robot_bt2) #Desconectamos Bluetooth 2
Bt.move(robot_bt3,0,0)  #Apagamos motores en Robot 3
Bt.disconnect(robot_bt3) #Desconectamos Bluetooth 3
Bt.move(robot_bt4,0,0)  #Apagamos motores en Robot 3
Bt.disconnect(robot_bt4) #Desconectamos Bluetooth 3
camara.release() #Liberamos Camara
cv2.destroyAllWindows() #Cerramos ventanas
