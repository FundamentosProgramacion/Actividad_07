#encoding: UTF-8
#Autor: Hector Manuel Takami Flores
#Actividad 7
from Graphics import*
from math import*

def dibujaCuadrosYCirculos():
    v=Window("                                                      A   ",400,400)
    for k in range(0,200,10):
        circulo=Circle((200,200),k)
        circulo.fill=None
        circulo.draw(v)
        rectangulo=Rectangle((190-k,190-k),(210+k,210+k))
        rectangulo.fill=None
        rectangulo.draw(v)
        
def dibujaEstrella():
    v=Window("                                                      B   ",400,400)
    flecha=Arrow((100,200),0)
    flecha.draw(v)
    flecha.penDown()
    for k in range(5):
        flecha.forward(200)
        flecha.rotate(144)
        
def dibujaCuadradoEspiral():
    v=Window("                                                      C   ",400,400)
    flecha=Arrow((200,200),0)
    flecha.draw(v)
    flecha.penDown()
    for k in range(0,365,5):
        flecha.forward(10+k)
        flecha.rotate(90)
        
def dibujaCirculoDeCirculos():
    v=Window("                                                      D   ",400,400)
    a=(pi/6)
    for k in range(12):
        circulo=Circle((200+50*cos(a),200+50*sin(a)),50)
        circulo.fill=None 
        circulo.draw(v)
        a += (pi/6)
        
def calculaPI(n):
    sumaParcial=1
    signo=1
    for k in range(3,n,2):
        signo *= -1
        sumaParcial=sumaParcial+(signo/k)
    print("\nPi=",(sumaParcial*4))
                 
def calculaNumerosDivisibles(n):
    a=0
    for k in range(1000,10000,1):
        if k%n ==0:
            a += 1
        else:
            a += 0
    print("Numeros de 4 cifras divisibles entre 17: %i"%(a))
    
def calculaOperaciones():
    m=1
    a=1
    for k in range(1,10,1):
        print("%i*8+%i=%i" % (m,k,(m*8+k)))
        print(end="")
        m += (10**k)+a
        a = (10**k)+a
   
    b=1    
    for q in range(1,10,1):
        print("%i*%i=%i" % (b,b,(b**2)))
        b=(10**q)+b
    
   
def main():
    opcion=int(input("1.Graficos\n2.Calcula aproximacion de PI\n3.Calcula numeros de 4 cifras divisibles entre 17\n4.Cadenas de operaciones\n5.Salir"))
    while opcion!=5:
            if opcion==1:
                opcionGrafica=int(input("1.Cuadrados y circulos\n2.Estrella\n3.Cuadrado espiral\n4.Circulo de circulos\n5.Cambiar de funcion\n6.Salir"))
                if opcionGrafica==1:
                    dibujaCuadrosYCirculos()
                    opcionGrafica=int(input("1.Cuadrados y circulos\n2.Estrella\n3.Cuadrado espiral\n4.Circulo de circulos\n5.Cambiar de funcion\n6.Salir"))
                elif opcionGrafica==2:
                    dibujaEstrella()
                    opcionGrafica=int(input("1.Cuadrados y circulos\n2.Estrella\n3.Cuadrado espiral\n4.Circulo de circulos\n5.Cambiar de funcion\n6.Salir"))
                elif opcionGrafica==3:
                    dibujaCuadradoEspiral()
                    opcionGrafica=int(input("1.Cuadrados y circulos\n2.Estrella\n3.Cuadrado espiral\n4.Circulo de circulos\n5.Cambiar de funcion\n6.Salir"))
                elif opcionGrafica==4:
                    dibujaCirculoDeCirculos()
                    opcionGrafica=int(input("1.Cuadrados y circulos\n2.Estrella\n3.Cuadrado espiral\n4.Circulo de circulos\n5.Cambiar de funcion\n6.Salir"))
                elif opcionGrafica==5:
                    opcion=int(input("1.Graficos\n2.Calcula aproximacion de PI\n3.Calcula numeros de 4 cifras divisibles entre 17\n4.Cadenas de operaciones\n5.Salir"))
                elif opcionGrafica==6:
                    opcion=5
                elif opcionGrafica>6:
                    print("Error intente nuevamente")
                    opcionGrafica=int(input("1.Cuadrados y circulos\n2.Estrella\n3.Cuadrado espiral\n4.Circulo de circulos\n5.Cambiar de funcion\n6.Salir"))
                else:
                    print("")
            elif opcion==2:
                calculaPI(200)
                opcion=int(input("1.Graficos\n2.Calcula aproximacion de PI\n3.Calcula numeros de 4 cifras divisibles entre 17\n4.Cadenas de operaciones\n5.Salir"))
            elif opcion==3:
                calculaNumerosDivisibles(17)
                opcion=int(input("1.Graficos\n2.Calcula aproximacion de PI\n3.Calcula numeros de 4 cifras divisibles entre 17\n4.Cadenas de operaciones\n5.Salir"))
            elif opcion==4:
                calculaOperaciones()
                opcion=int(input("1.Graficos\n2.Calcula aproximacion de PI\n3.Calcula numeros de 4 cifras divisibles entre 17\n4.Cadenas de operaciones\n5.Salir"))
            elif opcion>5:
                print("Error intente nuevamente")
                opcion=int(input("1.Graficos\n2.Calcula aproximacion de PI\n3.Calcula numeros de 4 cifras divisibles entre 17\n4.Cadenas de operaciones\n5.Salir"))
            else:
                print("")
main()