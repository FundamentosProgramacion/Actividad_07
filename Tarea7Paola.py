#Encoding:UTF-8
#Paola Castillo Nacif
#Tarea 7

from Graphics import*
from math import*

def dibujarCirculoCuadrado(radio,lado):
    v=Window("A",400,400)
    x=200
    y=200
    for circulo in range(0,19):
        radio+=10
        if radio<=390:
            circulo=Circle((x,y),radio)
            circulo.draw(v)
            circulo.fill=None
    for cuadrado in range(0,20):
        lado+=10
        if lado<=390:
            x-=10
            y-=10
            cuadrado=Rectangle((x,y),(lado,lado))
            cuadrado.draw(v)
            cuadrado.fill=None
        
    
def dibujarEstrella(lado):
    color="blue"
    angulo=144
    v2=Window("B",400,400)
    estrella=Arrow((100,200),0)
    estrella.penDown()
    for k in range(5):
        estrella.draw(v2)
        estrella.fill=Color(color)
        estrella.forward(lado)
        estrella.rotate(angulo)
    return
    
def dibujarEspiral(l):
    v3=Window("C",400,400)
    for espiral in range(20):
        espiral=Arrow((200,200),0)
        espiral.draw(v3)
        espiral.penDown()
        for l in range(10,375,5):
            espiral.forward(l)
            espiral.rotate(90)
            
def dibujarFlor(a,n,an,an2):
    v4=Window("D",400,400)
    while an2<=360:
        rad=an2*pi/180
        an2+=an
        r=a*cos(n*rad)
        x=r*cos(rad)+100
        y=200-r*sin(rad)
        
        circulo=Circle((x,y),100)
        circulo.fill=None
        circulo.draw(v4)
        
def serieLeibniz(n):
    suma=0
    signo=1
    for k in range(1,1001,2):
        suma=suma+signo/k
        signo*=-1
    return suma*4
    
def numerosDivisores(contadorDivisores):
    for n in range (999,10000):
        if n%17==0:
            contadorDivisores+=1
    return contadorDivisores
    
def calcularOperaciones(acnum,conum,num):
    
    for k in range(1,10):
        print(acnum,"*",8,"+",k,"=",(acnum*8+k))
        num+=conum
        acnum+=num
        conum*=10
    print("\n")
    num=1
    conum=10
    for k in range(9):
        print(num,"*",num,"=",num*num)
        num+=conum
        conum*=10
                  
def main():
    opcion=int(input("1.Circulos y Cuadrados\n2.Estrella\n3.Espiral\n4.Flor\n5.Calcular Pi\n6.Divisores\n7.Operaciones\n8.Salir\nTeclea tu opcion"))
    if opcion==1:
        radio=0
        lado=200
        dibujarCirculoCuadrado(radio,lado)
    elif opcion==2:
        lado=200
        dibujarEstrella(lado)
    elif opcion==3:
        l=0
        dibujarEspiral(l)
    elif opcion==4:
        a=200
        n=1
        an=15
        an2=0
        dibujarFlor(a,n,an,an2)
    elif opcion==5:
        n=int(input("valor de n"))
        aprox=serieLeibniz(n)
        print("π=",aprox)
        print("\n")
    elif opcion==6:
        contadorDivisores=0
        nD=numerosDivisores(contadorDivisores)
        print("Hay",nD,"numeros de 4 digitos divisibles entre 17")
        print("\n")
    elif opcion==7:
        acnum=1
        conum=10
        num=1
        calcularOperaciones(acnum,conum,num)
    elif opcion==8:
        exit
    else:
        print("Opcion incorrecta, intenta nuevamente")
        opcion=int(input("1.Circulos y Cuadrados\n2.Estrella\n3.Espiral\n4.Flor\n5.Calcular Pi\n6.Divisores\n7.Operaciones\n8.Salir\nTeclea tu opcion"))
main()