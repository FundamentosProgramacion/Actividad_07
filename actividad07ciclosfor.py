#Encoding:utf-8
#Autor:Manuel Eduardo Zavala Gómez
#Actividad 7

from Graphics import*


def crearCuadradosyCirculos():
    v=Window("Circulos y Cuadrados",400,400)
    for x in range(10,200,15):
        cuadrado=Rectangle(((200-x),(200-x)),((x+200),(x+200)))
        cuadrado.fill=Color(0,0,0,0)
        cuadrado.draw(v)
        
        circulo= Circle((200,200),x)
        circulo.fill = Color(0,0,0,0)
        circulo.draw(v)
        
def crearEstrella():
    v= Window("Estrella",400,400)
    t=Arrow( (20,200), 0 )
    t.fill=Color("blue")
    t.draw(v)
    t.penDown()
    for n in range (5):
        t.forward(300)
        t.rotate(144)

def crearEspiral():
    v= Window("Espiral",400,400)
    t=Arrow( (200,200), 0 )
    t.draw(v)
    t.penDown()
    for e in range(5,370,5):
        t.forward(e)
        t.rotate(90)
                
def crearCirculo():
    v=Window("Circulo",400,400)
    t= Arrow((200,200),0)
    t.draw(v)
    t.penDown()
    for f in range (12):    
        for c in range (360):
            t.forward(1)
            t.rotate(1)   
        t.rotate(30)
        
#def calcularAprox():
    
        
      
def calcularDivision17():
    division=0
    for a in range (100,1000):
        if a%17==0:
            division=division+1
    print(division)
    
def calcularSumayMultip():
    d=0
    f=0
    for b in range(1,10):
        d=d+10**(b-1)
        f=f+d
        s=f*8+b
        print(f,"* 8 +",b,"=",s)
        
    print("Suma 2")
    k=0
    for o in range(1,10):
        k=k+10**(o-1)
        res=k*k
        print(k,"*",k,"=",res)
        
def main():
   
    opcion=1
    while opcion!=0:
        opcion=int(input("Escribe tu Opcion(salir 0):\n1)Dibujar cuadrados y circulos\n2)Dibujar estrella\n3)Dibujar espiral\n4)Dibujar circulos\n5)Aproximación de Pi\n6)Divisibles entre 17\n7)Sumas y multiplicacion"))
   
        if opcion==1:
            crearCuadradosyCirculos()
        elif opcion==2:
            crearEstrella()
        elif opcion==3:
            crearEspiral()
        elif opcion==4:
            crearCirculo()
        elif opcion==5:
            calcularAprox()
        elif opcion==6:
            calcularDivision17()
        elif opcion==7:
            calcularSumayMultip()
        else:
            print("Error")
     
main()
