import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import qrcode

# Lista de platos principales y sus ingredientes
platos_principales = {
    'Sushi de salmón': ['Arroz', 'Salmón fresco', 'Alga nori', 'Vinagre de arroz', 'Salsa de soja', 'Wasabi', 'Jengibre encurtido'],
    'Tempura de verduras': ['Verduras variadas', 'Harina', 'Huevo', 'Agua con gas', 'Salsa de soja', 'Jengibre encurtido'],
    'Ramen de pollo': ['Caldo de pollo', 'Fideos ramen', 'Pollo', 'Huevo', 'Cebolleta', 'Brotes de bambú', 'Setas shiitake'],
    'Gyudon': ['Ternera', 'Cebolla', 'Salsa de soja', 'Caldo dashi', 'Azúcar', 'Jengibre', 'Arroz'],
}

def abrir_ventana_ingredientes(plato):
    ventana_ingredientes = tk.Toplevel()
    ventana_ingredientes.title(f"Ingredientes para {plato}")
    
    ingredientes_seleccionados = []

    def agregar_ingrediente(ingrediente):
        if ingrediente not in ingredientes_seleccionados:
            ingredientes_seleccionados.append(ingrediente)

    def finalizar_seleccion():
        if ingredientes_seleccionados:
            agregar_al_carrito(plato, ingredientes_seleccionados)
            ventana_ingredientes.destroy()
        else:
            messagebox.showwarning("Sin Ingredientes", "Por favor, seleccione al menos un ingrediente.")

    label_titulo = tk.Label(ventana_ingredientes, text=f"Seleccione los ingredientes para {plato}:", font=("Helvetica", 14, "bold"))
    label_titulo.pack(pady=10)

    lista_ingredientes = tk.Listbox(ventana_ingredientes, selectmode=tk.MULTIPLE, font=("Helvetica", 12))
    lista_ingredientes.pack(fill=tk.BOTH, expand=True)

    for ingrediente in platos_principales[plato]:
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

def agregar_al_carrito(plato, ingredientes_seleccionados):
    mensaje = f"Plato: {plato}\nIngredientes: "
    if ingredientes_seleccionados:
        mensaje += ", ".join(ingredientes_seleccionados)
    else:
        mensaje += "Ninguno"
    messagebox.showinfo("Plato Agregado", mensaje)

def abrir_ventana_pedidos_comida():
    ventana_pedidos = tk.Toplevel()
    ventana_pedidos.title("Pedidos de Comida Japonesa")
    
    # Creación de los marcos y botones de platos
    frame_platos_principales = tk.LabelFrame(ventana_pedidos, text="Platos Principales", font=("Helvetica", 16, "bold"))
    frame_platos_principales.pack(fill="both", expand="yes", padx=20, pady=20)
    for plato in platos_principales.keys():
        tk.Button(frame_platos_principales, text=plato, command=lambda plato=plato: abrir_ventana_ingredientes(plato), font=("Helvetica", 14), bg="blue", fg="white").pack(pady=5, padx=10)

def main():
    root = tk.Tk()
    app = abrir_ventana_pedidos_comida()
    root.mainloop()

if __name__ == "__main__":
    main()
