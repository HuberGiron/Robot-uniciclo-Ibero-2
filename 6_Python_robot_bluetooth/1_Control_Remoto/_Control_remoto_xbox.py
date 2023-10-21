#LIBRERIAS
from _py_librerias import xbox as xb
from _py_librerias import Bluetooth as Bt #Bluetoot
import time

#INICIALIZACION ROBOT Y CAMARA
robot0=Bt.connect("98:D3:21:F7:B5:70")
#robot1=Bt.connect("98:D3:31:FA:17:5B")
#robot2=Bt.connect("98:D3:71:F6:63:9C")
#robot3=Bt.connect("98:D3:21:F7:B4:86")

#robot4=Bt.connect("00:21:06:08:16:21")
#robot5=Bt.connect("00:21:06:08:18:AD")
#robot6=Bt.connect("00:21:06:08:17:60")
#robot7=Bt.connect("98:D3:31:F6:AC:8F")

robot_bt=robot0 #Seleccion del robot a utilizar en el programa

#CONTROL XBOX
control=xb.XboxController()

#PARAMETROS ROBOT UNICILO
wmax=150 #Velocidad angular robot maxima
r=58 #radio llanta (pixeles)
L=120 #distancia entre centros de llantas (pixeles)

#INICIALIZACION DE VALORES ROBOT FISICO
V=0 #Velocidad Vx inicial
W=0 #Velocidad angular robot inicial
wd=0 #Velocidad angular motor derecho
wi=0 #Velocidad angular motor izquierdo

#PROGRAMA PRINCIPAL
while (True):

    wd= (V/r)+((L*W)/(2*r)) #Calulo de wd robot unicilo
    wi= (V/r)-((L*W)/(2*r)) #Calulo de wi robot unicilo

    if(wd>wmax):    #Normalizamos el valor de wd a wmax 
        wd=wmax
    elif(wd<-wmax):
        wd=-wmax

    if(wi>wmax):    #Normalizamos el valor de wi a wmax 
        wi=wmax
    elif(wi<-wmax):
        wi=-wmax

    # Mostrar CALCULOS
    print("V="+str(V)+"W="+str(W))  #Imprimir V y W
    print("wd="+str(wd)+"wi="+str(wi)) #Imprimir wi y wd

    #Control bluetooth y camara
    Bt.move(robot_bt,wd,wi)
    time.sleep(0.1)
    

    #Detectamos tecla presionada en control xbox
    print(control.read_abxy())
    a, b, x, y, rb =control.read_abxy()
    if y==1:
        V=8700
        W=0
    elif a==1:
        V=-8700
        W=0
    elif b==1:
        V=0
        W=70
    elif x==1:
        V=0
        W=-70
    elif rb==1:
        V=0
        W=0
        break
    else:
        V=0
        W=0  

#FINALIZAR EL PROGRAMA
Bt.move(robot_bt,0,0)   #Enviamos wd y wi en cero a robot bluetooth para detenerlo
Bt.disconnect(robot_bt) #Desconectamos Bluetooth