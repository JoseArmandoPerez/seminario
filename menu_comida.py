import tkinter as tk
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

def mostrar_menu():
        root = tk.Tk()
        root.title("Menú de Comida Japonesa")
        root.attributes("-fullscreen", True)  # Abrir en pantalla completa

        # Definir colores
        color_fondo = "#FFFAF0"  # Marfil claro
        color_titulo = "#8B4513"  # Marrón oscuro
        color_texto = "#000000"  # Negro

        frame_menu = tk.Frame(root, bg=color_fondo)
        frame_menu.pack(fill="both", expand=True)

        label_titulo = tk.Label(frame_menu, text="Menú de Comida Japonesa", font=("Helvetica", 24, "bold"), bg=color_fondo, fg=color_titulo)
        label_titulo.pack(pady=(20,10))

        for plato, detalle in platos_principales.items():
            frame_plato = tk.Frame(frame_menu, bg=color_fondo, bd=2, relief=tk.RAISED)
            frame_plato.pack(anchor="w", fill="x", padx=20, pady=10)

            # Cargar imagen y ajustar tamaño si es necesario
            imagen = Image.open(detalle['imagen'])
            imagen = imagen.resize((100, 100))  # Ajustar tamaño de imagen
            imagen = ImageTk.PhotoImage(imagen)

            label_imagen = tk.Label(frame_plato, image=imagen, bg=color_fondo)
            label_imagen.image = imagen
            label_imagen.pack(side="left", padx=10, pady=10)

            label_plato = tk.Label(frame_plato, text=plato, font=("Helvetica", 16, "bold"), bg=color_fondo, fg=color_titulo)
            label_plato.pack(side="left", padx=(10, 20), pady=10)

            label_ingredientes = tk.Label(frame_plato, text=", ".join(detalle['ingredientes']), font=("Helvetica", 12), bg=color_fondo, fg=color_texto)
            label_ingredientes.pack(side="left", padx=(10, 0), pady=10)

        # Botón para abrir Registrar_comida.py
        button_registrar_comida = tk.Button(frame_menu, text="Registrar Comida", font=("Helvetica", 16), command=abrir_ventana_pedidos_comida)
        button_registrar_comida.pack(side="bottom", pady=20)

        root.mainloop()
    
if __name__ == "__main__":
    mostrar_menu()
