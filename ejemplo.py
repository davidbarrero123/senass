from tkinter import *

# crea una ventana
ventana = Tk()

# establece el tamaño de la ventana
ventana.geometry("400x400")

# crea una imagen de fondo para el primer botón
imagen1 = PhotoImage(file="b.jpg")

# crea el primer botón con la imagen de fondo
boton1 = Button(ventana, image=imagen1)

# coloca el botón en la ventana
boton1.pack()

# crea una imagen de fondo para el segundo botón
imagen2 = PhotoImage(file="a.png")

# crea el segundo botón con la imagen de fondo
boton2 = Button(ventana, image=imagen2)

# coloca el botón en la ventana
boton2.pack()

# inicia el bucle de eventos de la ventana
ventana.mainloop()

