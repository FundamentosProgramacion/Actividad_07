#encoding: UTF-8
#Autor: Astrid M. Villegas Berdejo
#Rosa de n petalos

from math import *
from Graphics import *

def main ():
    opcion = int( input("Teclea la opción que deseas\n1.Dibujar Circulo y rectángulo\n2.Dibujar estrella\n3.Dibujar espiral\n4.Dibujar flor\n5.Calcular PI\n6.Divisores\n7.Hacer operaciones\n8.Salir"))
    if opcion == 1:
        radio = 0
        lado = 200
        dibujarRyC (radio, lado)
        
    elif opcion == 2:
        lado = 200
        dibujarEstrella (lado)
    
    elif opcion == 3:
        lado = 0
        dibujarEspiral (lado)
        
    elif opcion == 4:
        a = 200
        n = 1
        alfa = 0.1
        otroAlfa = 0
        dibujarFlor (a, n, alfa, otroAlfa)
        
    elif opcion ==5:
        #suma = 0
        #signo = 1
        p = aproximarPI ()
        print ("PI = " , p)
        
    elif opcion == 6:
        cDivisor = 0
        d = dividir (cDivisor)
        print ("Hay %i numeros de cuatro digitos divisibles entre 17" % d)
        
    elif opcion ==7:
        an = 1
        cn = 10
        n = 1
        calcularOperaciones (an, cn, n)
        
    elif opcion == 8:
        print (" ")
        
    else:
        opcion = int( input("Opción incorrecta, selecciona de nuevo:\n1.Dibujar Círculo y rectángulo\n2.Dibujar estrella\n3.Dibujar espiral\n4.Dibujar flor\n5.Calcular PI\n6.Divisores\n7.Hacer operaciones\n8.Salir"))
    
    
def dibujarRyC (r, lado):
    v = Window ("A", 400,400)
    x = 200
    y = 200
    for circulo in range (0, 19):
        r = r + 10
        if r <= 390:
            circulo = Circle ((x,y), r)
            circulo.draw (v)
            circulo.fill = None
    for rectangulo in range (0, 20):
        lado = lado + 10
        if lado <= 390:
            x = x-10
            y = y-10
            rectangulo = Rectangle ((x, y),(lado, lado))
            rectangulo.draw (v)
            rectangulo.fill = None
            
            #x = x-10
            #y = y-10
            
def dibujarEspiral (lado):
    v = Window ("C",400, 400)
    #for k in range (20):
    espiral = Arrow ((200,200),0)
        #espiral.penDown ()
        #espiral.draw (v)
    for l in range (10, 375, 5):
        espiral.penDown ()
        espiral.draw (v)
        espiral.forward (l)
        espiral.rotate (90)        

def dibujarEstrella (lado):
    #angulo = 144
    v = Window ("B", 400, 400)
    angulo = 144
    estrella = Arrow ((100, 200),0)
    estrella.penDown ()
    for k in range (5):
        estrella.draw (v)
        estrella.pen.color = Color("blue") 
        estrella.forward (lado)
        estrella.rotate (angulo)
        
    #return

def dibujarFlor (a, n, alfa, otroAlfa):
    v = Window ("D", 400, 400)
    
    for a in range (0,361,30):
        radianes = a * pi/180
        a = a+alfa
        #r = a * cos(radianes)
        #x = r * cos (radianes) + 200
        #y = 200 - r * sin (radianes)
        x = 200 + 50 * cos(radianes)
        y = 200 + 50 * sin(radianes)
        circulo = Circle ((x,y), 50)
        circulo.draw (v)
        circulo.fill = None
        
def aproximarPI ():
    suma = 0
    signo = 1
    ultimo = 100000
    for k in range (1, ultimo, 2):
        suma = suma + signo/k
        signo = signo*-1
    return suma*4
    
def dividir (cDivisor):
    for n in range (999, 10000):
        if n%17 == 0:
            cDivisor = cDivisor +1
            
    return cDivisor
    
def calcularOperaciones (an, cn, n):
    for k in range (1,10):
        rOperacion = an*8+k
        print ("%i x 8 + %i = %i" %(an, k, rOperacion))#(an, "x", 8, "+", k, "=", rOperacion)
        
        n = n+cn
        an = an+n
        cn = cn*10
    print ("\n")
    n = 1
    cn = 10
    for k in range (9):
        r = n*n
        print (n, "x", n, "=", r)       
        n = n+cn
        cn = cn*10
        
        
main ()