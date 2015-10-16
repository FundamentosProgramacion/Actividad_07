#Encoding: UTF-8
#Autor: Pablo Alejandro Sanchez Tadeo, A01377515
#Ciclos for

from Graphics import *

#funcion para crear el circulo y el rectangulo
def dibujarCirculoYRectangulo(v) :
    for x in range (10,200,10) :
        circulo = Circle((200,200),x)
        circulo.draw(v)
        circulo.fill = None
        
    x1 = 200
    x2 = 200
    y1 = 200
    y2 = 200
    for y in range (20) :
        rec = Rectangle( (x1,y1),(x2,y2) )
        rec.draw(v)
        x1 -= 10
        y1 -= 10
        x2 += 10
        y2 += 10
        rec.fill = None

#Funcion para dibujar la estrella
def dibujarEstrella(v) :
    tort = Arrow( (100,200),0 )
    tort.draw(v)
    tort.penDown()
    for x in range(5) :
        tort.forward(200)
        tort.rotate(144)
    
#Funcion para dibujar el espiral
def dibujarEspiral(v) :   
   tortuga =  Arrow((200,200),0)
   tortuga.draw(v)
   tortuga.penDown()
   i = 10
   for x in range (0,73) :
       tortuga.forward(i)
       tortuga.rotate(90)
       i = i +5  

#Funcion para dibujar circulos
def dibujarCirculos(v) :
    circle = Circle((250,200),50)
    circle.fill = None
    for angulo in range (0,360,30) :
        circle = Circle((200,200),50)
        circle.fill = None
        circle.rotate(angulo)
        circle.forward(50)
        circle.draw(v)
    
#funcion para aproximar PI
def aprixomarPi(d) :
    suma = 0
    signo = 1
    for x in range (1,d,2):
        if d <= 100 :
            if signo > 0 :
                print((" + 1/%i"%x), end = " " ) 
            else :
                print((" - 1/%i"%x),  end = " " ) 
        suma = suma +    ((1/x)*signo)
        signo *= -1
        
    print("\n Pi = ",suma*4)    
    
#funcion para calcular cuantos numeros de 4 cifras son divisibles entre 17
def esDivisible() :
    contador = 0
    for numero in range (999,9999) :
        if numero % 17 == 0 :
            contador += 1
    print("Hay ",contador," numeros de 4 digitos divisibles entre 17")
    
#funcion que realiza una serie de numeros
def serieDeNumeros() :
    acumulador = 1
    numero = 1
    contador = 10
    for x in range(1,10) :
        #print(n)
        print(acumulador," * ",8," + ",x," = ",(acumulador * 8 + x))
        numero += contador
        acumulador += numero
        contador *= 10
        
    print("\n")
    numero = 1
    contador = 10
    for x in range(9) :
        print(numero,"*",numero, " = ",numero*numero)
        numero += contador
        contador *= 10
    
#funcion principal
def main() :
    v = Window("Ventana",400,400)
    opcion = int( input("1. Circulo y rectangulo\n2. Estrella\n3. Espiral\n4.Circulos\n5. Limpiar pantalla\n6. Aproximacion de Pi\n7. Numeros divisibles entre 17\n8. Serie de numeros\n9. Salir"))
    while opcion != 9 :
        if opcion == 1 :
            dibujarCirculoYRectangulo(v) #funcion
            print("Circulo y rectangulo")
        elif opcion == 2 :
            dibujarEstrella(v) #funcion
            print("Estrella")
        elif opcion == 3:
            print("Espiral")
            dibujarEspiral(v) #funcion
        elif opcion == 4 :
            print("Circulos")
            dibujarCirculos(v) #funcion
        elif opcion == 5 :
            v = Window("Ventana",400,400)
        elif opcion == 6 :
            print("Aproximacion de pi")
            divisor = int( input("Ingresa el valor de n, mientras mas grande, mas cerca de Pi estara"))
            aprixomarPi(divisor) #funcion
        elif opcion == 7 :
            print("Numeros divisibles entre 17")
            esDivisible() #funcion
        elif opcion == 8 :
            print("Serie de numeros")
            serieDeNumeros() #funcion      
        else :
            print("Opcion no valida")
        opcion = int( input("1. Circulo y rectangulo\n2. Estrella\n3. Espiral\n4.Circulos\n5. Limpiar pantalla\n6. Aproximacion de Pi\n7. Numeros divisibles entre 17\n8. Serie de numeros\n9. Salir"))
main()