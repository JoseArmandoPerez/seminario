import tkinter as tk
import json
from tkinter import messagebox

import requests

button_colors = ["green"] * 15
buttons = []  # Define the "buttons" list

def button_pressed(button_number):
    if button_colors[button_number] == "green":
        with open('usuario.json', 'r') as file:
            data = json.load(file)
            id = data['id']
            nombre = data['nombre']
        print(f"Button {button_number + 1} pressed")
        button_colors[button_number] = "red"
        buttons[button_number].config(bg="red", fg="white")  # Cambiar tanto el fondo como el color del texto
        buttons[button_number].config(text=f"Mesa {button_number + 1}\n{nombre}")
        buttons[button_number].config(state=tk.DISABLED)
        # Deshabilitar todos los botones
        for button in buttons:
            button.config(state=tk.DISABLED)
        mandar_a_base(nombre, id, button_number + 1)

        
def mesas_ventana():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Mesas Disponibles")
    nueva_ventana.attributes('-fullscreen', True)

    for i in range(15):
        button = tk.Button(nueva_ventana, text=f"Mesa {i + 1}", bg="green", width=15, height=5, font=("Helvetica", 14), command=lambda i=i: button_pressed(i))
        button.grid(row=i // 5, column=i % 5, padx=80, pady=80)
        if verificar_mesa(i + 1):
            button.config(state=tk.DISABLED)
            button.config(bg="red", fg="white")
            button.config(text=f"Mesa {i + 1}\nOcupada")
        buttons.append(button)
        
    boton = tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy)
    boton.grid(row=3, column=2, pady=20)
    
def mandar_a_base(nombre, id, mesa):
    IP = 'http://192.168.100.89:5000'
    # Guarda nombre, id y mesa en data
    data = {'nombre': nombre, 'id': id, 'mesa': mesa}
   
    # Usar IP para la dirección del servidor
    response = requests.post(f'{IP}/registrarmesa', json=data)

    if response.status_code == 201:
        # Si se registró la mesa, muestra un mensaje de éxito
        messagebox.showinfo("Registro de Mesa", "¡Mesa registrada con éxito!")
    else:
        # Si falla el registro de la mesa, muestra un mensaje de error
        messagebox.showerror("Registro de Mesa", "Error al registrar la mesa.")
        
def verificar_mesa(mesa):
    IP = 'http://192.168.100.89:5000'
    data = {'mesa': mesa}
    response = requests.post(f'{IP}/verificar_mesa', json=data)
    if response.status_code == 200:
        return True
    else:
        return False