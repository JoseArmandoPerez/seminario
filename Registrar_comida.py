import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

# Lista de platos principales y sus ingredientes
platos_principales = {
    'Sushi de salmón': ['Arroz', 'Salmón fresco', 'Alga nori', 'Vinagre de arroz', 'Salsa de soja', 'Wasabi', 'Jengibre encurtido'],
    'Tempura de verduras': ['Verduras variadas', 'Harina', 'Huevo', 'Agua con gas', 'Salsa de soja', 'Jengibre encurtido'],
    'Ramen de pollo': ['Caldo de pollo', 'Fideos ramen', 'Pollo', 'Huevo', 'Cebolleta', 'Brotes de bambú', 'Setas shiitake'],
    'Gyudon': ['Ternera', 'Cebolla', 'Salsa de soja', 'Caldo dashi', 'Azúcar', 'Jengibre', 'Arroz'],
}

# Lista de platos de entradas y sus ingredientes
platos_entradas ={
    'Bruschetta': ['Pan baguette','Ajo','Albahaca fresca','Aceite de oliva virgen', 'Vinagre balsámico','Sal y pimienta al gusto','Tomates maduros'],
    'Ensalada Caprese': ['Tomates maduros','Mozzarella fresca','Hojas de albahaca fresca','Aceite de oliva virgen', 'Vinagre balsámico','Sal y pimienta al gusto','Tomates maduros'],
    'Queso fundido': ['Queso rallado: cheddar, mozzarella, mixto','Chorizo, champiñones','Tortillas de maíz o chips de tortilla para servir'],
    'Sashimi': ['Pescado fresco: salmón, atún, hamachi (pez limón), vieira','Wasabi','Salsa de soja'],
    'Yakitori': ['Pollo','Salsa Yakitori','Sake o mirin','Salsa de soja','Azúcar','Ajo','Jengibre rallado'],
    'Nigiri sushi': ['Pescado','Arroz sushi','Wasabi','Salsa de soja','Azúcar','Jengibre encurtido']
}

# Lista de platos de postres y sus ingredientes
platos_postres = {
    'Tarta de queso': ['Queso crema','Azúcar','Huevos','Extracto de vainilla', 'Galletas para la base','Mantequilla'],
    'Coulant de chocolate': ['Chocolate negro','Azúcar','Huevos','Mantequilla', 'Harina'],
    'Crème brûlée': ['Crema de leche','Azúcar','Yemas de huevo','Vainilla'],
    'Dorayaki': ['Harina de trigo','Azúcar','Miel','Huevos','Bicarbonato de sodio','Agua','Anko'],
    'Mochi': ['Harina de arroz glutinoso','Azúcar','Agua','Rellenos: fresa, mango, té verde']
}

# Lista para almacenar los pedidos realizados
pedidos = []

def abrir_ventana_ingredientes(plato, tipo):
    ventana_ingredientes = tk.Toplevel()
    ventana_ingredientes.title(f"Ingredientes para {plato}")

    platos = platos_principales
    if tipo == "Entradas":
        platos = platos_entradas
    elif tipo == "Postres":
        platos = platos_postres
    
    ingredientes_seleccionados = []

    def agregar_ingrediente(ingrediente):
        if ingrediente not in ingredientes_seleccionados:
            ingredientes_seleccionados.append(ingrediente)

    def finalizar_seleccion():
        if ingredientes_seleccionados:
            agregar_al_carrito(plato, ingredientes_seleccionados)
            ventana_ingredientes.destroy()
            actualizar_contador()  # Actualizar contador de pedidos
        else:
            messagebox.showwarning("Sin Ingredientes", "Por favor, seleccione al menos un ingrediente.")

    label_titulo = tk.Label(ventana_ingredientes, text=f"Seleccione los ingredientes para {plato}:", font=("Helvetica", 14, "bold"))
    label_titulo.pack(pady=10)

    lista_ingredientes = tk.Listbox(ventana_ingredientes, selectmode=tk.MULTIPLE, font=("Helvetica", 12))
    lista_ingredientes.pack(fill=tk.BOTH, expand=True)

    for ingrediente in platos[plato]:
        lista_ingredientes.insert(tk.END, ingrediente)

    def on_select(event):
        # Obtener los índices de los elementos seleccionados
        selected_indices = lista_ingredientes.curselection()
        # Obtener los elementos seleccionados
        selected_ingredients = [lista_ingredientes.get(index) for index in selected_indices]
        # Actualizar la lista de ingredientes seleccionados
        ingredientes_seleccionados.clear()
        for ingredient in selected_ingredients:
            ingredientes_seleccionados.append(ingredient)

    lista_ingredientes.bind("<<ListboxSelect>>", on_select)

    boton_agregar = tk.Button(ventana_ingredientes, text="Finalizar Selección", command=finalizar_seleccion, font=("Helvetica", 14, "bold"), bg="green", fg="white")
    boton_agregar.pack(pady=10)

    # Funcionalidad del carrito
    label_carrito = tk.Label(ventana_ingredientes, text="Carrito:", font=("Helvetica", 12, "bold"))
    label_carrito.pack(pady=10)

    def agregar_al_carrito(plato, ingredientes_seleccionados):
        mensaje = f"Plato: {plato}\nIngredientes: "
        if ingredientes_seleccionados:
            mensaje += ", ".join(ingredientes_seleccionados)
        else:
            mensaje += "Ninguno"
        pedidos.append(mensaje)
        actualizar_contador()

    def actualizar_contador():
        label_carrito.config(text=f"Carrito: {len(pedidos)}")

    # Actualizar el contador inicialmente
    actualizar_contador()


    def agregar_al_carrito(plato, ingredientes_seleccionados):
        mensaje = f"Plato: {plato}\nIngredientes: "
        if ingredientes_seleccionados:
            mensaje += ", ".join(ingredientes_seleccionados)
        else:
            mensaje += "Ninguno"
        pedidos.append(mensaje)
        actualizar_contador()  # Agregar esta línea para actualizar el carrito


def ver_pedidos():
    ventana_ver_pedidos = tk.Toplevel()
    ventana_ver_pedidos.title("Lista de Pedidos")

    if not pedidos:
        label_vacio = tk.Label(ventana_ver_pedidos, text="No se han realizado pedidos aún.", font=("Helvetica", 14))
        label_vacio.pack(padx=20, pady=20)
    else:
        for pedido in pedidos:
            label_pedido = tk.Label(ventana_ver_pedidos, text=pedido, font=("Helvetica", 12))
            label_pedido.pack(padx=20, pady=5)

def limpiar_pedidos(label_contador):  # Pasar la etiqueta como argumento
    pedidos.clear()
    actualizar_contador(label_contador)  # Actualizar el contador después de limpiar los pedidos
    messagebox.showinfo("Pedidos Limpiados", "La lista de pedidos ha sido limpiada.")

def enviar_pedidos():
    if not pedidos:
        messagebox.showwarning("Sin Pedidos", "No hay pedidos para enviar.")
    else:
        # Aquí agregaría el código para enviar los pedidos, por ejemplo, a través de una API, correo electrónico, etc.
        messagebox.showinfo("Pedidos Enviados", "Los pedidos han sido enviados correctamente.")

def abrir_ventana_pedidos_comida():
    ventana_pedidos = tk.Toplevel()
    ventana_pedidos.title("Pedidos de Comida Japonesa")

    # Creación de pestañas para platos principales, entradas y postres
    notebook = ttk.Notebook(ventana_pedidos)
    notebook.pack(fill=tk.BOTH, expand=True)

    frame_platos_principales = tk.Frame(notebook)
    frame_platos_entradas = tk.Frame(notebook)
    frame_platos_postres = tk.Frame(notebook)

    notebook.add(frame_platos_principales, text="Platos Principales")
    notebook.add(frame_platos_entradas, text="Entradas")
    notebook.add(frame_platos_postres, text="Postres")

    # Botones de platos principales
    for plato in platos_principales.keys():
        tk.Button(frame_platos_principales, text=plato, command=lambda plato=plato: abrir_ventana_ingredientes(plato, "Principales"), font=("Helvetica", 14), bg="blue", fg="white").pack(pady=5, padx=10)

    # Botones de entradas
    for plato in platos_entradas.keys():
        tk.Button(frame_platos_entradas, text=plato, command=lambda plato=plato: abrir_ventana_ingredientes(plato, "Entradas"), font=("Helvetica", 14), bg="green", fg="white").pack(pady=5, padx=10)

    # Botones de postres
    for plato in platos_postres.keys():
        tk.Button(frame_platos_postres, text=plato, command=lambda plato=plato: abrir_ventana_ingredientes(plato, "Postres"), font=("Helvetica", 14), bg="orange", fg="white").pack(pady=5, padx=10)

    # Visualización del carrito
    carrito_texto = tk.StringVar()  # Variable para almacenar el texto del carrito
    label_carrito = tk.Label(ventana_pedidos, textvariable=carrito_texto, font=("Helvetica", 14))
    label_carrito.pack()

    # Función para actualizar el carrito
    def actualizar_carrito():
        texto_carrito = "Carrito:\n" + "\n".join(pedidos)
        carrito_texto.set(texto_carrito)  # Actualizar el texto del carrito

    # Botones para ver resumen de pedidos y limpiar la lista
    label_contador = tk.Label(ventana_pedidos)  # Etiqueta para el contador de pedidos
    label_contador.pack()
    tk.Button(ventana_pedidos, text="Ver Pedidos", command=ver_pedidos, font=("Helvetica", 14), bg="gray", fg="white").pack(pady=10)
    tk.Button(ventana_pedidos, text="Limpiar Pedidos", command=lambda: limpiar_pedidos(label_contador), font=("Helvetica", 14), bg="red", fg="white").pack(pady=10)
    tk.Button(ventana_pedidos, text="Enviar Pedidos", command=enviar_pedidos, font=("Helvetica", 14), bg="green", fg="white").pack(pady=10)


    return ventana_pedidos




def actualizar_contador(label_contador):  # Pasar la etiqueta como argumento
    label_contador.config(text=f"Pedidos: {len(pedidos)}")

def main():
    root = tk.Tk()
    app = abrir_ventana_pedidos_comida()
    root.mainloop()

if __name__ == "__main__":
    main()
