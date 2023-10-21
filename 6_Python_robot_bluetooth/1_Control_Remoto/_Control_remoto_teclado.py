#LIBRERIAS
from _py_librerias  import Bluetooth as Bt #Bluetooth
from _py_librerias  import Camera as cam #Camara
import cv2 #Opencv2

#INICIALIZACION ROBOT Y CAMARA
#robot0=Bt.connect("98:D3:21:F7:B5:70")
robot1=Bt.connect("98:D3:31:FA:17:5B")
#robot2=Bt.connect("98:D3:71:F6:63:9C")
#robot3=Bt.connect("98:D3:21:F7:B4:86")

robot_bt=robot1 #Seleccion del robot a utilizar en el programa

#RESOLUCION CAMARA HD
resolucionx=1280
resoluciony=720
camara=cam.initialize(1,resolucionx,resoluciony)

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
    cam.preview(camara,resolucionx, resoluciony)

    #Detectamos tecla presionada en teclado
    k=cv2.waitKey(33)
    if k == 27: #Presiona esc para salir 
        break
    elif k == 32: #Presiona space para detener
        V=0
        W=0
    elif k == 119: #Presiona w para avanzar
        V=8700
        W=0
    elif k == 115: #Presiona s para ir atras
        V=-8700
        W=0
    elif k == 100: #Presiona d para rotar derecha
        V=0
        W=70
    elif k== 97: #Presiona a para rotar izquierda
        V=0
        W=-70

#FINALIZAR EL PROGRAMA
Bt.move(robot_bt,0,0)   #Enviamos wd y wi en cero a robot bluetooth para detenerlo
Bt.disconnect(robot_bt) #Desconectamos Bluetooth
camara.release()        #Liberamos la camara
cv2.destroyAllWindows() #Cerramos todas las ventanas