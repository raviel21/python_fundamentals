class Punto:
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=y
    def __add__(self,other):
        return float(str(self.x)+str(other.x)),float(str(self.y)+str(other.y))
    def __mul__(self,other):
        x=self.x * other.x
        y=self.y * other.y
        return x,y
    def __sub__(self,other):
        x=self.x - other.x
        y=self.y - other.y
        return x,y
    def __truediv__(self,other):
        if other.x==0 or other.y==0:
            return "error, operacion de division sobre cero"
        x=self.x / other.x
        y=self.y / other.y
        return x,y

def aplica_operacion(operacion, puntox1, puntoy1, puntox2, puntoy2):
    punto1 = Punto(puntox1,puntoy1)
    punto2 = Punto(puntox2,puntoy2)
    if operacion=="+":
        print(punto1 + punto2)
    elif operacion=="-":
        print(punto1 - punto2)
    elif operacion=="*":
        print(punto1 * punto2)
    elif operacion=="/":
        print(punto1 / punto2)
    else:
        print("Operacion invalida")
    return

punto1 = Punto(4,3)
punto2 = Punto(1,2)
print ("Bienvenido")
puntox_1=int(input("ingresa x1: "))
puntoy_1=int(input("ingresa y1: "))
puntox_2=int(input("ingresa x2: "))
puntoy_2=int(input("ingresa y2: "))
operac=input("ingresa operacion (operaciones permitidas + - * /): ")
print(operac)
aplica_operacion(operac, puntox_1,puntoy_1, puntox_2, puntoy_2)
print("hasta luego")
