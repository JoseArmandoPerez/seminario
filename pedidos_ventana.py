import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Define las comidas, refrescos y bebidas alcohólicas
comidas = ['Pollo a la parmesana', 'Tacos al pastor', 'Enchiladas verdes', 'Ceviche de pescado', 'Chiles rellenos', 'Fajitas de pollo', 'Paella', 'Carpaccio de res', 'Lasagna', 'Risotto de setas']
refrescos = ['Coca-Cola', 'Pepsi', 'Fanta', 'Sprite', '7 Up', 'Jarritos', 'Agua mineral', 'Limonada', 'Té helado', 'Agua de horchata']
bebidas_alcoholicas = ['Cerveza Modelo', 'Cerveza Corona', 'Vino tinto', 'Vino blanco', 'Margarita', 'Mojito', 'Tequila', 'Ron', 'Whisky', 'Mezcal']

# Función para generar el ticket con un código QR
def generar_ticket(pedido_info):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(pedido_info)
    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white')

    # Crea una imagen para el ticket con el código QR
    ticket = Image.new('RGB', (qr_img.width + 500, qr_img.height + 300), 'white')
    draw = ImageDraw.Draw(ticket)
    font = ImageFont.load_default()
    draw.text((10, 10), 'Ticket Restaurante', fill='black', font=font)
    draw.text((10, 30), pedido_info, fill='black', font=font)
    ticket.paste(qr_img, (0, 200))

    # Guarda el ticket como imagen y lo muestra
    ticket_path = 'tickets/ticket.png'
    ticket.save(ticket_path)
    messagebox.showinfo('Ticket generado', f'El ticket se ha generado con éxito y está guardado en {ticket_path}')
    Image.open(ticket_path).show()

# Función para la ventana de pedidos
def pedidos_ventana():
    ventana_pedidos = tk.Toplevel()
    ventana_pedidos.title("Realizar Pedido")
    
    # Carrito de compras
    carrito = {}

    # Función para agregar productos al carrito
    def agregar_al_carrito(producto, cantidad):
        if producto and cantidad.get() > 0:
            carrito[producto] = carrito.get(producto, 0) + cantidad.get()
            actualizar_carrito()

    # Función para actualizar la visualización del carrito
    def actualizar_carrito():
        texto_carrito = "Carrito:\n"
        for producto, cantidad in carrito.items():
            texto_carrito += f"{producto}: {cantidad}\n"
        label_carrito.config(text=texto_carrito)

    # Función para crear marco de productos
    def crear_marco_productos(categoria, productos, fila, columna):
        frame = tk.LabelFrame(ventana_pedidos, text=categoria)
        frame.grid(row=fila, column=columna, padx=10, pady=10, sticky='ew')
        combobox = ttk.Combobox(frame, values=productos, state='readonly')
        combobox.grid(row=0, column=0, padx=10, pady=10)
        cantidad = tk.IntVar(value=1)
        spinbox = tk.Spinbox(frame, from_=0, to=10, textvariable=cantidad)
        spinbox.grid(row=0, column=1, padx=10, pady=10)
        boton_agregar = tk.Button(frame, text="Agregar al carro", command=lambda: agregar_al_carrito(combobox.get(), cantidad))
        boton_agregar.grid(row=0, column=2, padx=10, pady=10)
        return combobox, spinbox, boton_agregar

    # Crear marcos de productos para comidas, refrescos y bebidas alcohólicas
    crear_marco_productos("Comidas", comidas, 0, 0)
    crear_marco_productos("Refrescos", refrescos, 1, 0)
    crear_marco_productos("Bebidas Alcohólicas", bebidas_alcoholicas, 2, 0)

    # Etiqueta para mostrar el carrito
    label_carrito = tk.Label(ventana_pedidos, text="Carrito:\n", justify='left')
    label_carrito.grid(row=3, column=0, columnspan=3, sticky='ew')

    def confirmar_y_generar_ticket():
        # Construir la información del pedido
        pedido_info = "Detalle del pedido:\n"
        for producto, cantidad in carrito.items():
            pedido_info += f"{producto}: {cantidad}\n"
        pedido_info += "\nGracias por su compra!"
        
        # Llamar a la función para generar el ticket
        generar_ticket(pedido_info)

    # Botón para confirmar el pedido y generar el ticket
    boton_confirmar = tk.Button(ventana_pedidos, text="Confirmar Pedido", command=confirmar_y_generar_ticket)
    boton_confirmar.grid(row=4, column=0, columnspan=3, pady=10)

    # Botón para cerrar la ventana de pedidos
    boton_cerrar = tk.Button(ventana_pedidos, text="Cerrar", command=ventana_pedidos.destroy)
    boton_cerrar.grid(row=5, column=0, columnspan=3, pady=10)


