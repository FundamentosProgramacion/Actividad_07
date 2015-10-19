#encoding: UTF-8
#David Salvador Ruiz Roa
#Tarea 7
from Graphics import*
from math import*

def dibujarRectangulo(v):
    a = 190
    b = 210
    for n in range(20):
        r = Rectangle((a,a),(b,b))
        r.fill = None
        r.draw(v)
        a =+ a - 10
        b =+ b + 10
    
    
def dibujarCirculo(v):
    r = 10
    for n in range(20):
        c = Circle((200,200),(r))
        c.fill = None
        c.draw(v)
        r =+ r + 10
    main()
        
def dibujarEstrella(v):
    a = Arrow((200,200),0)
    a.forward(100)
    a.rotate(90)
    a.forward(50)
    a.rotate(270)
    a.penDown()
    for n in range(5):
        a.rotate(216)
        a.forward(200)
        a.draw(v)
    main()
        
def dibujarEspiral(v):
    l = Arrow((200,200),0)
    l.penDown()
    d = 5
    for n in range(77):
        l.forward(d)
        l.rotate(90)
        d =+ d + 5
        l.draw(v)
    main()
        
def dibujarCirculos(v):
    for n in range (0,360,30):
        c = Circle((200,200),70)
        c.fill = None
        c.rotate(n)
        c.forward(70)
        c.draw(v)
    main()
    
def calcularPi(divisor):
    signo = 1
    suma = 0
    for n in range (1,divisor,2):
        if divisor <101:
            if signo > 0:
                print(("+1/%i"%n),end = "")
            else:
                print(("-1/%i"%n),end = "")
        suma = suma + ((1/n)*signo)
        signo *= -1
    pi = suma*4
    return pi
                
def divisibles17():
    a = 0
    for n in range(999,9999):
        if (n % 17) == 0:
            a =+ a + 1
    print("El numero de numeros de 4 digitos divisibles entre 17 son: ",a)
    main()
    
def serie():
    n = 1
    a = 1
    c = 10
    for k in range(1,10) :
        print(a,"*",8,"+",k,"=",(a*8+k))
        n += c
        a += n
        c *= 10
    n = 1
    c = 10
    for k in range(9) :
        print(n,"*",n, "=",n*n)
        n += c
        c *= 10    
    main()

def main():
    opcion = int( input("1. Circulos y rectangulos\n2. Estrella\n3. Espiral\n4. 12 Circulos\n5. CalcularPi\n6. Divisibles entre 17\n7. Serie de numeros\n8. Salir"))
    v = Window("Tarea 07",400,400)
    if opcion == 1:
        dibujarRectangulo(v)
        dibujarCirculo(v)
    elif opcion == 2:
        dibujarEstrella(v)
    elif opcion == 3:
        dibujarEspiral(v)
    elif opcion == 4:
        dibujarCirculos(v)
    elif opcion == 5:
        v.close()
        divisor = int(input("Ingrese el divisor"))
        pi = calcularPi(divisor)
        print("\nEl valor de pi es:",pi)
        main()
    elif opcion == 6:
        v.close()
        divisibles17()
    elif opcion == 7:
        v.close()
        serie()
    elif opcion == 8:
        v.close()
    else:
        print("Error")
        v.close()
main()