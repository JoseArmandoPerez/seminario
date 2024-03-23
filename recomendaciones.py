import tkinter as tk

def recomendaciones_ventana():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Recomendaciones")
    # Ventana de tamaño completo
    nueva_ventana.attributes('-fullscreen', True)
    label = tk.Label(nueva_ventana, text="¡Hola desde la Ventana 1!")
    label.pack()
