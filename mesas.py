import tkinter as tk

def mesas_ventana():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Mesas Disponibles")
    nueva_ventana.attributes('-fullscreen', True)
    label = tk.Label(nueva_ventana, text="¡Hola desde la Ventana 3!")
    label.pack()
