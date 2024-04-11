import tkinter as tk
from PIL import Image, ImageTk

platos_principales = {
    'Sushi de salmón': {
        'ingredientes': ['Arroz', 'Salmón fresco', 'Alga nori', 'Vinagre de arroz', 'Salsa de soja', 'Wasabi', 'Jengibre encurtido'],
        'imagen': 'sushi_salmon.jpeg'
    },
    'Tempura de verduras': {
        'ingredientes': ['Verduras variadas', 'Harina', 'Huevo', 'Agua con gas', 'Salsa de soja', 'Jengibre encurtido'],
        'imagen': 'tempura_verduras.jpg'
    },
    'Ramen de pollo': {
        'ingredientes': ['Caldo de pollo', 'Fideos ramen', 'Pollo', 'Huevo', 'Cebolleta', 'Brotes de bambú', 'Setas shiitake'],
        'imagen': 'ramen_pollo.jpg'
    },
    'Gyudon': {
        'ingredientes': ['Ternera', 'Cebolla', 'Salsa de soja', 'Caldo dashi', 'Azúcar', 'Jengibre', 'Arroz'],
        'imagen': 'gyudon.jpg'
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
        imagen = Image.open(detalle[''])
        imagen = imagen.resize((100, 100), Image.ANTIALIAS)  # Ajustar tamaño de imagen
        imagen = ImageTk.PhotoImage(imagen)

        label_imagen = tk.Label(frame_plato, image=imagen, bg=color_fondo)
        label_imagen.image = imagen
        label_imagen.pack(side="left", padx=10, pady=10)

        label_plato = tk.Label(frame_plato, text=plato, font=("Helvetica", 16, "bold"), bg=color_fondo, fg=color_titulo)
        label_plato.pack(side="left", padx=(10, 20), pady=10)

        label_ingredientes = tk.Label(frame_plato, text=", ".join(detalle['ingredientes']), font=("Helvetica", 12), bg=color_fondo, fg=color_texto)
        label_ingredientes.pack(side="left", padx=(10, 0), pady=10)

    root.mainloop()

mostrar_menu()
