#encoding:UTF-8
#Jorge Daniel Juárez Ruiz
#Uso de ciclo for para distintas funciones.  

from Graphics import*
from math import*

def calcularDivisores17():
    divisibles=0
    for x in range(1000,10000):
        if x%17==0:
            divisibles+=1
    print(divisibles)
   

def calcularPi():
    suma=0
    signo=1
    a=int(input("Lmite"))
    for k in range(1,a,2):
            fraccion=signo/k
            signo*=-1
            suma+=fraccion
    suma=4*suma
    print("PI=",suma)

def dibujarCirculosYCuadros():
    v=Window("Dibujos",400,400)
    for x in range(1,200,10):
        a=Rectangle((200-x,200-x),(200+x,200+x))
        a.fill=None
        a.draw(v)    
    for x in range(1,200,10):
        a=Circle((200,200),x)
        a.fill=None
        a.draw(v)    

def dibujarEstrella():
    v=Window("Estrella",400,400)
    tortuga=Arrow((100,250),0)
    tortuga.penDown()
    for x in range(5):
        tortuga.forward(200)
        tortuga.rotate(144)
        tortuga.draw(v)
        
def dibujarEspiral():
    v=Window("Estrella",400,400)
    tortuga=Arrow((200,200),0)
    tortuga.penDown()
    for x in range (7,400,5):
        tortuga.forward(x)
        tortuga.rotate(90)
        tortuga.draw(v)
        
def dibujarCirculos():
    v=Window("Circulos",400,400)
    a=(pi/6)
    
    for x in range(12):
        c=Circle((200+50*cos(a),200+50*sin(a)),50)
        c.fill=None
        c.draw(v)
        a+=(pi/6)
    
def imprimirOperaciones():
    y=1
    t=1
    for z in range (1,10):
        print("%i*8+%i=%i" %(y,z,(y*8+z)))
        y+=(10**z)+t
        t=(10**z)+t
    t=1
    for z in range(1,10):
        print("%i*%i=%i"%(t,t,t**2))
        t=(10**z)+t

    
def main():
    f=int(input("1.Circulos y cuadrados\n2.Estrella\n3.Espiral Cuadrada\n4.Circulos\n5.Calcular pi\n6.Números de cuatro digitos divisibles entre 17\n7.Operaciones\n8.Salir"))
    while f!=8:
        if f==1:
            dibujarCirculosYCuadros()
        if f==2:
            dibujarEstrella()
        if f==3:
            dibujarEspiral()
        if f==4:
            dibujarCirculos()
        if f==5:
            calcularPi()
        if f==6:
            calcularDivisores17()
        if f==7:
            imprimirOperaciones()
        f=int(input("1.Circulos y cuadrados\n2.Estrella\n3.Espiral Cuadrada\n4.Círculos\n5.Calcular pi\n6.Números de cuatro digitos divisibles entre 17\n7.Operaciones\n8.Salir"))
    
main()