def area():
    a = int(input("1.Area del circulo \n 2.Area Cuadrado "))
    if (a==1):
        r = int(input("Deme el valor del radio"))
        p=3.14
        area=p*r*r
        print(area)    
    elif(a==2):
        l = int(input("Deme el valor de el lado"))
        area = l*l
        print(area)
    else:
        print("No me dio un valor correcto")
        
    
