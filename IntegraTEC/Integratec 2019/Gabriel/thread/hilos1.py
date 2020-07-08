from tkinter import *
import winsound
from threading import *
import time


ventanaani= Tk()
ventanaani.title("animación")
ventanaani.geometry("600x600")
canvas = Canvas(ventanaani , width= 600, height = 600, bg = "black")
canvas.place(x=0,y=0)

#TENES QUE CAMBIAR A LAS IMAGENES TUYAS PARA QUE FUNCIONE
emoji= PhotoImage (file= 'persona.png')
emoji1=canvas.create_image(10, 10, image=emoji, anchor= NW)

imag=PhotoImage (file= 'persona2.png')
imag1=canvas.create_image(120, 120, image=imag, anchor= NW)

#ESTOS THREADS NO SON NECESARIOS PORQUE CON LO QUE HACEN LO PODES HACER CON UNO SOLO MODIFICANDO EN LAS FUNCIONES
#threademoji2 = Thread(target= movemoji2, args=(canvas,emoji,0,0))
#threademoji3 = Thread(target= movemoji3, args=(canvas,emoji,0,0))
#threademoji4 = Thread(target= movemoji4, args=(canvas,emoji,0,0))


#threadimag2 = Thread(target= movimag2, args=(canvas,imag,0,0))
#threadimag3 = Thread(target= movimag3, args=(canvas,imag,0,0))
#threadimag4 = Thread(target= movimag4, args=(canvas,imag,0,0))

def movemoji(canvas,emoji,x,y):
    if x==31:
        movemoji2(canvas,emoji1,0, 0)  #ACA LO QUE HICE FUE EMPEZAR EL OTRO MOVIMIENTO EN LUGAR DE INICIAR OTRO
    else:                              #DEBIDO A QUE EL MOVIMIENTO FINALIZA EN EL MOVIMIENTO NUMERO 4 Y ASI EL THREAD TERMINA SOLO
        canvas.move(emoji1,x,0)
        canvas.update()
        time.sleep(0.009)
        movemoji(canvas,emoji1,x+1,y)


def movemoji2(canvas,emoji,x,y):
    if y==28:
        movemoji3(canvas,emoji1, 0,0) 
    else:
        canvas.move(emoji1,0,y)
        canvas.update()
        time.sleep(0.009)
        movemoji2(canvas,emoji1,x, y+1)

def movemoji3(canvas,emoji,x,y):
    if x==-31:
        movemoji4(canvas,emoji1, 0,0)
    else:
        canvas.move(emoji1,x,0)
        canvas.update() 
        time.sleep(0.009)
        movemoji3(canvas,emoji1, x-1,y)
def movemoji4(canvas,emoji,x,y):
    if y==-28:
        return #este return hace que el movimiento se termine
    else:
        canvas.move(emoji1,0,y)
        canvas.update()
        time.sleep(0.009)
        movemoji4(canvas,emoji1, x,y-1)
        
def movimag(canvas,imag,x,y):
    if x==19:
        movimag2(canvas,imag1,0,0) #ACA HICE LO MISMO QUE CON EL movemoji 
    else:
        canvas.move(imag1,x,0)
        canvas.update()
        time.sleep(0.009)
        movimag(canvas,imag1,x+1,y)
   
def movimag2(canvas,imag,x,y):
    if y==18:
        movimag3(canvas,imag1, 0,0) 
    else:
        canvas.move(imag1,0,y)
        canvas.update()
        time.sleep(0.009)
        movimag2(canvas,imag1,x,y+1)
def movimag3(canvas,imag,x,y):
    if x==-19:
        movimag4(canvas,imag1,0,0) 
    else:
        canvas.move(imag1,x,0)
        canvas.update() 
        time.sleep(0.009)
        movimag3(canvas,imag1, x-1,y)
def movimag4(canvas,imag,x,y):
    if y==-18:
        return 
    else:
        canvas.move(imag1,0,y)
        canvas.update()
        time.sleep(0.009)
        movimag4(canvas,imag1,x,y-1)

#Los threads se crean adentro de la funcion iniciar para que no queden corriendo
#y que vuelvan a iniciarse


def iniciar():
    threademoji = Thread(target= movemoji, args=(canvas,emoji,0,0))
    threadimag = Thread(target= movimag, args=(canvas,imag,0,0))
    threademoji.start()
    threadimag.start()

botoniniciar= Button(canvas, text= "animar", command=iniciar, bg="red", fg="black",font="Century")
botoniniciar.place(x=500,y=500)
ventanaani.mainloop()
