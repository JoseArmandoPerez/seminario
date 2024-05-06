import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from PIL import Image, ImageTk
import qrcode
import os


text_carrito = None

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
    'Agua de horchata': "Bebida tradicional hecha con arroz y canela.",
    'Corona': "Cerveza tipo lager, ligera y refrescante.",
    'Modelo Especial': "Cerveza tipo pilsner de sabor robusto.",
    'Heineken': "Cerveza tipo lager con un toque amargo.",
    'Whisky': "Bebida alcohólica destilada de granos fermentados.",
    'Vodka': "Destilado originario de Rusia, neutral y versátil.",
    'Tequila': "Destilado mexicano hecho de agave azul.",
    'Vino Tinto': "Vino hecho de la fermentación de uvas negras.",
    'Vino Blanco': "Vino producido a partir de uvas blancas o de uvas negras sin piel.",
    
    'Sushi de salmón': "Sushi fresco con arroz, salmón y alga nori, servido con salsa de soja, wasabi y jengibre encurtido.",
    'Tempura de verduras': "Verduras variadas en un crujiente rebozado de tempura, servidas con salsa de soja y jengibre encurtido.",
    'Ramen de pollo': "Caldo de pollo rico y sabroso con fideos ramen, pollo, huevo, cebolleta, brotes de bambú y setas shiitake.",
    'Gyudon': "Ternera tierna cocida con cebolla en salsa de soja y dashi, servido sobre arroz.",
    'Bruschetta': "Rodajas de pan baguette tostado con tomate fresco, ajo, albahaca y un toque de vinagre balsámico.",
    'Ensalada Caprese': "Tomates maduros y mozzarella fresca con albahaca y un aliño de aceite de oliva y balsámico.",
    'Queso fundido': "Queso derretido con chorizo o champiñones, servido con tortillas de maíz o chips de tortilla.",
    'Sashimi': "Rodajas de pescado fresco como salmón o atún, servidas con wasabi y salsa de soja.",
    'Yakitori': "Brochetas de pollo marinadas en salsa yakitori y asadas, acompañadas de sake o mirin.",
    'Nigiri sushi': "Bolitas de arroz sushi cubiertas con filetes de pescado fresco, servidas con wasabi y salsa de soja.",
    'Tarta de queso': "Suave y cremosa tarta de queso sobre una base de galleta, a menudo servida con fruta fresca o coulis.",
    'Coulant de chocolate': "Pequeño pastel de chocolate con un centro líquido de chocolate fundido.",
    'Crème brûlée': "Postre francés de crema custodia con una capa superior de caramelo crujiente.",
    'Dorayaki': "Pancakes japoneses rellenos de pasta de judía roja dulce, conocido como anko.",
    'Mochi': "Pastelitos japoneses de masa de arroz glutinoso, rellenos de fresa, mango, té verde u otros sabores."
}

ingredientes = {
    'Coca-Cola': ['Con hielo', 'Sin hielo', 'Con limón'],
    'Pepsi': ['Con hielo', 'Sin hielo', 'Con limón'],
    'Fanta': ['Con hielo', 'Sin hielo'],
    'Sprite': ['Con hielo', 'Sin hielo'],
    '7 Up': ['Con hielo', 'Sin hielo'],
    'Jarritos': ['Con hielo', 'Sin hielo'],
    'Agua mineral': ['Con limón'],
    'Limonada': ['Agua natural', 'Agua mineral', 'Con azúcar', 'Con stevia', 'Con esplenda'],
    'Té helado': ['Con hielo', 'Sin hielo', 'Con azúcar', 'Con stevia', 'Con esplenda'],
    'Agua de horchata': ['Con hielo', 'Sin hielo', 'Con canela'],
    'Corona': ['Con limón', 'Con sal', 'Con clamato', 'Con salsa inglesa', 'Con salsa picante'],
    'Modelo Especial': ['Con limón', 'Con sal', 'Con clamato', 'Con salsa inglesa'],
    'Heineken': ['Con limón', 'Con sal'],
    'Whisky': ['Con hielo', 'Sin hielo', 'Con agua'],
    'Vodka': ['Con hielo', 'Sin hielo', 'Con limón', 'Con agua tónica'],
    'Tequila': ['Con sal', 'Con limón', 'Con sangrita'],
    'Vino Tinto': ['Con hielo', 'Sin hielo'],
    'Vino Blanco': ['Con hielo', 'Sin hielo', 'Con soda'],
    'Sushi de salmón': ['Arroz', 'Salmón fresco', 'Alga nori', 'Vinagre de arroz', 'Salsa de soja', 'Wasabi', 'Jengibre encurtido'],
    'Tempura de verduras': ['Verduras variadas', 'Harina', 'Huevo', 'Agua con gas', 'Salsa de soja', 'Jengibre encurtido'],
    'Ramen de pollo': ['Caldo de pollo', 'Fideos ramen', 'Pollo', 'Huevo', 'Cebolleta', 'Brotes de bambú', 'Setas shiitake'],
    'Gyudon': ['Ternera', 'Cebolla', 'Salsa de soja', 'Caldo dashi', 'Azúcar', 'Jengibre', 'Arroz'],
    'Bruschetta': ['Pan baguette', 'Ajo', 'Albahaca fresca', 'Aceite de oliva virgen', 'Vinagre balsámico', 'Sal y pimienta al gusto', 'Tomates maduros'],
    'Ensalada Caprese': ['Tomates maduros', 'Mozzarella fresca', 'Hojas de albahaca fresca', 'Aceite de oliva virgen', 'Vinagre balsámico', 'Sal y pimienta al gusto'],
    'Queso fundido': ['Queso rallado: cheddar, mozzarella, mixto', 'Chorizo', 'Champiñones', 'Tortillas de maíz o chips de tortilla para servir'],
    'Sashimi': ['Pescado fresco: salmón, atún, hamachi', 'Wasabi', 'Salsa de soja'],
    'Yakitori': ['Pollo', 'Salsa Yakitori', 'Sake o mirin', 'Salsa de soja', 'Azúcar', 'Ajo', 'Jengibre rallado'],
    'Nigiri sushi': ['Pescado', 'Arroz sushi', 'Wasabi', 'Salsa de soja', 'Azúcar', 'Jengibre encurtido'],
    'Tarta de queso': ['Queso crema', 'Azúcar', 'Huevos', 'Extracto de vainilla', 'Galletas para la base', 'Mantequilla'],
    'Coulant de chocolate': ['Chocolate negro', 'Azúcar', 'Huevos', 'Mantequilla', 'Harina'],
    'Crème brûlée': ['Crema de leche', 'Azúcar', 'Yemas de huevo', 'Vainilla'],
    'Dorayaki': ['Harina de trigo', 'Azúcar', 'Miel', 'Huevos', 'Bicarbonato de sodio', 'Agua', 'Anko'],
    'Mochi': ['Harina de arroz glutinoso', 'Azúcar', 'Agua', 'Rellenos: fresa, mango, té verde']
}


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
        if producto in ingredientes:
            cantidad = carrito.get(producto, 0)
            if cantidad > 0:
                # Crear ventana para seleccionar ingredientes por producto
                ing_window = tk.Toplevel()
                ing_window.title(f"Ingredientes para {producto}")
                ing_window.geometry("400x300")

                # Crear notebook en la ventana emergente
                notebook = ttk.Notebook(ing_window)
                notebook.pack(expand=True, fill='both')

                # Crear pestañas para cada unidad del producto
                for i in range(1, cantidad + 1):
                    tab = ttk.Frame(notebook)
                    notebook.add(tab, text=f'{producto} #{i}')

                    # Lista de ingredientes para seleccionar
                    lb = tk.Listbox(tab, selectmode='multiple')
                    lb.pack(expand=True, fill='both', padx=10, pady=10)
                    
                    # Añadir ingredientes a la lista
                    for ing in ingredientes[producto]:
                        lb.insert(tk.END, ing)

                    # Botón para guardar selección de ingredientes
                    def guardar_ingredientes(p_num, listbox, product):
                        seleccionados = [listbox.get(idx) for idx in listbox.curselection()]
                        notas[product] = notas.get(product, {})
                        notas[product][p_num] = seleccionados
                        actualizar_carrito()
                        ing_window.destroy()

                    guardar_btn = tk.Button(tab, text="Guardar", command=lambda lb=lb, p_num=i: guardar_ingredientes(p_num, lb, producto))
                    guardar_btn.pack(pady=10)

                ing_window.mainloop()
            else:
                messagebox.showinfo("Información", f"No hay {producto} en el carrito para añadir ingredientes.")
        else:
            messagebox.showinfo("Información", f"No hay ingredientes predefinidos para {producto}")



    def actualizar_carrito():
        texto_carrito = "Carrito:\n"
        for prod, cant in carrito.items():
            texto_carrito += f"{prod}: {cant}"
            if prod in notas:
                texto_carrito += " (" + " / ".join(f"{ing}: {cant_ing}" for ing, cant_ing in notas[prod].items()) + ")"
            texto_carrito += "\n"
        label_carrito.config(text=texto_carrito)


    def crear_boton_bebida(nombre, descripcion, frame, col, row):
        bebida_frame = tk.Frame(frame, bd=2, relief="groove", padx=5, pady=5, bg='#F7C898')  # Fondo rojo pastel para los recuadros
        bebida_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew", ipadx=10, ipady=10)

        # Cargar imagen
        ruta_imagen = os.path.join(os.path.dirname(__file__), 'imagenes', 'rammen.png')
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

        label_nombre = tk.Label(bebida_frame, text=nombre, font=("Helvetica", 12, "bold"), bg='#F7C898', fg='black')
        label_nombre.pack(side="top")

        # Ajuste de la descripción para evitar el corte de texto
        label_descripcion = tk.Label(bebida_frame, text=descripcion, font=("Helvetica", 10), bg='#F7C898', fg='black', wraplength=180)  # Ajusta el wraplength según necesario
        label_descripcion.pack(side="top")

        boton_aumentar = tk.Button(bebida_frame, text="Añadir", command=lambda: agregar_al_carrito(nombre), bg='#C2F798', fg='black')  # Botón verde
        boton_aumentar.pack(side="left", padx=10)

        boton_disminuir = tk.Button(bebida_frame, text="Quitar", command=lambda: agregar_al_carrito(nombre, -1), bg='#F57682', fg='black')  # Botón rojo
        boton_disminuir.pack(side="right", padx=10)

        boton_nota = tk.Button(bebida_frame, text="Agregar Ing", command=lambda: agregar_ingrediente(nombre), bg='#F5D276', fg='black')  # Botón para ingredientes
        boton_nota.pack(side="bottom", pady=5)

    col = 0
    row = 0
    for nombre, descripcion in bebidas.items():
        crear_boton_bebida(nombre, descripcion, scrollable_frame, col, row)
        col += 1
        if col == 4:
            col = 0
            row += 1

    cart_frame = tk.Frame(main_frame, bd=2, relief="sunken", padx=5, pady=5)
    cart_frame.pack(side="right", fill="y")

    label_carrito = tk.Label(cart_frame, text="Carrito:", bg='#FFDAB9', fg='black')
    label_carrito.pack(side="top", fill="x")


    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="left", fill="y")

    def generar_y_mostrar_qr():
        info = []
        for producto, cantidad in carrito.items():
            detalles = f"{producto}: {cantidad}"
            if producto in notas:
                detalles_notas = []
                for num_item, lista_notas in notas[producto].items():
                    # Cada nota se presenta con el formato 'Producto índice: notas'
                    detalles_notas.append(f"{producto} {num_item}: {', '.join(map(str, lista_notas))}")
                detalles += " Notas: " + "; ".join(detalles_notas)
            info.append(detalles)

        info_qr = "\n".join(info)
        qr = qrcode.make(info_qr)
        qr_image = ImageTk.PhotoImage(image=qr)
        qr_window = tk.Toplevel(ventana_pedidos)
        qr_window.title("Código QR del Pedido")
        label = tk.Label(qr_window, image=qr_image)
        label.image = qr_image  # Guardar una referencia
        label.pack()
        qr_window.mainloop()


    # Botón para generar el código QR
    boton_confirmar = tk.Button(cart_frame, text="Generar QR del Pedido", command=generar_y_mostrar_qr, bg='#FFFF00', fg='black')
    boton_confirmar.pack(side="top", pady=10)

    # Packing del canvas y scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="left", fill="y")

if __name__ == "__main__":
    root = tk.Tk()
    tk.Button(root, text="Abrir Ventana de Pedidos", command=abrir_ventana_pedidos).pack()
    root.mainloop()