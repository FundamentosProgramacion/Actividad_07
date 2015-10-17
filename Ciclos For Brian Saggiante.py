#encoding: UTF-8
#Autor: Brian Saggiante A01377511
#Ciclos for geometría,valores numericos, obtencion de Pi y numeros divisibles de 17

from Graphics import*

def circulosRectangulos(v):
    for x in range (10,200,10):
        cir=Circle((200,200),x)
        cir.draw(v)
        cir.fill=None
        x1=200
        x2=200
        y1=200
        y2=200
    for y in range (20):
        rect=Rectangle((x1,y1),(x2,y2))
        rect.draw(v)
        x1-=10
        y1-=10
        x2+=10
        y2+=10
        rect.fill=None
        
def estrella(v):
    tortuga=Arrow((100,200),0)
    tortuga.draw(v)
    tortuga.penDown()
    for x in range(5):
        tortuga.forward(200)
        tortuga.rotate(144)
        
def cuadrados(v):   
    tortuga=Arrow((200,200),0)
    tortuga.draw(v)
    tortuga.penDown()
    i=10
    for x in range (0,73):
        tortuga.forward(i)
        tortuga.rotate(90)
        i=i+5
            
def circulos(v):
    cir=Circle((250,200),50)
    cir.fill=None
    for angulo in range (0,360,30):
        cir=Circle((200,200),50)
        cir.fill = None
        cir.rotate(angulo)
        cir.forward(50)
        cir.draw(v)
            
def figuraGeometrica(v):
    m=0
    while m!=5:
        m=int(input('''1. Criculo y Rectangulo
2. Estrella
3. Cuadrado
4. Circulos
5. Salir
    Tecle su opción'''))
        if m==1:
            circulosRectangulos(v)
        elif m==2:
            estrella(v)
        elif m==3:
            cuadrados(v)
        elif m==4:
            circulos(v)
    

def aproximacionPi():
    suma=0
    signo=1
    n=int(input('Valor de n'))
    for k in range(1,n+1,2):
        if n<=100:
            if signo>0:
                print('+', end=' ')
            else:
                print('-', end=' ')
            print(('1/%i'% k), end=' ')
        suma=suma+signo/k
        signo*=-1
    print('\nPI=',suma*4)
    
def divisiblesDe17():
    contador=0
    for n in range (999,9999):
        if n%17==0:
            contador+=1
    print("Existen",contador,"numeros de 4 digitos que son divisibles entre 17")
 
def valoresNumericos():
    acumulador=1
    numero=1
    contador=10
    for digito in range(1,10):
        print(acumulador,"*",8,"+",digito,"=",(acumulador*8+digito))
        numero+=contador
        acumulador+=numero
        contador*=10        
    print("\n")
    num=1
    contador=10
    for x in range(9) :
        print(num,"*",num,"=",num*num)
        num+=contador
        contador*=10
 
def main():
    v=Window('Ventana',400,400)
    m=0
    while m!=5:
        m=int(input('''1. Figura Geométrica
2. Aproximación a Pi
3. Cuatro digitos divisibles entre 17
4. Valores Numéricos
5. Salir
    Tecle su opción'''))
        if m==1:
            figuraGeometrica(v)
        elif m==2:
            aproximacionPi()
        elif m==3:
            divisiblesDe17()
        elif m==4:
            valoresNumericos()
main()