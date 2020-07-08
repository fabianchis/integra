def areaCirculo():
    r = int(input("Defina el valor del radio:"))
    pi=3.1415
    area = r*r*pi
    return area

    
def areaCuadrado():
    l = int(input("Defina el valor del lado"))
    area = l**2
    print(area)


def ejemploIfElse():
    opcion = int(input("1.Area de circulo\n2.Area de un cuadrado\n"))

    if (opcion == 1):
        areaCirculo()
        
    elif(opcion == 2):
        areaCuadrado()        

    else:
        print("La opcion es incorrecta")
