#encoding: UTF-8
#Autor: Sergio Hernandez
#Descripcion: Actividad 07 - Funciones graficas y menu

from Graphics import *
from math import pi, cos, sin

def cuadrosYCirculos ():
    a = Window ("A", 400, 400)
    for circulos in range (20):
        circulo = Circle ((200,200), circulos*10)
        circulo.fill = None
        circulo.draw(a)
    for cuadros in range (1,20):
        cuadro = Rectangle ( (10*cuadros,10*cuadros) , (400-10*cuadros,400-10*cuadros) )
        cuadro.fill = None
        cuadro.draw(a)
    print ("Se han dibujado cuadros y círculos en la ventana A")
    
def estrella ():
    b = Window ("B", 400, 400)
    tortuga = Arrow ( (100,200), 0)
    tortuga.draw (b)
    tortuga.penDown()
    for estrella in range (5):
        tortuga.forward (200)
        tortuga.rotate (144)
    print ("Se ha dibujado una estrella de cinco picos en la ventana B")

def laberinto():
    c = Window ("C", 400, 400)
    tortuga = Arrow ( (200,200), 0)
    tortuga.draw (c)
    tortuga.penDown()
    tortuga.forward (10)
    tortuga.rotate (90)
    for laberinto in range (20, 370+1, 10):
        tortuga.forward (laberinto)
        tortuga.rotate (90)
        tortuga.forward (laberinto)
        tortuga.rotate (90)
    print ("Se ha dibujado un laberinto en la ventana C")

def circulos():
    d = Window ("D", 400, 400)
    for angulos in range (0,360+1,30):
        x = 50 * cos (angulos * pi / 180)
        y = 50 * sin (angulos * pi / 180)
        circulo = Circle ((200+x,200+y), 50)
        circulo.fill = None
        circulo.draw(d)
    print ("Se han dibujado circulos en la ventana D")

def calcularPi (n):
    print ("pi(%i) = 4 (" % n, end = "")
    pi = 0
    signo = 1
    for i in range (1,n+1,2):
        pi += (signo*(1/i))
        if (n <=100):
                if (signo == 1):
                        print (("+ 1/%i") % i, end= " ")
                else:
                        print (("- 1/%i") % i, end= " ")
        signo *= -1
    pi*=4
    print (") = %.12f" % pi)

def divisibles17 ():
    divisibles = 0
    for x in range (1000, 10000):
        if (x%17==0):
            divisibles+=1
    return divisibles
    

def piramide ():
    acumulador = 0
    resultado = 0
    for i in range (1, 10):
        acumulador = acumulador * 10 + i
        resultado = resultado * 10 + (10-i)
        print ("%i * 8 + %i = %i" % (acumulador, acumulador, resultado ) )
    print ("")    
    acumulador = 0
    for i in range (1, 10):
        acumulador = acumulador*10+1
        print ("%i * %i = %i" % (acumulador, acumulador, acumulador**2 ) )
        
               
def main():
    opcion = int (input ("Elige que opcion quieres: \n1. Dibujar cuadros y circulos \n2. Dibujar una estrella \n3. Dibujar un laberinto \n4. Dibujar circulos \n5. Aproximar Pi \n6. Numeros de cuatro digitos divisibles entre 17\n7. Operaciones en piramide \n0. Salir"))
    while (opcion != 0):
        if (opcion == 1):
            cuadrosYCirculos ()
        elif (opcion == 2):
            estrella()
        elif (opcion == 3):
            laberinto()
        elif (opcion == 4):
            circulos()
        elif (opcion == 5):
            n = int (input ("Dame n, el limite de la aproximacion"))
            calcularPi(n)
        elif (opcion == 6):
            divisibles = divisibles17()
            print ("Existen %i numeros de cuatro digitos que son divisibles entre 17" % divisibles)
        elif (opcion == 7):
            piramide()
        else:
            print ("Opcion invalida. Intenta de nuevo.")
        
        opcion = int (input ("Elige que opcion quieres: \n1. Dibujar cuadros y circulos \n2. Dibujar una estrella \n3. Dibujar un laberinto \n4. Dibujar circulos \n5. Aproximar Pi \n6. Numeros de cuatro digitos divisibles entre 17\n7. Operaciones en piramide \n0. Salir"))
        
    
main()
    