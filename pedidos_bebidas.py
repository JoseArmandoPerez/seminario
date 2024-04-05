import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import qrcode

# Listas de bebidas como en el ejemplo anterior
refrescos = ['Coca-Cola', 'Pepsi', 'Fanta', 'Sprite', '7 Up', 'Jarritos', 'Agua mineral', 'Limonada', 'Té helado', 'Agua de horchata']
bebidas_alcoholicas = ['Cerveza Modelo', 'Cerveza Corona', 'Vino tinto', 'Vino blanco', 'Margarita', 'Mojito', 'Tequila', 'Ron', 'Whisky', 'Mezcal']

def abrir_ventana_pedidos():
    ventana_pedidos = tk.Toplevel()
    ventana_pedidos.title("Pedidos de Bebidas")
    
    carrito = {}
    notas = {}

    def actualizar_carrito():
        texto_carrito = "Carrito:\n"
        for producto, detalles in carrito.items():
            texto = f"{producto}: {detalles['cantidad']}"
            if producto in notas:
                texto += f" ({notas[producto]})"
            texto_carrito += texto + "\n"
        label_carrito.config(text=texto_carrito)

    def agregar_al_carrito(producto):
        if producto in carrito:
            carrito[producto]['cantidad'] += 1
        else:
            carrito[producto] = {'cantidad': 1}
        actualizar_carrito()

    def reducir_cantidad(producto):
        if producto in carrito:
            if carrito[producto]['cantidad'] > 1:
                carrito[producto]['cantidad'] -= 1
            else:
                del carrito[producto]
                if producto in notas:
                    del notas[producto]
        actualizar_carrito()

    def agregar_nota(producto):
        nota = simpledialog.askstring("Nota para " + producto, "Especifique la nota para este producto:")
        if nota:
            notas[producto] = nota
        actualizar_carrito()

    def generar_y_mostrar_qr():
        pedido_info = "Pedido:\n"
        for producto, detalles in carrito.items():
            texto = f"{producto}: {detalles['cantidad']}"
            if producto in notas:
                texto += f" - Nota: {notas[producto]}"
            pedido_info += texto + "\n"
        
        qr = qrcode.make(pedido_info)
        qr_img = ImageTk.PhotoImage(qr)
        ventana_qr = tk.Toplevel(ventana_pedidos)
        ventana_qr.title("Código QR del Pedido")
        label_qr = tk.Label(ventana_qr, image=qr_img)
        label_qr.image = qr_img  # keep a reference!
        label_qr.pack()

    def crear_botones_bebida(frame, bebidas, columna):
        for i, bebida in enumerate(bebidas):
            tk.Button(frame, text=bebida, command=lambda bebida=bebida: agregar_al_carrito(bebida)).grid(row=i, column=columna, sticky='ew')
            tk.Button(frame, text=f'Reducir {bebida}', command=lambda bebida=bebida: reducir_cantidad(bebida)).grid(row=i, column=columna+1, sticky='ew')
            tk.Button(frame, text=f'Nota {bebida}', command=lambda bebida=bebida: agregar_nota(bebida)).grid(row=i, column=columna+2, sticky='ew')

    # Creación de los marcos y botones de bebidas
    frame_refrescos = tk.LabelFrame(ventana_pedidos, text="Refrescos")
    frame_refrescos.pack(fill="both", expand="yes")
    crear_botones_bebida(frame_refrescos, refrescos, 0)

    frame_bebidas_alcoholicas = tk.LabelFrame(ventana_pedidos, text="Bebidas Alcohólicas")
    frame_bebidas_alcoholicas.pack(fill="both", expand="yes", pady=10)
    crear_botones_bebida(frame_bebidas_alcoholicas, bebidas_alcoholicas, 0)

    # Etiqueta y botón para confirmación y generación del QR
    label_carrito = tk.Label(ventana_pedidos, text="Carrito:\n", justify='left')
    label_carrito.pack(fill="both", expand="yes")

    boton_confirmar = tk.Button(ventana_pedidos, text="Generar QR del Pedido", command=generar_y_mostrar_qr)
    boton_confirmar.pack(pady=10)



