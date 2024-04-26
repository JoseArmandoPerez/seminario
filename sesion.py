import tkinter as tk
import tkinter.messagebox as messagebox
import requests
import json

# Define las variables de entrada como globales
name_entry = None
email_entry = None
password_entry = None
tipo_sesion = None

def guardar_estado_usuario(usuario_iniciado, nombre_usuario, id_usuario):
    with open('config.json', 'w') as f:
        # Guarda el estado del usuario en un archivo JSON
        json.dump({'usuario_iniciado': usuario_iniciado, 'nombre_usuario': nombre_usuario, 'id_usuario': id_usuario}, f)

def iniciar_sesion():
    # Crea la ventana
    window = tk.Tk()
    window.title("Inicio de Sesión")
    sign_in(window)


def sign_in(window):
    # Marco para contener los widgets
    frame = tk.Frame(window, padx=10, pady=10)
    frame.pack()

    # Etiqueta y campo de entrada para el correo electrónico
    email_label = tk.Label(frame, text="Email:")
    email_label.grid(row=0, column=0, sticky="w", pady=5)
    email_entry = tk.Entry(frame)
    email_entry.grid(row=0, column=1, padx=5, pady=5)

    # Etiqueta y campo de entrada para la contraseña
    password_label = tk.Label(frame, text="Password:")
    password_label.grid(row=1, column=0, sticky="w", pady=5)
    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    # Botón de inicio de sesión
    button = tk.Button(frame, text="Iniciar sesión", command=lambda: validate_credentials(email_entry, password_entry, window))
    button.grid(row=2, column=1, pady=5, padx=5)

    # botón para crear una cuenta si no la tiene
    create_account_button = tk.Button(frame, text="Crear cuenta", command=lambda: sign_up(window))
    create_account_button.grid(row=3, column=1, pady=5, padx=5)


def validate_credentials(email_entry, password_entry, window):
    email = email_entry.get()
    password = password_entry.get()
    if email == "" or password == "":
        messagebox.showerror("Sign In", "Please enter email and password.")
        return
    else:
        data = {'email': email, 'password': password}
        response = requests.post('http://192.168.100.89:5000/login', json=data)  # Define la variable `response` aquí
    if response.status_code == 200:
        # Obtenemos la información del usuario
        datos_usuario = response.json()
        id_usuario = datos_usuario["id"]
        nombre = datos_usuario["nombre"]
        tipo_sesion = datos_usuario["tipo_sesion"]

        # Guardamos el estado del usuario
        guardar_estado_usuario(True, nombre, id_usuario)

        # Mostramos el mensaje de bienvenida
        messagebox.showinfo("Sign In", f"Bienvenido, {nombre}! Tipo de sesión: {tipo_sesion}")
        window.after(2000, window.destroy)
        return
    else:
        # Mostramos un mensaje de error
        messagebox.showerror("Error", "Correo electrónico o contraseña incorrectos.")
        window.after(2000, window.destroy)

def sign_up(window):
    global name_entry, email_entry, password_entry  # Declara las variables globales
    
    window.destroy()
    window = tk.Tk()  # Crea una nueva ventana
    window.title("Create Account")
    
    # Marco para contener los widgets
    frame = tk.Frame(window, padx=20, pady=10)
    frame.pack()
    
    # Etiqueta y campo de entrada para el nombre
    name_label = tk.Label(frame, text="Name:")
    name_label.grid(row=0, column=0, sticky="w", pady=5)
    name_entry = tk.Entry(frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    
    # Etiqueta y campo de entrada para el correo electrónico
    email_label = tk.Label(frame, text="Email:")
    email_label.grid(row=1, column=0, sticky="w", pady=5)
    email_entry = tk.Entry(frame)
    email_entry.grid(row=1, column=1, padx=5, pady=5)
    
    # Etiqueta y campo de entrada para la contraseña
    password_label = tk.Label(frame, text="Password:")
    password_label.grid(row=2, column=0, sticky="w", pady=5)
    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=2, column=1, padx=5, pady=5)
    
    button_create = tk.Button(frame, text="Create Account", command=lambda: create_account(window))
    button_create.grid(row=3, column=1, pady=5, padx=5)

def create_account(window):
    # Accede a las variables globales
    global name_entry, email_entry, password_entry  
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    data = {'nombre': name, 'email': email, 'password': password}
    response = requests.post('http://192.168.100.89:5000/crear_usuario', json=data)
    if response.status_code == 201:
        messagebox.showinfo("Create Account", response.json()['message'])
    else:
        messagebox.showerror("Create Account", "Failed to create account.")
    
    # Cerrar la ventana (o realizar cualquier otra acción necesaria)
    window.destroy()
