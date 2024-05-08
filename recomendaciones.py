import tkinter as tk

def recomendaciones_ventana():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Recomendaciones")
    # Ventana de tamaño completo
    nueva_ventana.attributes('-fullscreen', True)
    label = tk.Label(nueva_ventana, text="Recomendaciones", font=("Helvetica", 16))
    label.pack()
    label2 = tk.Label(nueva_ventana, text="Aquí se mostrarán las recomendaciones personalizadas para el usuario", font=("Helvetica", 12))
    label2.pack()
    boton = tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy)
    boton.pack()