from random import randint
import sys
import time

from Tools.scripts.treesync import raw_input


def sendGPIO(num):
     if (num == ROJO):
            print("1-ROJO")
            #ON RED LED
     if (num == VERDE):
            print("2-VERDE")
             #ON GREEN LED
     if (num == AZUL):
            print("3-AZUL")
            #ON BLUE LED
     if (num == AMARILLO):
            print("4-AMARILLO")
            #ON YELLOW LED
     time.sleep(1)

def terminate():
    sys.exit()

def initializeArray(numInicial):
    array = []
    for i in range(numInicial):
       array.append(0)
    return array

def getNumInputUser(str):
    try:
        numInit=int(raw_input(str))
        return numInit
    except ValueError:
        print ("No es un numero")

def showColors(array):
     for i in array:
          sendGPIO(i)

print("Start")
ROJO = 1
VERDE = 2
AZUL = 3
AMARILLO = 4
print("Comienzo Juego")
numInicial =  getNumInputUser('Seleccione numero de iteraciones inicial:')
listMachine = initializeArray(numInicial)
for i in range(numInicial):
    # Se obtiene numero random
    numRandom = (randint(1,4))
    listMachine[i] =numRandom
while True:
    showColors(listMachine)
    for i in listMachine:
        colorSeleccionado= getNumInputUser('Seleccione color:')
        sendGPIO(colorSeleccionado)
        if colorSeleccionado == i:
             print("CORRECTO")
        else:
             print("ERROR!")
             print("CERRANDO SESION")
             time.sleep(4)
             terminate()
    count = len(listMachine)
    listMachine.append(randint(1,4))
    print("CONTINUA EL JUEGO")




