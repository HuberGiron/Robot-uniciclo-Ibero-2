import cv2 #pip install opencv-python, opencv-contrib-python
import numpy as np #pip install numpy
import math #default pip install python-math

#pip opencv-contrib-python: descarga libreria cv2, aruco, y si es necesario, numpy

#modifica imagen, le reduce el brillo
def change_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

    return img

#funcion que consigue punto medio del eje x y y
def mid_points(matrix, pt1, pt2):
  matrix[0][0] = (pt1[0] + pt2[0]) / 2
  matrix[0][1] = (pt1[1] + pt2[1]) / 2
  return matrix

#conseguir el angulo de rotacion de los codigos aruco
def get_angle(bottomRight, bottomLeft):
    x = (bottomRight[0] - bottomLeft[0])
    y = (bottomRight[1] - bottomLeft[1])
    angle = math.atan2(y, x)
    angle = math.degrees(angle)
    angle *= -1

    if angle < 0:
      angle += 360
    angle = round(angle, 2)
    angle = abs(angle)
    return angle

#consigue angulo de rotacion de los codigos aruco en radianes
def get_anglerad(bottomRight, bottomLeft):
    x = (bottomRight[0] - bottomLeft[0])
    y = (bottomRight[1] - bottomLeft[1])
    angle = math.atan2(y, x)
    """ angle = math.degrees(angle)
    angle *= -1

    if angle < 0:
      angle += 360

    angle = abs(angle)
    angle = math.radians(angle) """
    angle = round(angle, 2)
    return angle


#funcion que dibuja e imprime informacion en el frame de opencv
def draw_aruco(frame, topLeft, topRight, bottomLeft, bottomRight, MidP, X, Y,angle,markerID,resolucionx,resoluciony):
       
  #Se dibuja el cuadrado 
  cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
  cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
  cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
  cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)

  #Se dibujan las lineas 
  line_thickness = 3
  cv2.line(frame, X[0], MidP[0], (0, 0, 255), thickness = line_thickness )
  cv2.line(frame, Y[0], MidP[0], (255, 0, 0), thickness = line_thickness )

  #Se imprime la información del texto 
  cv2.putText(frame, "["+str(MidP[0][0]-(resolucionx/2))+" ,"+str(MidP[0][1]-(resoluciony/2))+"]", (MidP[0][0], MidP[0][1] - 150),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,204,204),2,cv2.LINE_AA )
  cv2.putText(frame, str(f'ID: {markerID}'), (MidP[0][0] - 50, MidP[0][1] - 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 204, 204), 2, cv2.LINE_AA )
  #cv2.putText(frame, str(angle) + " grados", (MidP[0][0] - 400, MidP[0][1] - 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 204, 204), 2, cv2.LINE_AA )

#funcion que dibuja e imprime informacion en el frame de opencv
def draw_texto_titulo(frame,text,color):
  #Se imprime la información del texto 
  cv2.putText(frame,text,(20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

def draw_punto(frame,text,color, posx, posy, resolucionx,resoluciony):
  #Se imprime la información del texto 
  cv2.putText(frame,text,(posx+20,posy+20), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
  cv2.putText(frame,str(posx-resolucionx/2)+","+str(posy-(resoluciony/2)),(posx+20,posy+50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
  cv2.circle(frame,(posx,posy),10,color,5)

#conseguimos las coordenadas del aruco y lo guadamos como pares (x y y) en variables por seccion diferente
def get_coordenates(markerCorner):
  # extract the marker corners (which are always returned in
	# top-left, top-right, bottom-right, and bottom-left order)
  corners = markerCorner.reshape((4, 2))
  (topLeft, topRight, bottomRight, bottomLeft) = corners
  
  # convert each of the (x, y)-coordinate pairs to integers
  topRight = (int(topRight[0]), int(topRight[1]))
  bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
  bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
  topLeft = (int(topLeft[0]), int(topLeft[1]))

  return topLeft, topRight, bottomLeft, bottomRight

#almacenamos info de coordenadas y angulo del aruco, y la almacenamos en un diccionario
def get_ArucoInfo(markerCorner, markerID):

    topLeft, topRight, bottomLeft, bottomRight = get_coordenates(markerCorner)
 
    #Calculamos el angulo de inclinación 
    angle = get_anglerad(bottomRight, bottomLeft)

    info = {"coordenadas": [topLeft, topRight, bottomLeft, bottomRight], "angulo": (angle), "ID": (markerID)}

    return info

def initialize(camara, resolutionx, resolutiony):

  capture = cv2.VideoCapture(camara, cv2.CAP_DSHOW)
  capture.set(3, resolutionx)
  capture.set(4, resolutiony)
  #capture.set(cv2.CAP_PROP_SETTINGS, 1)
  capture.set(cv2.CAP_PROP_AUTOFOCUS, 0) # turn the autofocus off

  return capture

def buscar_Aruco(camara, resolucionx,resoluciony):

  ret, frame = camara.read()
  frame = cv2.resize(frame, (resolucionx, resoluciony)) #Cambiar el tamaño de la ventana que despliega
  frame = change_brightness(frame, 10)

  gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
  arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_50)
  arucoParams = cv2.aruco.DetectorParameters()
  detector = cv2.aruco.ArucoDetector(arucoDict, arucoParams) ########
  points, ids, rejected = detector.detectMarkers(gray)

  return frame, points, ids

def dibujar_aruco(frame, points, ids, resolucionx,resoluciony):

  MidP = np.arange(2).reshape(1,2)
  Y = np.arange(2).reshape(1,2)
  X = np.arange(2).reshape(1,2)
  #window_name = 'Camara detector qr' #Nombre de la ventana

  if len(points) > 0:
      # flatten the ArUco IDs list
      ids = ids.flatten()
      # loop over the detected ArUCo corners
      for (markerCorner, markerID) in zip(points, ids):

          topLeft, topRight, bottomLeft, bottomRight = get_coordenates(markerCorner)

          #Obtenemos coordenadas para punto medio y lineas
          mid_points(MidP, topRight, bottomLeft)
          mid_points(Y, topRight, bottomRight)
          mid_points(X, bottomLeft, bottomRight)
          
          #Calculamos el angulo de inclinación 
          angle = get_anglerad(bottomRight, bottomLeft)

          draw_aruco(frame, topLeft, topRight, bottomLeft, bottomRight, MidP, X, Y, angle, markerID, resolucionx,resoluciony)
      

  #cv2.imshow(window_name, frame) #Despliega la ventana 

def buscar_robots( points, ids, robot):

  MidP = np.arange(2).reshape(1,2)

  if len(points) > 0:
      # flatten the ArUco IDs list
      ids = ids.flatten()
      # loop over the detected ArUCo corners
      for (markerCorner, markerID) in zip(points, ids):

          topLeft, topRight, bottomLeft, bottomRight = get_coordenates(markerCorner)

          #Obtenemos coordenadas para punto medio
          mid_points(MidP, topRight, bottomLeft)
          robot[markerID][0]=MidP[0][0]
          robot[markerID][1]=MidP[0][1]
          robot[markerID][2]=get_anglerad(bottomRight, bottomLeft)

  return robot

def preview(camara, resolucionx, resoluciony):

  ret, frame = camara.read()
  frame = cv2.resize(frame, (resolucionx, resoluciony)) #Cambiar el tamaño de la ventana que despliega
  frame = change_brightness(frame, 10)
  window_name = 'Camara detector qr' #Nombre de la ventana
  cv2.imshow(window_name, frame) #Despliega la ventana 


##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##CODIGO EJEMPLO##
#si es True, se visualizara la camara y su interfaz, si es falsa ejecutará la camara sin mostrar nada
visual=True

if __name__=="__main__":

  capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
  qrCodeDetector = cv2.aruco

  window_name = 'Camara detector qr' #Nombre de la ventana
  #resolucion HD
  capture.set(3, 1280)
  capture.set(4, 720)
  
  points = np.arange(8).reshape(4,2)
  MidP = np.arange(2).reshape(1,2)
  Y = np.arange(2).reshape(1,2)
  X = np.arange(2).reshape(1,2)

  while (True):
    ret, frame = capture.read()
    if ret == False:
      break  #Por si acaso no detecta nada

    frame = cv2.resize(frame, (1280, 720)) #Cambiar el tamaño de la ventana que despliega
    frame = change_brightness(frame, 10)
    gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
    arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_50)
    arucoParams = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(arucoDict, arucoParams) ########
    points, ids, rejected = detector.detectMarkers(gray)
    
    if len(points) > 0:
      # flatten the ArUco IDs list
      ids = ids.flatten()
      # loop over the detected ArUCo corners
      for (markerCorner, markerID) in zip(points, ids):

          topLeft, topRight, bottomLeft, bottomRight = get_coordenates(markerCorner)

          #Obtenemos coordenadas para punto medio y lineas
          mid_points(MidP, topRight, bottomLeft)
          mid_points(Y, topRight, bottomRight)
          mid_points(X, bottomLeft, bottomRight)
          
          #Calculamos el angulo de inclinación 
          angle = get_angle(bottomRight, bottomLeft)

          if visual==True:
            draw_aruco(frame, topLeft, topRight, bottomLeft, bottomRight, MidP, X, Y, angle, markerID)
  
    if visual ==True:
      cv2.imshow(window_name, frame) #Despliega la ventana 

      if cv2.waitKey(1) & 0xFF == 27: #Presiona esc para salir 
        break
  
  capture.release()
  cv2.destroyAllWindows()
