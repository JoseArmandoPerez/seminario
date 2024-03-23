import tkinter as tk
from recomendaciones import recomendaciones_ventana
from acerca import acerca_ventana
from mesas import mesas_ventana

def salir():
    root.destroy()
    
root = tk.Tk()
root.title("Interfaz con Botones")
root.attributes('-fullscreen', True)  # Set the window to fullscreen

# Imagen de fondo
imagen_fondo = tk.PhotoImage(file="imagenes/background_image.png")
fondo = tk.Label(root, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

about_button = tk.Button(root, text="Acerca de nosotros", font=("Helvetica", 24), command=acerca_ventana, width=15)
about_button.place(relx=0.5, rely=0.5, anchor="center")

tables_button = tk.Button(root, text="Mesas disponibles", font=("Helvetica", 24), command=mesas_ventana, width=15)
tables_button.place(relx=0.5, rely=0.6, anchor="center")

recommendations_button = tk.Button(root, text="Recomendaciones", font=("Helvetica", 24), command=recomendaciones_ventana, width=15)
recommendations_button.place(relx=0.5, rely=0.7, anchor="center")

close_button = tk.Button(root, text="Salir", font=("Helvetica", 24), command=salir, width=15)
close_button.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()