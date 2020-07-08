def octToDecimal(num,exp):
    if (num<=0):
        return 0
    else:
        return ((num%10)*8**exp)+octToDecimal(num//10,exp+1)

def comprobacion(num):
    if(num==0):
        return True
    elif((num%10)>7):
        return False
    else:
        return comprobacion(num//10)

def mainOCtalADecimal():
    num = int(input("Agregue el numero octal: \n"))
    if (comprobacion(num)==True):
        return octToDecimal(num,0)
    else:
        return "Numero invalido"


def fibonacci(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
    
def serieFib(num,N,serie):
    if N==num:
        return serie
    else:
        serie = serie + [fibonacci(N)]
        return serieFib(num,N+1,serie)

    
def mainSerieFib():
    num = int(input("Que serie de fibbonacci desea? \n"))
    N = 0
    return serieFib(num,N,[])

def abz(num):
    if num<0:
        return -num
    else:
        return num
def dividir(dividendo, divisor):
    if dividendo<0 :
        if dividendo>divisor:
            return 0
        else:
            return (-1- abz(dividir(dividendo+divisor, divisor)))
    else:
        if dividendo<divisor:
            return 0
        else:
            return 1 + dividir(dividendo-divisor, divisor)
def main():
    opcion = int(input("Cual progra ocupa Kenneth: \n 1. Octal a Decimal \n 2. Fibonacci \n 3. Serie de Fibonacci \n 4.Division a pata" ))
    if opcion==1:
        return mainOCtalADecimal()
    elif opcion==2:
        num = int(input("Que numero de fibbonacci desea? \n"))
        return fibonacci(num)
    elif opcion==3:
        return mainOCtalADecimal()
    else:
        dividendo = int(input("Defina el dividendo"))
        divisor = int(input("Defina el divisor"))
        return dividir(dividendo, divisor)


   
    
