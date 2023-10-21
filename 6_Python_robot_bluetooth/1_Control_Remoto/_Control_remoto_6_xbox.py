#LIBRERIAS
from _py_librerias import xbox as xb
from _py_librerias import Bluetooth as Bt #Bluetoot
import time

#INICIALIZACION ROBOT Y CAMARA

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

print("Conectando Robot 4.....")
robot4=Bt.connect("00:21:06:08:16:21")
print("Robot 4 OK")

print("Conectando Robot 5.....")
robot5=Bt.connect("00:21:06:08:18:AD")
print("Robot 5 OK")

# print("Conectando Robot 6.....")
# robot6=Bt.connect("00:21:06:08:17:60")
# print("Robot 6 OK")

# print("Conectando Robot 7.....")
# robot7=Bt.connect("98:D3:31:F6:AC:8F")
# print("Robot 7 OK")


robot_bt1=robot0 #Seleccion del robot a utilizar en el programa
robot_bt2=robot1 #Seleccion del robot a utilizar en el programa
robot_bt3=robot2 #Seleccion del robot a utilizar en el programa
robot_bt4=robot3 #Seleccion del robot a utilizar en el programa
robot_bt5=robot4 #Seleccion del robot a utilizar en el programa
robot_bt6=robot5 #Seleccion del robot a utilizar en el programa

#CONTROL XBOX
control=xb.XboxController()

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

#INICIALIZACION DE VALORES ROBOT FISICO 3
V3=0 #Velocidad Vx inicial
W3=0 #Velocidad angular robot inicial
wd3=0 #Velocidad angular motor derecho
wi3=0 #Velocidad angular motor izquierdo

#INICIALIZACION DE VALORES ROBOT FISICO 4
V4=0 #Velocidad Vx inicial
W4=0 #Velocidad angular robot inicial
wd4=0 #Velocidad angular motor derecho
wi4=0 #Velocidad angular motor izquierdo

#INICIALIZACION DE VALORES ROBOT FISICO 5
V5=0 #Velocidad Vx inicial
W5=0 #Velocidad angular robot inicial
wd5=0 #Velocidad angular motor derecho
wi5=0 #Velocidad angular motor izquierdo

#INICIALIZACION DE VALORES ROBOT FISICO 6
V6=0 #Velocidad Vx inicial
W6=0 #Velocidad angular robot inicial
wd6=0 #Velocidad angular motor derecho
wi6=0 #Velocidad angular motor izquierdo


#PROGRAMA PRINCIPAL
while (True):

    #Calculo velocidad Angular de llantas robot 1
    wd1= (V1/r)+((L*W1)/(2*r)) #Calulo de wd robot unicilo
    wi1= (V1/r)-((L*W1)/(2*r)) #Calulo de wi robot unicilo

    if(wd1>wmax):    #Normalizamos el valor de wd a wmax 
        wd1=wmax
    elif(wd1<-wmax):
        wd1=-wmax

    if(wi1>wmax):    #Normalizamos el valor de wi a wmax 
        wi1=wmax
    elif(wi1<-wmax):
        wi1=-wmax

    #Calculo velocidad Angular de llantas robot 2
    wd2= (V2/r)+((L*W2)/(2*r)) #Calulo de wd robot unicilo
    wi2= (V2/r)-((L*W2)/(2*r)) #Calulo de wi robot unicilo

    if(wd2>wmax):    #Normalizamos el valor de wd a wmax 
        wd2=wmax
    elif(wd2<-wmax):
        wd2=-wmax

    if(wi2>wmax):    #Normalizamos el valor de wi a wmax 
        wi2=wmax
    elif(wi2<-wmax):
        wi2=-wmax

    #Calculo velocidad Angular de llantas robot 3
    wd3= (V3/r)+((L*W3)/(2*r)) #Calulo de wd robot unicilo
    wi3= (V3/r)-((L*W3)/(2*r)) #Calulo de wi robot unicilo

    if(wd3>wmax):    #Normalizamos el valor de wd a wmax 
        wd3=wmax
    elif(wd3<-wmax):
        wd3=-wmax

    if(wi3>wmax):    #Normalizamos el valor de wi a wmax 
        wi3=wmax
    elif(wi3<-wmax):
        wi3=-wmax

    #Calculo velocidad Angular de llantas robot 4
    wd4= (V4/r)+((L*W4)/(2*r)) #Calulo de wd robot unicilo
    wi4= (V4/r)-((L*W4)/(2*r)) #Calulo de wi robot unicilo

    if(wd4>wmax):    #Normalizamos el valor de wd a wmax 
        wd4=wmax
    elif(wd4<-wmax):
        wd4=-wmax

    if(wi4>wmax):    #Normalizamos el valor de wi a wmax 
        wi4=wmax
    elif(wi4<-wmax):
        wi4=-wmax

    #Calculo velocidad Angular de llantas robot 5
    wd5= (V5/r)+((L*W5)/(2*r)) #Calulo de wd robot unicilo
    wi5= (V5/r)-((L*W5)/(2*r)) #Calulo de wi robot unicilo

    if(wd5>wmax):    #Normalizamos el valor de wd a wmax 
        wd5=wmax
    elif(wd5<-wmax):
        wd5=-wmax

    if(wi5>wmax):    #Normalizamos el valor de wi a wmax 
        wi5=wmax
    elif(wi5<-wmax):
        wi5=-wmax

    #Calculo velocidad Angular de llantas robot 6
    wd6= (V6/r)+((L*W6)/(2*r)) #Calulo de wd robot unicilo
    wi6= (V6/r)-((L*W6)/(2*r)) #Calulo de wi robot unicilo

    if(wd6>wmax):    #Normalizamos el valor de wd a wmax 
        wd6=wmax
    elif(wd6<-wmax):
        wd6=-wmax

    if(wi6>wmax):    #Normalizamos el valor de wi a wmax 
        wi6=wmax
    elif(wi6<-wmax):
        wi6=-wmax

    # Mostrar CALCULOS
    # print("V1="+str(V1)+"W1="+str(W1))  #Imprimir V y W
    # print("wd1="+str(wd1)+"wi1="+str(wi1)) #Imprimir wi y wd
    # print("V2="+str(V2)+"W2="+str(W2))  #Imprimir V y W
    # print("wd2="+str(wd2)+"wi2="+str(wi2)) #Imprimir wi y wd
    # print("V3="+str(V3)+"W3="+str(W3))  #Imprimir V y W
    # print("wd3="+str(wd3)+"wi3="+str(wi3)) #Imprimir wi y wd
    # print("V4="+str(V4)+"W4="+str(W4))  #Imprimir V y W
    # print("wd4="+str(wd4)+"wi4="+str(wi4)) #Imprimir wi y wd
    # print("V5="+str(V5)+"W5="+str(W5))  #Imprimir V y W
    # print("wd5="+str(wd5)+"wi5="+str(wi5)) #Imprimir wi y wd
    # print("V6="+str(V6)+"W6="+str(W6))  #Imprimir V y W
    # print("wd6="+str(wd6)+"wi6="+str(wi6)) #Imprimir wi y wd

    #Control bluetooth y camara
    Bt.move(robot_bt1,wd1,wi1)
    Bt.move(robot_bt2,wd2,wi2)
    Bt.move(robot_bt3,wd3,wi3)
    Bt.move(robot_bt4,wd4,wi4)
    Bt.move(robot_bt5,wd5,wi5)
    Bt.move(robot_bt6,wd6,wi6)
    time.sleep(0.2)
    
    #Detectamos Trigger's1
    RT, LT =control.read_Trigger()

    if(LT>0.5):
        #Detectamos tecla presionada en control 1 xbox
        #print(control.read_control1_abxy())
        a, b, x, y, rb =control.read_control1_abxy()
        if y==1:
            V1=8700
            W1=0
        elif a==1:
            V1=-8700
            W1=0
        elif b==1:
            V1=0
            W1=70
        elif x==1:
            V1=0
            W1=-70
        elif rb==1:
            V1=0
            W1=0
            break
        else:
            V1=0
            W1=0  

        #Detectamos tecla presionada en control 2 xbox
        #print(control.read_control2_joystick_right())
        y, x, rb =control.read_control2_joystick_right()
        x=x*10
        y=y*10
        if x>5:
            V2=8700
            W2=0
        elif x<-5:
            V2=-8700
            W2=0
        elif y>5:
            V2=0
            W2=70
        elif y<-5:
            V2=0
            W2=-70
        elif rb==1:
            V2=0
            W2=0
            break
        else:
            V2=0
            W2=0  

        #Detectamos tecla presionada en control 3 xbox
        #print(control.read_control3_PAD_Left())
        y, x, rb =control.read_control3_PAD_Left()
        x=x*-10
        y=y*10
        if x>5:
            V3=8700
            W3=0
        elif x<-5:
            V3=-8700
            W3=0
        elif y>5:
            V3=0
            W3=70
        elif y<-5:
            V3=0
            W3=-70
        elif rb==1:
            V3=0
            W3=0
            break
        else:
            V3=0
            W3=0  

        #Detectamos tecla presionada en control 4 xbox
        #print(control.read_control4_joystick_Left())
        y, x, rb =control.read_control4_joystick_Left()
        x=x*10
        y=y*10
        if x>5:
            V4=8700
            W4=0
        elif x<-5:
            V4=-8700
            W4=0
        elif y>5:
            V4=0
            W4=70
        elif y<-5:
            V4=0
            W4=-70
        elif rb==1:
            V4=0
            W4=0
            break
        else:
            V4=0
            W4=0  

    elif(RT>0.5):
        #Detectamos tecla presionada en control 1 xbox
        #print(control.read_control1_abxy())
        a, b, x, y, rb =control.read_control1_abxy()
        if y==1:
            V5=8700
            W5=0
        elif a==1:
            V5=-8700
            W5=0
        elif b==1:
            V5=0
            W5=70
        elif x==1:
            V5=0
            W5=-70
        elif rb==1:
            V5=0
            W5=0
            break
        else:
            V5=0
            W5=0  

        #Detectamos tecla presionada en control 2 xbox
        #print(control.read_control2_joystick_right())
        y, x, rb =control.read_control2_joystick_right()
        x=x*10
        y=y*10
        if x>5:
            V6=8700
            W6=0
        elif x<-5:
            V6=-8700
            W6=0
        elif y>5:
            V6=0
            W6=70
        elif y<-5:
            V6=0
            W6=-70
        elif rb==1:
            V6=0
            W6=0
            break
        else:
            V6=0
            W6=0    

    else:
        #Detectamos tecla presionada en control 1 xbox
        #print(control.read_control1_abxy())
        a, b, x, y, rb =control.read_control1_abxy()
        if y==1:
            V1=8700
            W1=0
            V2=8700
            W2=0
            V3=8700
            W3=0
            V4=8700
            W4=0
            V5=8700
            W5=0
            V6=8700
            W6=0

        elif a==1:
            V1=-8700
            W1=0
            V2=-8700
            W2=0
            V3=-8700
            W3=0
            V4=-8700
            W4=0
            V5=-8700
            W5=0
            V6=-8700
            W6=0


        elif b==1:
            V1=0
            W1=70
            V2=0
            W2=70
            V3=0
            W3=70
            V4=0
            W4=70
            V5=0
            W5=70
            V6=0
            W6=70


        elif x==1:
            V1=0
            W1=-70
            V2=0
            W2=-70
            V3=0
            W3=-70
            V4=0
            W4=-70
            V5=0
            W5=-70
            V6=0
            W6=-70


        elif rb==1:
            V1=0
            W1=0
            V2=0
            W2=0
            V3=0
            W3=0
            V4=0
            W4=0
            V5=0
            W5=0
            V6=0
            W6=0
            break
        
        else:
            V1=0
            W1=0
            V2=0
            W2=0
            V3=0
            W3=0
            V4=0
            W4=0
            V5=0
            W5=0
            V6=0
            W6=0

#FINALIZAR EL PROGRAMA
Bt.move(robot_bt1,0,0)   #Enviamos wd y wi en cero a robot bluetooth para detenerlo
Bt.move(robot_bt2,0,0)   #Enviamos wd y wi en cero a robot bluetooth para detenerlo
Bt.move(robot_bt3,0,0)   #Enviamos wd y wi en cero a robot bluetooth para detenerlo
Bt.move(robot_bt4,0,0)   #Enviamos wd y wi en cero a robot bluetooth para detenerlo
Bt.move(robot_bt5,0,0)   #Enviamos wd y wi en cero a robot bluetooth para detenerlo
Bt.move(robot_bt6,0,0)   #Enviamos wd y wi en cero a robot bluetooth para detenerlo

Bt.disconnect(robot_bt1) #Desconectamos Bluetooth
Bt.disconnect(robot_bt2) #Desconectamos Bluetooth
Bt.disconnect(robot_bt3) #Desconectamos Bluetooth
Bt.disconnect(robot_bt4) #Desconectamos Bluetooth
Bt.disconnect(robot_bt5) #Desconectamos Bluetooth
Bt.disconnect(robot_bt6) #Desconectamos Bluetooth