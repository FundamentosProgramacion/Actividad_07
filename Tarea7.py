# encoding: UTF-8
# Autor: Humberto Serra Mendieta
# Tarea 7, "for"

from Graphics import*


def dibujarCuadrosCirculos(v,la,lb):
    
    
    for lb in range(lb,400,10):
         
        r=Rectangle((la,la),(lb,lb))
        r.setOutline(Color('Black'))
        r.fill=None
        r.draw(v)
        la=la-10
    
    
    for r in range(10,210,10):
     
        c=Circle((199,199),r) 
        c.setOutline(Color('Black'))
        c.fill=None   
        c.draw(v)
    
def dibujarEstrella(v):
    t=Arrow((100,250))
    t.pen.color=Color("blue")
    t.draw(v)
    t.penDown()
    
    for k in range(1,6):
        t.forward(200)
        t.rotate(144)
        
def dibujarLaberinto(v,d):
    t=Arrow((199,199))
    t.pen.color=Color("blue")
    t.draw(v)
    t.penDown()
    t.forward(10)
    t.rotate(90)
    t.forward(20)
    t.rotate(90)
    t.forward(20)
    t.rotate(90)
    for d in range(d,400,10):
        t.forward(d)
        t.rotate(90)
        t.forward(d)
        t.rotate(90)

def dibujarPatronCirculo(v):
    for n in range (0,360,30):
        c = Circle((199,199),50)
        c.fill = None
        c.rotate(n)
        c.forward(50)
        c.draw(v)
    
def calcularPi(n):
    suma=0
    signo=1
   
    for k in range(1,n+1,2):
        if n<=100:
            if signo>0:
                print(" + ",end="")
            else:
                print(" - ",end="")
            print(("1/%i"%k),end="")
        suma=suma+signo/k
        signo*=-1
    print("= \n" ,suma*4)    
             
def calcularDivisibles17():
    cd=0
    print("Numeros divisibles entre 17:")
   
    for n in range (1,10000):
        if n%17==0:
            print(n)
            cd+=1
    print("Total de numeros divisibles entre 17=",cd)

def calcularOperaciones():
    a=1
    b=1
    c=10
    for k in range(1,10) :
        print(b,"*8+",k,"=",(b*8+k))
        a += c
        b += a
        c *= 10
        
    print("")
    c=1
    n=0
    for k in range(1,10):
        n=n+c
        r=n*n
        print(n,"*",n,"=",r)                        
        c*=10
        
def main():
    opcion=0
    while opcion!=8:
        opcion=int(input("""1. Dibujar cuadros y circulos
2. Dibujar estrella
3. Dibujar laberinto
4. Dibujar patron de circulos
5. Calcular Pi
6. Numeros divisibles entre 17
7. Operaciones 
8. Salir
Teclee su opcion"""))
        if opcion==1:
            v=Window("for",400,400)
            dibujarCuadrosCirculos(v,189,209)
        elif opcion==2:
            v=Window("for",400,400)
            dibujarEstrella(v)
        elif opcion==3:
            v=Window("for",400,400)
            dibujarLaberinto(v,30)
        elif opcion==4:
            v=Window("for",400,400)
            dibujarPatronCirculo(v)
        elif opcion==5:
            n=int(input("Valor de n"))
            calcularPi(n)
        elif opcion==6:
            calcularDivisibles17()
        elif opcion==7:
            calcularOperaciones()
     
          
main()