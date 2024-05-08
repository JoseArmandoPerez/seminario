import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from PIL import Image, ImageTk
import requests
import qrcode
import os

# Dirección IP del servidor y ruta para obtener la lista de platillos
SERVER_URL = "http://192.168.100.89:5000"
PLATILLOS_ENDPOINT = f"{SERVER_URL}/platillo"

text_carrito = None

def obtener_lista_platillos():  # Función para obtener la lista de platillos
    try:
        response = requests.get(PLATILLOS_ENDPOINT)
        response.raise_for_status()  # Lanzar una excepción si hay un error en la solicitud
        data = response.json()
        return data
    except requests.RequestException as e:
        print("Error al obtener la lista de platillos:", e)
        return {}

def abrir_ventana_pedidos():
    global text_carrito
    ventana_pedidos = tk.Toplevel()
    ventana_pedidos.title("Pedidos de Platillos")  # Modificamos el título para reflejar platillos
    ventana_pedidos.geometry('1000x600')

    main_frame = ttk.Frame(ventana_pedidos)
    main_frame.pack(fill='both', expand=True)

    canvas = tk.Canvas(main_frame)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    carrito = {}
    notas = {}

    col, row = 0, 0

    def agregar_al_carrito(producto, incremento=1):
        if producto in carrito:
            carrito[producto] += incremento
            if carrito[producto] <= 0:
                del carrito[producto]  # Eliminar producto si la cantidad es cero o menor
        elif incremento > 0:
            carrito[producto] = incremento
        actualizar_carrito()

    def agregar_ingrediente(producto):
        try:
            # Obtener el ID del platillo
            id_platillo = producto.get('id')

            # Hacer una solicitud GET a la ruta de la API Flask para obtener los ingredientes del platillo
            response = requests.get(f"{SERVER_URL}/ingredientes/{id_platillo}")
            response.raise_for_status()  # Lanzar una excepción si hay un error en la solicitud
            ingredientes_platillo = response.json()

            if ingredientes_platillo:
                # Crear ventana emergente para mostrar los ingredientes
                ventana_ingredientes = tk.Toplevel()
                ventana_ingredientes.title(f"Ingredientes para {producto['nombre']}")
                ventana_ingredientes.geometry("400x300")

                # Mostrar los ingredientes en la ventana emergente
                label_ingredientes = tk.Label(ventana_ingredientes, text="Ingredientes:")
                label_ingredientes.pack()

                for ingrediente in ingredientes_platillo:
                    nombre = ingrediente.get('nombre', 'Nombre no disponible')
                    cantidad = ingrediente.get('cantidad', 'Cantidad no disponible')
                    label = tk.Label(ventana_ingredientes, text=f"{nombre}: {cantidad}")
                    label.pack()

            else:
                messagebox.showinfo("Información", "No se encontraron ingredientes para este platillo.")

        except requests.RequestException as e:
            print("Error al obtener los ingredientes:", e)

    def actualizar_carrito():
        global text_carrito
        if text_carrito is None:
            text_carrito = tk.Text(cart_frame, height=10, width=50)
            text_carrito.pack(side="top")
        text_carrito.delete(1.0, tk.END)
        for producto, cantidad in carrito.items():
            text_carrito.insert(tk.END, f"{producto}: {cantidad}\n")

    def crear_boton_producto(platillo, frame, col, row):
        producto_frame = tk.Frame(frame, bd=2, relief="groove", padx=5, pady=5, bg='#F7C898')
        producto_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew", ipadx=10, ipady=10)

        ruta_imagen = os.path.join(os.path.dirname(__file__), 'imagenes', 'platillo.png')  
        try:
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((100, 100), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(e)
            photo = None

        label_imagen = tk.Label(producto_frame, image=photo)
        label_imagen.image = photo
        label_imagen.pack(side="top", pady=5)

        label_nombre = tk.Label(producto_frame, text=platillo['nombre'], font=("Helvetica", 12, "bold"), bg='#F7C898', fg='black')
        label_nombre.pack(side="top")

        label_descripcion = tk.Label(producto_frame, text=platillo['descripcion'], font=("Helvetica", 10), bg='#F7C898', fg='black', wraplength=180)
        label_descripcion.pack(side="top")

        label_precio = tk.Label(producto_frame, text=f"Precio: ${platillo['precio']}", font=("Helvetica", 10), bg='#F7C898', fg='black')
        label_precio.pack(side="top")

        boton_aumentar = tk.Button(producto_frame, text="Añadir", command=lambda: agregar_al_carrito(platillo['nombre']), bg='#C2F798', fg='black')
        boton_aumentar.pack(side="left", padx=10)

        boton_disminuir = tk.Button(producto_frame, text="Quitar", command=lambda: agregar_al_carrito(platillo['nombre'], -1), bg='#F57682', fg='black')
        boton_disminuir.pack(side="right", padx=10)

        boton_nota = tk.Button(producto_frame, text="Ingredientes", command=lambda: agregar_ingrediente(platillo), bg='#F5D276', fg='black')
        boton_nota.pack(side="bottom", pady=5)

    # Obtener la lista de platillos desde el servidor
    lista_platillos = obtener_lista_platillos()

    if lista_platillos:
        for platillo in lista_platillos:
            crear_boton_producto(platillo, scrollable_frame, col, row)
            col += 1
            if col == 4:
                col = 0
                row += 1

    cart_frame = tk.Frame(main_frame, bd=2, relief="sunken", padx=5, pady=5)
    cart_frame.pack(side="right", fill="y")

    label_carrito = tk.Label(cart_frame, text="Carrito:")
    label_carrito.pack(side="top", fill="x")

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="left", fill="y")

    def generar_y_mostrar_qr():
        if not carrito:
            messagebox.showinfo("Información", "El carrito está vacío.")
            return

        # Crear datos para el QR
        qr_data = "; ".join([f"{producto}: {cantidad}" for producto, cantidad in carrito.items()])
        qr = qrcode.make(qr_data)

        # Mostrar el QR en una nueva ventana
        top = tk.Toplevel()
        top.title("Código QR del Pedido")
        qr_image = ImageTk.PhotoImage(qr)
        qr_label = tk.Label(top, image=qr_image)
        qr_label.image = qr_image  # mantener una referencia
        qr_label.pack()

    boton_confirmar = tk.Button(cart_frame, text="Generar QR del Pedido", command=generar_y_mostrar_qr)
    boton_confirmar.pack(side="top", pady=10)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="left", fill="y")

    ventana_pedidos.mainloop()
