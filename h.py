from tkinter import *
import os

# define una función para ejecutar un archivo de Python
def ejecutar_archivo(archivo):
    os.execfile(archivo)

# crea una ventana
ventana = Tk()

# establece el tamaño de la ventana
ventana.geometry("400x400")

# crea una imagen de fondo para el botón
imagen = PhotoImage(file="a.png").subsample(2).subsample(2)

# crea el botón con la imagen de fondo y la función de acción correspondiente
boton = Button(ventana, image=imagen, command=lambda: ejecutar_archivo("otro_archivo.py"))

# coloca el botón en la ventana
boton.pack()

# inicia el bucle de eventos de la ventana
ventana.mainloop()
