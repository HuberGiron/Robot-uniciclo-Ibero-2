import bluetooth #pip install pybluez2
import time  #default
import numpy   #pip install numpy

def scan():
    print("\n Scnng Bluetooth devices")
    devices = bluetooth.discover_devices(lookup_names= True, lookup_class= True)
    number_of_devices = len(devices)
    print(number_of_devices, " devices found")

    for addr, name, devices_class in devices:
        #if(name == "HC-05"):
        print("\n Device: ")
        print("Device Name: %s " % (name))
        print("Device MAC address: %s " % (addr))
        print("\n")
        print("Device Class: %s " % (devices_class))
        print("\n")

    return
 
def connect (bd_addr):
    port = 1
    sock=bluetooth.BluetoothSocket()
    sock.settimeout(20)
    while(True):
        try:
            sock.connect((bd_addr, port))
            break
        except:
            print("Error en conexion....reintentando")
        time.sleep(1)

    return sock

def move(sock,wr,wl):
    #Información para el robot
    sock.send('H'.encode())
    sock.send(numpy.int16(wr))
    sock.send(numpy.int16(wl))

def move_demo(sock):
    #Información para el robot
    sock.send('H'.encode())
    sock.send(numpy.int16(100))
    sock.send(numpy.int16(100))
    time.sleep(3)
    sock.send('H'.encode())
    sock.send(numpy.int16(0))
    sock.send(numpy.int16(0))
    time.sleep(3)
    sock.send('H'.encode())
    sock.send(numpy.int16(-100))
    sock.send(numpy.int16(-100))
    time.sleep(3)
    sock.send('H'.encode())
    sock.send(numpy.int16(0))
    sock.send(numpy.int16(0))
    time.sleep(3)

def disconnect(sock):
    sock.close()

#EJEMPLO
#scan()
#robot1=connect("98:D3:71:F6:63:9C")
#move(robot1,100,100)
#disconnect(robot1)