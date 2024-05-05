import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from Registrar_comida import abrir_ventana_pedidos_comida

carpeta = '../imagenes'
carpeta = os.path.join(os.path.dirname(__file__), "imagenes")

platos_principales = {
    'Sushi de salmón': {
        'ingredientes': ['Arroz', 'Salmón fresco', 'Alga nori', 'Vinagre de arroz', 'Salsa de soja', 'Wasabi', 'Jengibre encurtido'],
        'imagen': os.path.join(carpeta, 'sushi_salmon.jpeg')
    },
    'Tempura de verduras': {
        'ingredientes': ['Verduras variadas', 'Harina', 'Huevo', 'Agua con gas', 'Salsa de soja', 'Jengibre encurtido'],
        'imagen': os.path.join(carpeta, 'tempura_verduras.jpg')
    },
    'Ramen de pollo': {
        'ingredientes': ['Caldo de pollo', 'Fideos ramen', 'Pollo', 'Huevo', 'Cebolleta', 'Brotes de bambú', 'Setas shiitake'],
        'imagen': os.path.join(carpeta, 'ramen_pollo.jpg')
    },
    'Gyudon': {
        'ingredientes': ['Ternera', 'Cebolla', 'Salsa de soja', 'Caldo dashi', 'Azúcar', 'Jengibre', 'Arroz'],
        'imagen': os.path.join(carpeta, 'gyudon.jpg')
    },
}

platos_entradas = {
    'Bruschetta': {
        'ingredientes': ['Pan baguette', 'Ajo', 'Albahaca fresca', 'Aceite de oliva virgen', 'Vinagre balsámico', 'Sal y pimienta al gusto', 'Tomates maduros'],
        'imagen': os.path.join(carpeta, 'gyudon.jpg')
    },
    'Ensalada Caprese': {
        'ingredientes': ['Tomates maduros', 'Mozzarella fresca', 'Hojas de albahaca fresca', 'Aceite de oliva virgen', 'Vinagre balsámico', 'Sal y pimienta al gusto', 'Tomates maduros'],
        'imagen': os.path.join(carpeta, 'gyudon.jpg')
    },
    'Queso fundido': {
        'ingredientes': ['Queso rallado: cheddar, mozzarella, mixto', 'Chorizo, champiñones', 'Tortillas de maíz o chips de tortilla para servir'],
        'imagen': os.path.join(carpeta, 'gyudon.jpg')
    },
    'Sashimi': {
        'ingredientes': ['Pescado fresco: salmón, atún, hamachi (pez limón), vieira', 'Wasabi', 'Salsa de soja'],
        'imagen': os.path.join(carpeta, 'gyudon.jpg')
    },
    'Yakitori': {
        'ingredientes': ['Pollo', 'Salsa Yakitori', 'Sake o mirin', 'Salsa de soja', 'Azúcar', 'Ajo', 'Jengibre rallado'],
        'imagen': os.path.join(carpeta, 'gyudon.jpg')
    },
    'Nigiri sushi': {
        'ingredientes': ['Pescado', 'Arroz sushi', 'Wasabi', 'Salsa de soja', 'Azúcar', 'Jengibre encurtido'],
        'imagen': os.path.join(carpeta, 'gyudon.jpg')
    }
}

platos_postres = {
    'Tarta de queso': {
        'ingredientes': ['Queso crema', 'Azúcar', 'Huevos', 'Extracto de vainilla', 'Galletas para la base', 'Mantequilla'],
        'imagen': os.path.join(carpeta, 'gyudon.jpg')
    },
    'Coulant de chocolate': {
        'ingredientes': ['Chocolate negro', 'Azúcar', 'Huevos', 'Mantequilla', 'Harina'],
        'imagen': os.path.join(carpeta, 'gyudon.jpg')
    },
    'Crème brûlée': {
        'ingredientes': ['Crema de leche', 'Azúcar', 'Yemas de huevo', 'Vainilla'],
        'imagen': os.path.join(carpeta, 'gyudon.jpg')
    },
    'Dorayaki': {
        'ingredientes': ['Harina de trigo', 'Azúcar', 'Miel', 'Huevos', 'Bicarbonato de sodio', 'Agua', 'Anko'],
        'imagen': os.path.join(carpeta, 'gyudon.jpg')
    },
    'Mochi': {
        'ingredientes': ['Harina de arroz glutinoso', 'Azúcar', 'Agua', 'Rellenos: fresa, mango, té verde'],
        'imagen': os.path.join(carpeta, 'gyudon.jpg')
    }

}

def mostrar_menu():
    root = tk.Tk()
    root.title("Menú de Comida Japonesa")
    root.attributes("-fullscreen", True)  # Abrir en pantalla completa

    # Definir colores
    color_fondo = "#FFFAF0"  # Marfil claro
    color_titulo = "#8B4513"  # Marrón oscuro
    color_texto = "#000000"  # Negro
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

    def crear_platos(platos, frame):
        num_columnas = 3  # Número de columnas deseado
        num_platos = len(platos)
        num_filas = (num_platos + num_columnas - 1) // num_columnas  # Cálculo del número de filas necesario

        for contador, (plato, detalle) in enumerate(platos.items()):
            fila = contador // num_columnas
            columna = contador % num_columnas

            frame_plato = tk.Frame(frame, bg=color_fondo, bd=2, relief=tk.RAISED)
            frame_plato.grid(row=fila, column=columna, padx=20, pady=20, sticky="nsew")  # Ajustar al tamaño de la celda y centrar

            # Cargar imagen sin modificar tamaño
            imagen = Image.open(detalle['imagen'])
            imagen = imagen.resize((100, 100))
            imagen = ImageTk.PhotoImage(imagen)

            label_imagen = tk.Label(frame_plato, image=imagen, bg=color_fondo)
            label_imagen.image = imagen
            label_imagen.grid(row=0, column=0, padx=10, pady=10, sticky="n")  # Centrar la imagen

            label_plato = tk.Label(frame_plato, text=plato, font=("Helvetica", 16, "bold"), bg=color_recuadro, fg=color_titulo)
            label_plato.grid(row=1, column=0, padx=10, pady=(0, 5), sticky="nsew")  # Centrar el texto del plato y ajustar al recuadro

            # Mostrar los ingredientes sin marco
            label_ingredientes = tk.Label(frame_plato, text=", ".join(detalle['ingredientes']), font=("Helvetica", 12), bg=color_fondo, fg=color_texto, wraplength=200)
            label_ingredientes.grid(row=2, column=0, padx=120, pady=(40, 40), sticky="nsew")

    # Crear platos en cada página
    crear_platos(platos_principales, frame_principales)
    crear_platos(platos_entradas, frame_entradas)
    crear_platos(platos_postres, frame_postres)

    # Botón para abrir Registrar_comida.py
    button_registrar_comida = tk.Button(root, text="Registrar Comida", font=("Helvetica", 16), command=abrir_ventana_pedidos_comida, bg=color_fondo, fg=color_titulo)
    button_registrar_comida.pack(side="bottom", pady=20)

    notebook.pack(fill='both', expand=True)
    root.mainloop()

if __name__ == "__main__":
    mostrar_menu()
