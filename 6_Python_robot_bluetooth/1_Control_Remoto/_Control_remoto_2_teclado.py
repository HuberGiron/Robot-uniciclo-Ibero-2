#LIBRERIAS
from _py_librerias  import Bluetooth as Bt #Bluetooth
from _py_librerias  import Camera as cam #Camara
import cv2 #Opencv2

#INICIALIZACION ROBOT Y CAMARA
robot0=Bt.connect("98:D3:21:F7:B5:70")
robot1=Bt.connect("98:D3:31:FA:17:5B")
#robot2=Bt.connect("98:D3:71:F6:63:9C")
#robot3=Bt.connect("98:D3:21:F7:B4:86")

robot_bt1=robot0 #Seleccion del robot a utilizar en el programa
robot_bt2=robot1 #Seleccion del robot a utilizar en el programa

#RESOLUCION CAMARA HD
resolucionx=1280
resoluciony=720
camara=cam.initialize(0,resolucionx,resoluciony)

#PARAMETROS ROBOT UNICILO
wmax=150 #Velocidad angular robot maxima
r=58 #radio llanta (pixeles)
L=120 #distancia entre centros de llantas (pixeles)

#INICIALIZACION DE VALORES ROBOT FISICO 1
V1=0 #Velocidad Vx inicial
W1=0 #Velocidad angular robot inicial
wd1=0 #Velocidad angular motor derecho
wi1=0 #Velocidad angular motor izquierdo

#INICIALIZACION DE VALORES ROBOT FISICO 2
V2=0 #Velocidad Vx inicial
W2=0 #Velocidad angular robot inicial
wd2=0 #Velocidad angular motor derecho
wi2=0 #Velocidad angular motor izquierdo

#PROGRAMA PRINCIPAL
while (True):

    #CALULOS VELOCIDAD ANGULAR ROBOT FISICO 1
    print("V="+str(V1)+"W="+str(W1))  #Imprimir V y W

    wd= (V1/r)+((L*W1)/(2*r)) #Calulo de wd robot unicilo
    wi= (V1/r)-((L*W1)/(2*r)) #Calulo de wi robot unicilo

    if(wd1>wmax):    #Normalizamos el valor de wd a wmax 
        wd1=wmax
    elif(wd1<-wmax):
        wd1=-wmax

    if(wi1>wmax):    #Normalizamos el valor de wi a wmax 
        wi1=wmax
    elif(wi1<-wmax):
        wi1=-wmax
        
    #CALULOS VELOCIDAD ANGULAR ROBOT FISICO 1
    print("V="+str(V2)+"W="+str(W2))  #Imprimir V y W

    wd= (V2/r)+((L*W2)/(2*r)) #Calulo de wd robot unicilo
    wi= (V2/r)-((L*W2)/(2*r)) #Calulo de wi robot unicilo

    if(wd2>wmax):    #Normalizamos el valor de wd a wmax 
        wd2=wmax
    elif(wd2<-wmax):
        wd2=-wmax

    if(wi2>wmax):    #Normalizamos el valor de wi a wmax 
        wi2=wmax
    elif(wi2<-wmax):
        wi2=-wmax

        # Mostrar CALCULOS
    print("V1="+str(V1)+"W1="+str(W1))  #Imprimir V y W
    print("wd1="+str(wd1)+"wi1="+str(wi1)) #Imprimir wi y wd
    print("V2="+str(V2)+"W2="+str(W2))  #Imprimir V y W
    print("wd2="+str(wd2)+"wi2="+str(wi2)) #Imprimir wi y wd

    #Control bluetooth y camara
    Bt.move(robot_bt1,wd1,wi1)
    Bt.move(robot_bt1,wd2,wi2)
    cam.preview(camara,resolucionx, resoluciony)

    #Detectamos tecla presionada en teclado
    k=cv2.waitKey(33)
    if k == 27: #Presiona esc para salir 
        break
    elif k == 32: #Presiona space para detener ambos robot
        V1=0
        W1=0
        V2=0
        W3=0
    elif k == 119: #Presiona w para avanzar
        V1=8700
        W1=0
    elif k == 115: #Presiona s para ir atras
        V1=-8700
        W1=0
    elif k == 100: #Presiona d para rotar derecha
        V1=0
        W1=70
    elif k== 97: #Presiona a para rotar izquierda
        V1=0
        W1=-70
    elif k == 56: #Presiona 8 para avanzar
        V2=8700
        W2=0
    elif k == 53: #Presiona 2 para regresar
        V2=-8700
        W2=0
    elif k == 54: #Presiona 6 para rotar derecha
        V2=0
        W2=70
    elif k== 52: #Presiona 4 para rotar izquierda
        V2=0
        W2=-70
    
Bt.move(robot_bt1,0,0) #Enviamos wd y wi en cero a robot 1 bluetooth para detenerlo
Bt.move(robot_bt2,0,0) #Enviamos wd y wi en cero a robot 2 bluetooth para detenerlo
Bt.disconnect(robot_bt1) #Desconectamos Bluetooth
Bt.disconnect(robot_bt2) #Desconectamos Bluetooth
camara.release()        #Liberamos la camara
cv2.destroyAllWindows() #Cerramos todas las ventanas