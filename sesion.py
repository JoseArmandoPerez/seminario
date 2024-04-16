import tkinter as tk
import tkinter.messagebox as messagebox
import sqlite3

# Define las variables de entrada como globales
name_entry = None
email_entry = None
password_entry = None
tipo_sesion = None

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
    button = tk.Button(frame, text="Iniciar sesión", command=validate_credentials)
    button.grid(row=2, column=1, pady=5, padx=5)
    
    # botón para crear una cuenta si no la tiene
    create_account_button = tk.Button(frame, text="Crear cuenta", command=lambda: sign_up(window))
    create_account_button.grid(row=3, column=1, pady=5, padx=5)

def validate_credentials():
    global email_entry, password_entry
    email = email_entry.get()
    password = password_entry.get()
    if email == "" or password == "":
        messagebox.showerror("Sign In", "Please enter email and password.")
        return
    elif email == "admin" and password == "adm1n":
        messagebox.showinfo("Sign In", "Welcome, Admin!")
        tipo_sesion = "admin"
        return "admin"
    elif email == "juan@gmail.com" and password == "1234":
        messagebox.showinfo("Sign In", "Welcome, User!")
        tipo_sesion = "user"
        return "user"

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

    # Guardar el usuario en una base de datos SQLite
    # Conexión a la base de datos
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Insertar el usuario en la base de datos
    cursor.execute("INSERT INTO usuario (nombre, email, password) VALUES (?, ?, ?)", (name, email, password))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()
    
    # Mensaje de éxito
    messagebox.showinfo("Create Account", "Account created successfully.")
    
    # Cerrar la ventana (o realizar cualquier otra acción necesaria)
    window.destroy()
