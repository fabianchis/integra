
numeros = [0,0,0,0,0,0,0,0,0,0]
tuplaAux = ()
def main():
    num = int(input("Meter el numero \n"))
    if (num >=0):
        repeticiones(num)
    else:
        print("intente de nuevo")
        return main()

    
def repeticiones(num):
    global numeros
    if num==0:
        return repAux(1234567890) 
    else:
        numeros[num%10]+=1
        repeticiones(num//10)
        
def repAux(numAux):
    global tuplaAux
    global numeros
    if numAux ==0:
        numeros = [0,0,0,0,0,0,0,0,0,0]
        print(tuplaAux)
        return tuplaAux
    else:
        if numeros[numAux%10] != 0:
            tuplaAux = tuplaAux +((numAux%10, numeros[numAux%10]))
            return repAux(numAux//10)
        else:
            return repAux(numAux//10)
        
    
