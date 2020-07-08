def main():
    try:
        menu()
    except:
        print('Ha ocurrido un error')

def menu():
    print('1.Ejemplo print')
    print('2.Ejemplo for')
    print('3.Ejemplo for2')
    print('4.Ejemplo for3')
    print('5.Ejemplo if/else')
    print('6.Ejemplo if/else/elif')
    print('7.Ejemplo while')
    opt = int(input('Selecione una opcion y presione enter'))

    #hacer un switch para llamar las funciones#
        
        

def helloWorld():
    print('Hello World')
##############################          
def whileEx():
    i = 1
    num = int(input('Introduzca un numero: '))
    while i <= num:
        print(i)
        i += 1
##############################                 
def forEx():
    for i in range(20):
        print(i)

def forEx2():
    for i in [1, 5, 7]:
        print(i)
        
def forEx3():
    for i in "TEXTO":
        print(i)
        
##############################          
def ifElseEx():
    num = int(input('Introduzca un numero: '))
    if num % 2 == 0:
        print('Par')
    else:
        print('Impar')
#############################

def ifElseElifEx (n1, n2):
    if n1 < n2:
        return n2
    elif n2 < n1:
        return n1
    else:
        return n1
 
    
