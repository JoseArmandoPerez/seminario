import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from PIL import Image, ImageTk
import requests
import qrcode
import os

# Dirección IP del servidor y ruta para obtener la lista de bebidas
SERVER_URL = "http://172.16.119.180/:5000"
BEBIDAS_ENDPOINT = f"{SERVER_URL}/bebidas"
PLATILLO_ENDPOINT = f"{SERVER_URL}/platillo"

text_carrito = None

def obtener_lista_bebidas():
    try:
        response = requests.get(BEBIDAS_ENDPOINT)
        response.raise_for_status()  # Lanzar una excepción si hay un error en la solicitud
        data = response.json()
        return data
    except requests.RequestException as e:
        print("Error al obtener la lista de bebidas:", e)
        return {}
    
def obtener_lista_platillo():
    try:
        response = requests.get(PLATILLO_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print("Error al obtener la lista de platillos:", e)
        return {} 
    
def abrir_ventana_pedidos():
    global text_carrito
    ventana_pedidos = tk.Toplevel()
    ventana_pedidos.title("Pedidos de Bebidas")
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
            # Obtener el ID de la bebida
            id_bebida = producto.get('id')
            id_platillo = producto.get('id')

            # Hacer una solicitud GET a la ruta de la API Flask para obtener los ingredientes de la bebida
            response = requests.get(f"{SERVER_URL}/ingredientes/{id_bebida}")
            response.raise_for_status()  # Lanzar una excepción si hay un error en la solicitud
            ingredientes_bebida = response.json()
            
            response = requests.get(f"{SERVER_URL}/ingredinetes/{id_platillo}")
            response.raise_for_status()
            ingredientes_platillo = response.json()
            
            if ingredientes_bebida:
                # Crear ventana emergente para mostrar los ingredientes
                ventana_ingredientes = tk.Toplevel()
                ventana_ingredientes.title(f"Ingredientes para {producto['nombre']}")
                ventana_ingredientes.geometry("400x300")
            
                # Mostrar los ingredientes en la ventana emergente
                label_ingredientes = tk.Label(ventana_ingredientes, text="Ingredientes:")
                label_ingredientes.pack()

                for ingrediente in ingredientes_bebida:
                    nombre = ingrediente.get('nombre', 'Nombre no disponible')
                    cantidad = ingrediente.get('cantidad', 'Cantidad no disponible')
                    label = tk.Label(ventana_ingredientes, text=f"{nombre}: {cantidad}")
                    label.pack()

            else:
                messagebox.showinfo("Información", "No se encontraron ingredientes para esta bebida.")

        except requests.RequestException as e:
            print("Error al obtener los ingredientes:", e)

    def actualizar_carrito():
        # Función de actualizar el carrito, igual que en el código original
        pass

    def crear_boton_bebida(nombre, descripcion, frame, col, row):
        bebida_frame = tk.Frame(frame, bd=2, relief="groove", padx=5, pady=5, bg='#F7C898')
        bebida_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew", ipadx=10, ipady=10)

        ruta_imagen = os.path.join(os.path.dirname(__file__), 'imagenes', 'bebida.png')
        try:
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((100, 100), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(e)
            photo = None

        label_imagen = tk.Label(bebida_frame, image=photo)
        label_imagen.image = photo
        label_imagen.pack(side="top", pady=5)

        label_nombre = tk.Label(bebida_frame, text=nombre, font=("Helvetica", 12, "bold"), bg='#F7C898', fg='black')
        label_nombre.pack(side="top")

        label_descripcion = tk.Label(bebida_frame, text=descripcion, font=("Helvetica", 10), bg='#F7C898', fg='black', wraplength=180)
        label_descripcion.pack(side="top")

        boton_aumentar = tk.Button(bebida_frame, text="Añadir", command=lambda prod=nombre: agregar_al_carrito(prod), bg='#C2F798', fg='black')
        boton_aumentar.pack(side="left", padx=10)

        boton_disminuir = tk.Button(bebida_frame, text="Quitar", command=lambda prod=nombre: agregar_al_carrito(prod, -1), bg='#F57682', fg='black')
        boton_disminuir.pack(side="right", padx=10)

        boton_nota = tk.Button(bebida_frame, text="Agregar Ing", command=lambda prod=nombre: agregar_ingrediente(prod), bg='#F5D276', fg='black')
        boton_nota.pack(side="bottom", pady=5)

    # Obtener la lista de bebidas desde el servidor
    lista_bebidas = obtener_lista_bebidas()

    if lista_bebidas:
        for bebida in lista_bebidas:
            nombre = bebida.get('nombre', 'Nombre no disponible')
            descripcion = bebida.get('descripcion', 'Descripción no disponible')
            crear_boton_bebida(nombre, descripcion, scrollable_frame, col, row)
            col += 1
            if col == 4:
                col = 0
                row += 1
                
    def crear_boton_platillo(nombre, descripcion, frame, col, row):
        platillo_frame = tk.Frame(frame, bd=2, relief="groove", padx=5, pady=5, bg='#F7C898')
        platillo_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew", ipadx=10, ipady=10)

        # Puedes agregar el código para cargar la imagen del platillo, similar al de las bebidas
        ruta_imagen = os.path.join(os.path.dirname(__file__), 'imagenes', 'bebida.png')
        try:
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((100, 100), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(e)
            photo = None
            
        label_imagen = tk.Label(platillo_frame, image=photo)
        label_imagen.image = photo
        label_imagen.pack(side="top", pady=5)
            
        label_nombre = tk.Label(platillo_frame, text=nombre, font=("Helvetica", 12, "bold"), bg='#F7C898', fg='black')
        label_nombre.pack(side="top")

        label_descripcion = tk.Label(platillo_frame, text=descripcion, font=("Helvetica", 10), bg='#F7C898', fg='black', wraplength=180)
        label_descripcion.pack(side="top")

        boton_aumentar = tk.Button(platillo_frame, text="Añadir", command=lambda prod=nombre: agregar_al_carrito(prod), bg='#C2F798', fg='black')
        boton_aumentar.pack(side="left", padx=10)

        boton_disminuir = tk.Button(platillo_frame, text="Quitar", command=lambda prod=nombre: agregar_al_carrito(prod, -1), bg='#F57682', fg='black')
        boton_disminuir.pack(side="right", padx=10)

        boton_nota = tk.Button(platillo_frame, text="Agregar Ing", command=lambda prod=nombre: agregar_ingrediente(prod), bg='#F5D276', fg='black')
        boton_nota.pack(side="bottom", pady=5)

    lista_platillo = obtener_lista_platillo()


    if lista_platillo:
        for platillo in lista_platillo:
            nombre = platillo.get('nombre', 'Nombre no disponible')
            descripcion = platillo.get('descripcion', 'Descripción no disponible')
            crear_boton_bebida(nombre, descripcion, scrollable_frame, col, row)
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
        # Función para generar y mostrar el código QR, igual que en el código original
        pass

    boton_confirmar = tk.Button(cart_frame, text="Generar QR del Pedido", command=generar_y_mostrar_qr)
    boton_confirmar.pack(side="top", pady=10)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="left", fill="y")

    ventana_pedidos.mainloop()

# Llamada para abrir automáticamente la ventana de pedidos al ejecutar el programa
abrir_ventana_pedidos()
