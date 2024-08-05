#Programa básico para el entendimiento del entorno gráfico

from tkinter import * #Uso de imágnes png y gif
##Creación de la raíz
ig = Tk()
'''#Nombre que toma la ventana
ig.title(" Ventana de prueba ")
#Condiciones de redimensionar la ventana (Width,Height)
ig.resizable(1,1) #Booleans
#Icono de la ventana
ig.iconbitmap("dino.ico")
#Tamaño default de la ventan (width,height)
#ig.geometry("650x350")
#configuración de la interfaz por ejemplo el color del fondo
ig.config(bg="blue")'''
##Creación del Frame; tiene características fijas
fr=Frame(ig,width=500,height=400)
#Frame empaquetado según cierta ubicación default es "top"
fr.pack()
''' 
fr.pack(side="right",anchor="n")#right, left, top, bottom && n,s,w,e
fr.pack(fill="x") #Rellena en eje x sin importar la posición
fr.pack(fill="y",expand=1) #Rellena en eje y
fr.pack(fill="both",expand=1) #Rellena en ambas direcciones

'''
'''#Configuración del frame
fr.config(bg="green",width="650",height="350",relief="groove",bd=35)
relief: tipo de borde bd:ancho del borde
#Configuración del cursor
fr.config(cursor="hand2")'''

##Label
'''
im=PhotoImage(file="GJ.png")
lb1=Label(fr,image=im)
lb=Label(fr,text="Hola",fg="blue",font=("Comic Sans MS",18))
#Si se empaqueta el label, la interfaz se adaptará a las 
# dimensiones de la misma lb.pack() por lo que es preferible usar:
lb.place(x=100,y=200)
lb1.place(x=100,y=100)
'''
##Cuadro de Texto
''' si se coloca con place dos elementos en las misms coordenadas, será 
empujado dando la impresión de un acomodo, sin embargo se pueden presentar
distintos errores
tb=Entry(fr)
tb.place(x=100,y=100)
lb2=Label(fr,text="Introudce texto: ")
lb2.place(x=100,y=100)'''

'''Aplicación corregida con grid: se genera un grid 
donde se pueden ubicar distintos elementos, sin embargo se ajusta 
la ventana como con .pack
'''

#con sticky se colocan los elementos según la dirección deseada,
#sin definirlo será centrado
tb=Entry(fr)
tb.grid(row=0,column=1,padx=10,pady=10)
tb.config(fg="green",justify="center",show="*")
lb=Label(fr,text="Texto: ")
lb.grid(row=0,column=0,sticky="w",padx=10,pady=10)
tb1=Entry(fr)
tb1.grid(row=1,column=1,padx=10,pady=10)
lb1=Label(fr,text="Introduzca Texto: ")
lb1.grid(row=1,column=0,sticky="w",padx=10,pady=10)



#Loop para la constante ejecución de la ventana
ig.mainloop()