import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import qrcode
from PIL import Image, ImageTk

import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import qrcode
import json
from PIL import Image, ImageTk

# Función para cargar datos desde un archivo JSON
def cargar_datos(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Cargar los datos de bebidas e ingredientes
datos = cargar_datos('RegistroPlatillos.json')
bebidas = datos['bebidas']
platos_principales = datos['platos_principales']
platos_entradas = datos['platos_entradas']
platos_postres = datos['platos_postres']

# Lista para almacenar los pedidos realizados
pedidos = []



# Lista para almacenar los pedidos realizados
pedidos = []

def abrir_ventana_bebidas(bebida):
    ventana_bebidas = tk.Toplevel()
    ventana_bebidas.title(f"Variantes para {bebida}")

    for variante in bebidas[bebida]:
        tk.Button(ventana_bebidas, text=variante, command=lambda variante=variante: agregar_bebida(f"{bebida} - {variante}"), font=("Helvetica", 14), bg="#F7C898", fg="#000000").pack(pady=5, padx=10, fill="both", expand=True)

def abrir_ventana_ingredientes(plato, bebida, tipo):
    ventana_ingredientes = tk.Toplevel()
    ventana_ingredientes.title(f"Ingredientes para {plato}, {bebida}")

    platos = platos_principales
    if tipo == "Entradas":
        platos = platos_entradas
    elif tipo == "Postres":
        platos = platos_postres       

    ingredientes_seleccionados = []

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

    boton_agregar = tk.Button(ventana_ingredientes, text="Finalizar Selección", command=finalizar_seleccion, font=("Helvetica", 14, "bold"))
    boton_agregar.pack(pady=10)

def agregar_bebida(bebida):
    pedidos.append(f"Bebida: {bebida}")
    actualizar_contador()

def finalizar_seleccion(plato, ingredientes_seleccionados):
    if ingredientes_seleccionados:
        mensaje = f"Plato: {plato}\nIngredientes: "
        mensaje += ", ".join(ingredientes_seleccionados)
        pedidos.append(mensaje)
        actualizar_contador()
    else:
        messagebox.showwarning("Sin Ingredientes", "Por favor, seleccione al menos un ingrediente.")

def actualizar_contador():
    label_carrito.config(text=f"Carrito: {len(pedidos)}")

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

def limpiar_pedidos():  
    pedidos.clear()
    actualizar_contador()
    messagebox.showinfo("Pedidos Limpiados", "La lista de pedidos ha sido limpiada.")

def enviar_pedidos():
    if not pedidos:
        messagebox.showwarning("Sin Pedidos", "No hay pedidos para enviar.")
    else:
        qr_data = "\n".join(pedidos)
        qr = qrcode.make(qr_data)

        ventana_qr = tk.Toplevel()
        ventana_qr.title("Código QR de Pedidos")

        qr_image = ImageTk.PhotoImage(qr)

        qr_label = tk.Label(ventana_qr, image=qr_image)
        qr_label.image = qr_image
        qr_label.pack(padx=20, pady=20)

        qr_image_path = "pedido_qr.png"
        qr.save(qr_image_path)
        messagebox.showinfo("Código QR Generado", f"El código QR de los pedidos ha sido generado y guardado como {qr_image_path}.")

def abrir_ventana_pedidos_comida():
    ventana_pedidos = tk.Toplevel()
    ventana_pedidos.title("Pedidos de Comida Japonesa")

    notebook = ttk.Notebook(ventana_pedidos)
    notebook.pack(fill=tk.BOTH, expand=True)

    frame_platos_principales = tk.Frame(notebook)
    frame_platos_entradas = tk.Frame(notebook)
    frame_platos_postres = tk.Frame(notebook)
    frame_bebidas = tk.Frame(notebook)

    notebook.add(frame_platos_principales, text="Platos Principales")
    notebook.add(frame_platos_entradas, text="Entradas")
    notebook.add(frame_platos_postres, text="Postres")
    notebook.add(frame_bebidas, text="Bebidas")

    for plato in platos_principales.keys():
        tk.Button(frame_platos_principales, text=plato, command=lambda plato=plato: abrir_ventana_ingredientes(plato, "Principales", "Platos Principales"), font=("Helvetica", 14), bg="#F7C898", fg="#000000").pack(pady=5, padx=10, fill="both", expand=True)

    for plato in platos_entradas.keys():
        tk.Button(frame_platos_entradas, text=plato, command=lambda plato=plato: abrir_ventana_ingredientes(plato, "Entradas", "Entradas"), font=("Helvetica", 14), bg="#F7C898", fg="#000000").pack(pady=5, padx=10, fill="both", expand=True)

    for plato in platos_postres.keys():
        tk.Button(frame_platos_postres, text=plato, command=lambda plato=plato: abrir_ventana_ingredientes(plato, "Postres", "Postres"), font=("Helvetica", 14), bg="#F7C898", fg="#000000").pack(pady=5, padx=10, fill="both", expand=True)
    
    row_index = 0
    col_index = 0
    for bebida in bebidas.keys():
        tk.Button(frame_bebidas, text=bebida, command=lambda bebida=bebida: abrir_ventana_bebidas(bebida), font=("Helvetica", 14), bg="#F7C898", fg="#000000").grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")
        col_index += 1
        if col_index == 3:
            col_index = 0
            row_index += 1

    carrito_texto = tk.StringVar()  
    label_carrito = tk.Label(ventana_pedidos, textvariable=carrito_texto, font=("Helvetica", 14))
    label_carrito.pack()

    tk.Button(ventana_pedidos, text="Ver Pedidos", command=ver_pedidos, font=("Helvetica", 14), bg="#8B4513", fg="#FFFAF0").pack(pady=10)
    tk.Button(ventana_pedidos, text="Limpiar Pedidos", command=limpiar_pedidos, font=("Helvetica", 14), bg="#8B4513", fg="#FFFAF0").pack(pady=10)
    tk.Button(ventana_pedidos, text="Enviar Pedidos", command=enviar_pedidos, font=("Helvetica", 14), bg="#8B4513", fg="#FFFAF0").pack(pady=10)

    return ventana_pedidos

def main():
    root = tk.Tk()
    app = abrir_ventana_pedidos_comida()
    root.mainloop()

if __name__ == "__main__":
    main()
