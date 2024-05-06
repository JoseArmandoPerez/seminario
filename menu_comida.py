import tkinter as tk
from tkinter import ttk
import json
from Registrar_comida import abrir_ventana_pedidos_comida

# Función para cargar datos desde un archivo JSON
def cargar_datos(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Cargar los datos de bebidas e ingredientes
datos = cargar_datos('Platillos.json')
bebidas = datos['bebidas']
platos_principales = datos['platos_principales']
platos_entradas = datos['platos_entradas']
platos_postres = datos['platos_postres']

def mostrar_menu():
    root = tk.Tk()
    root.title("Menú de Comida Japonesa")
    root.attributes("-fullscreen", True)  # Abrir en pantalla completa

    # Definir colores
    color_fondo = "#FFFAF0"  # Marfil claro
    color_titulo = "#8B4513"  # Marrón oscuro
    color_recuadro = "#F7C898"  # Amarillo pastel

    # Crear estilo para las pestañas
    estilo = ttk.Style()
    estilo.theme_create("EstiloPestanas", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": color_fondo},
            "map": {"background": [("selected", color_fondo)],
                    "foreground": [("selected", color_titulo)]}
        }})

    estilo.theme_use("EstiloPestanas")

    # Crear pestañas
    notebook = ttk.Notebook(root)

    # Página de platos principales
    frame_principales = tk.Frame(notebook, bg=color_fondo)
    notebook.add(frame_principales, text='Platos Principales')

    # Página de platos de entradas
    frame_entradas = tk.Frame(notebook, bg=color_fondo)
    notebook.add(frame_entradas, text='Entradas')

    # Página de platos de postres
    frame_postres = tk.Frame(notebook, bg=color_fondo)
    notebook.add(frame_postres, text='Postres')

    # Página de bebidas
    frame_bebidas = tk.Frame(notebook, bg=color_fondo)
    notebook.add(frame_bebidas, text='Bebidas')

    def crear_platos(platos, frame):
        num_columnas = 6  # Número de columnas deseado
        num_platos = len(platos)
        num_filas = (num_platos + num_columnas - 1) // num_columnas  # Cálculo del número de filas necesario

        for nombre, detalle in platos.items():
            contador = list(platos.keys()).index(nombre)
            fila = contador // num_columnas
            columna = contador % num_columnas

            frame_plato = tk.Frame(frame, bg=color_recuadro, bd=2, relief="groove", width=200, height=200) # Tamaño fijo para todos los recuadros
            frame_plato.grid(row=fila, column=columna, padx=10, pady=10) 

            # Nombre del plato
            label_nombre = tk.Label(frame_plato, text=nombre, font=("Helvetica", 14, "bold"), bg=color_recuadro, fg="black")
            label_nombre.grid(row=1, column=0, columnspan=3) # Ajustar posición del nombre del plato

            # Descripción del plato con salto de línea
            descripcion = detalle.get('descripcion', '')  # Obtener la descripción del plato si existe
            label_descripcion = tk.Label(frame_plato, text=descripcion, font=("Helvetica", 10), bg=color_recuadro, fg="black", wraplength=180)
            label_descripcion.grid(row=2, column=0, columnspan=3)  # Ajustar posición de la descripción

    # Crear platos en cada página
    crear_platos(platos_principales, frame_principales)
    crear_platos(platos_entradas, frame_entradas)
    crear_platos(platos_postres, frame_postres)

    # Crear bebidas
    crear_platos(bebidas, frame_bebidas)

    # Botón para abrir Registrar_comida.py
    button_registrar_comida = tk.Button(root, text="Registrar Comida", font=("Helvetica", 16), command=abrir_ventana_pedidos_comida, bg=color_fondo, fg=color_titulo)
    button_registrar_comida.pack(side="bottom", pady=20)

    # Centrar la ventana
    root.eval('tk::PlaceWindow . center')

    notebook.pack(fill='both', expand=True)
    root.mainloop()

if __name__ == "__main__":
    mostrar_menu()
