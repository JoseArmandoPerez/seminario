import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from PIL import Image, ImageTk
import qrcode
import os

# Listas de bebidas con descripciones
bebidas = {
    'Coca-Cola': "Refresco de cola clásico, muy refrescante.",
    'Pepsi': "Otra variante popular del refresco de cola.",
    'Fanta': "Bebida de naranja sin alcohol.",
    'Sprite': "Refresco de limón lima sin colorantes.",
    '7 Up': "Refresco de limón con burbujas.",
    'Jarritos': "Refresco mexicano de sabores frutales.",
    'Agua mineral': "Agua con gas naturalmente enriquecida con minerales.",
    'Limonada': "Bebida tradicional hecha de limones frescos.",
    'Té helado': "Té negro refrescante servido frío.",
    'Agua de horchata': "Bebida tradicional hecha con arroz y canela."
}

def abrir_ventana_pedidos():
    ventana_pedidos = tk.Toplevel()
    ventana_pedidos.title("Pedidos de Bebidas")
    ventana_pedidos.geometry('800x600')


    # Canvas y Scrollbar
    canvas = tk.Canvas(ventana_pedidos)
    scrollbar = ttk.Scrollbar(ventana_pedidos, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    carrito = {}
    notas = {}

    def agregar_al_carrito(producto, incremento=1):
        if producto in carrito:
            carrito[producto] += incremento
            if carrito[producto] <= 0:
                del carrito[producto]  # Eliminar producto si la cantidad es cero o menor
        elif incremento > 0:
            carrito[producto] = incremento
        actualizar_carrito()

    def agregar_nota(producto):
        nota = simpledialog.askstring("Agregar nota", "Nota para " + producto + ":")
        if nota:
            notas[producto] = nota
        actualizar_carrito()

    def actualizar_carrito():
        texto_carrito = "Carrito:\n" + "\n".join(f"{prod}: {cant} {'Nota: ' + notas[prod] if prod in notas else ''}" for prod, cant in carrito.items())
        label_carrito.config(text=texto_carrito)

    def crear_boton_bebida(nombre, descripcion, frame, col, row):
        bebida_frame = tk.Frame(frame, bd=2, relief="groove", padx=5, pady=5, bg='#F7C898')  # Fondo rojo pastel para los recuadros
        bebida_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # Cargar imagen
        ruta_imagen = os.path.join(os.path.dirname(__file__), 'imagenes', 'bebida1.png')
        try:
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((100, 100), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(e)  # Imprime el error si la imagen no carga
            photo = None

        label_imagen = tk.Label(bebida_frame, image=photo)
        label_imagen.image = photo  # mantener referencia
        label_imagen.pack(side="top", pady=5)

        label_nombre = tk.Label(bebida_frame, text=nombre, font=("Helvetica", 12, "bold"),bg='#F7C898',  fg='black')  # Fondo amarillo, texto negro
        label_nombre.pack(side="top")

        label_descripcion = tk.Label(bebida_frame, text=descripcion, font=("Helvetica", 10),bg='#F7C898', fg='black')  # Fondo amarillo, texto negro
        label_descripcion.pack(side="top")

        boton_aumentar = tk.Button(bebida_frame, text="Añadir", command=lambda: agregar_al_carrito(nombre), bg='#C2F798', fg='black')  # Botón verde
        boton_aumentar.pack(side="left", padx=10)

        boton_disminuir = tk.Button(bebida_frame, text="Quitar", command=lambda: agregar_al_carrito(nombre, -1), bg='#F57682', fg='black')  # Botón rojo
        boton_disminuir.pack(side="right", padx=10)

        boton_nota = tk.Button(bebida_frame, text="Agregar nota", command=lambda: agregar_nota(nombre), bg='#F5D276', fg='black')  # Botón amarillo
        boton_nota.pack(side="bottom", pady=5)

    col = 0
    row = 0
    for nombre, descripcion in bebidas.items():
        crear_boton_bebida(nombre, descripcion, scrollable_frame, col, row)
        col += 1
        if col == 4:  # Ajusta el número de columnas aquí
            col = 0
            row += 1

    label_carrito = tk.Label(ventana_pedidos, text="Carrito:", bg='#FFDAB9', fg='black')  # Fondo naranja pastel, texto negro
    label_carrito.pack(side="bottom", fill="x")

    boton_confirmar = tk.Button(ventana_pedidos, text="Generar QR del Pedido", command=lambda: generar_y_mostrar_qr(carrito, notas), bg='#FFFF00', fg='black')  # Botón amarillo
    boton_confirmar.pack(side="bottom", pady=10)

    def generar_y_mostrar_qr(carrito, notas):
        info = "\n".join(f"{producto}: {cantidad} {'Nota: ' + notas[producto] if producto in notas else ''}" for producto, cantidad in carrito.items())
        qr = qrcode.make(info)
        qr_image = ImageTk.PhotoImage(qr)
        qr_window = tk.Toplevel(ventana_pedidos)
        qr_window.title("Código QR del Pedido")
        tk.Label(qr_window, image=qr_image).pack()
        qr_window.mainloop()

    # Packing
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

if __name__ == "__main__":
    root = tk.Tk()
    tk.Button(root, text="Abrir Ventana de Pedidos", command=abrir_ventana_pedidos).pack()
    root.mainloop()

