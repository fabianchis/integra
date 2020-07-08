#el cont empieza en menos uno porque el primero no cuenta
cont = -1
def fibonacci(num):
    global cont
    if num==0:
        cont=cont+1
        return 1
    elif num==1:
        cont=cont+1
        return 1
    else:
        cont= cont+1
        return fibonacci(num-1)+fibonacci(num-2)

def main():
    global cont
    num = int(input("Que numero de fibbonacci desea? \n"))
    resultado = str(fibonacci(num))
    print(cont)
    cont=-1
    return resultado

def igualNum():
    num1 = int(input("digite el primer numero \n"))
    num2 = int(input("digite el segundo numero numero \n"))

    if largo(num1) == largo(num2):
        return comparaNumeros(num1, num2) 
    else:
        print("intente otra vez")
        return igualNum()

def largo(num):
    if num==0:
        return 1
    else:
        return 1 + largo(num//10)
    
def comparaNumeros(num1,num2):
    if num1==0:
        return "Son iguales"
    elif num1%10 == num2%10:
        return comparaNumeros(num1//10,num2//10)
    else:
        return "los numeros son diferentes"
