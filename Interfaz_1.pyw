from tkinter import *

raiz = Tk()

#Nombre que toma la ventana
raiz.title(" Ventana de prueba ")
#Condiciones de redimensionar la ventana (Width,Height)
raiz.resizable(0,1) #Booleans
#Icono de la ventana
raiz.iconbitmap("dino.ico")
#Tamaño default de la ventan (width,height)
raiz.geometry("650x350")
#configuración de la interfaz por ejemplo el color del fondo
raiz.config(bg="blue")
#Loop para la constante ejecución de la ventana
raiz.mainloop()