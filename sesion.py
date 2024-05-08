import json
import tkinter as tk
from tkinter import messagebox
import requests

IP = 'http://192.168.100.89:5000'

def iniciar_sesion_cliente(nombre):
    # Realiza la lógica de inicio de sesión para el cliente con el nombre proporcionado
    data = {'nombre': nombre}
    # Usar IP para la dirección del servidor
    response = requests.post(f'{IP}/loginusuario', json=data)
    
    # extraer los datos del return
    data = response.json()
    data = {'id': data['id'], 'nombre': data['nombre'], 'tipo_usuario': 'cliente'}
    # Guardar id y nombre de usuario en usuario.json
    with open('usuario.json', 'w') as file:
        json.dump(data, file)
        

    if response.status_code == 200:
        # Si el inicio de sesión es exitoso, muestra un mensaje de éxito
        messagebox.showinfo("Inicio de Sesión", "¡Inicio de sesión exitoso!")
    else:
        # Si el inicio de sesión falla, muestra un mensaje de error
        messagebox.showerror("Inicio de Sesión", "Error al iniciar sesión.")

def iniciar_sesion_otro(nombre, password, tipo_usuario):
    # Realiza la lógica de inicio de sesión para el chef con el nombre y contraseña proporcionados
    data = {'nombre': nombre, 'password': password, 'tipo_usuario': tipo_usuario}
    response = requests.post(f'{IP}/loginotro', json=data)

    # extraer los datos del return
    data = response.json()
    data = {'id': data['id'], 'nombre': data['nombre'], 'tipo_usuario': tipo_usuario}
    
    # Guardar id y nombre de usuario en usuario.json
    with open('usuario.json', 'w') as file:
        json.dump(data, file)
    
    if response.status_code == 200:
        messagebox.showinfo("Inicio de Sesión", "¡Inicio de sesión exitoso!")
    else:
        messagebox.showerror("Inicio de Sesión", "Error al iniciar sesión.")
    pass


def iniciar_sesion():
    # Crea la ventana
    window = tk.Tk()
    window.title("Inicio de Sesión")
    sign_in(window)

def sign_in(window):
    # Marco para contener los widgets
    frame = tk.Frame(window, padx=10, pady=10)
    frame.pack()

    # Etiqueta y campo de entrada para el nombre de usuario
    name_label = tk.Label(frame, text="Nombre:")
    name_label.grid(row=0, column=0, sticky="w", pady=5)
    name_entry = tk.Entry(frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    # Botón de inicio de sesión
    button = tk.Button(frame, text="Iniciar sesión", command=lambda: iniciar_sesion_cliente(name_entry.get()))
    button.grid(row=1, columnspan=2, pady=5, padx=5)

if __name__ == "__main__":
    iniciar_sesion()
