import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sesion  # Importa el módulo de inicio de sesión
import requests
from acerca import acerca_ventana
from mesas import mesas_ventana
from recomendaciones import recomendaciones_ventana
from menu_comida import mostrar_menu
from pedidos_bebidas import abrir_ventana_pedidos


class RestauranteApp(tk.Tk):  
    def __init__(self):
        super().__init__()
        self.title("Interfaz con Botones")
        self.attributes('-fullscreen', True)  
        self.nombre_usuario = None
        self.sesion_iniciada = False
        self.id = 0
        
        self.bg_image = Image.open("imagenes/background_image.png")
        self.bg_image = self.bg_image.resize((self.winfo_screenwidth(), self.winfo_screenheight()))
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Coloca la imagen de fondo en toda la ventana


        restaurant_label = tk.Label(self, text="Ramen & Roll", font=("Helvetica", 36, "bold"), fg="white", bg="black")
        restaurant_label.place(relx=0.5, rely=0.1, anchor="center")
        
        self.orders_button2 = tk.Button(self, text="Menu Comida", font=("Helvetica", 24), command=self.mostrar_menu, width=15)
        self.orders_button2.place(relx=0.5, rely=0.3, anchor="center")
        
        self.orders_button = tk.Button(self, text="Menu Bebidas", font=("Helvetica", 24), command=self.open_menu_bebidas, width=15)
        self.orders_button.place(relx=0.5, rely=0.4, anchor="center")

        about_button = tk.Button(self, text="Acerca de nosotros", font=("Helvetica", 24), command=self.open_about_window, width=15)
        about_button.place(relx=0.5, rely=0.5, anchor="center")

        tables_button = tk.Button(self, text="Mesas disponibles", font=("Helvetica", 24), command=self.open_tables_window, width=15)
        tables_button.place(relx=0.5, rely=0.6, anchor="center")

        recommendations_button = tk.Button(self, text="Recomendaciones", font=("Helvetica", 24), command=self.open_recommendations_window, width=15)
        recommendations_button.place(relx=0.5, rely=0.7, anchor="center")

        close_button = tk.Button(self, text="Salir", font=("Helvetica", 24), command=self.close_all_windows, width=15)
        close_button.place(relx=0.5, rely=0.8, anchor="center")
        
        self.sign_out_button = tk.Button(self, text="Cerrar sesión", font=("Helvetica", 24), command=self.sign_out, width=15)
        self.sign_out_button.place(relx=0.8, rely=0.1, anchor="center")

        self.sign_in_button = tk.Button(self, text="Iniciar sesión", font=("Helvetica", 24), command=self.choose_login, width=15)
        self.sign_in_button.place(relx=0.8, rely=0.1, anchor="center")
        
        servidor_esta_activo = check_server_status("http://100.82.213.30:5000")
        if servidor_esta_activo:
            print("El servidor está activo.")
            restaurant_label = tk.Label(self, text="Servidor activo", font=("Helvetica", 12, "bold"), fg="green")
            restaurant_label.place(relx=0.1, rely=0.1, anchor="center")
        else:
            print("El servidor no está activo.")
            
    def open_about_window(self):
        acerca_ventana()

    def open_tables_window(self):
        mesas_ventana()

    def open_recommendations_window(self):
        recomendaciones_ventana()
        
    def open_menu_bebidas(self):
        self.verificar_sesion()
        abrir_ventana_pedidos()
        
    def mostrar_menu(self):
        self.verificar_sesion()
        mostrar_menu()    
            
    def close_all_windows(self):
        self.destroy()
        
    def sign_in(self):
        iniciar_sesion()

    def sign_out(self):
        self.nombre_usuario = None
        self.sesion_iniciada = False
        self.sign_in_button.place(relx=0.8, rely=0.1, anchor="center")
        self.sign_out_button.place_forget()

    def verificar_sesion(self):
        if self.sesion_iniciada:
            self.sign_out_button.config(text=f"Salir como {self.nombre_usuario}")
            self.sign_in_button.place_forget()
            self.sign_out_button.place(relx=0.8, rely=0.1, anchor="center")
        else:
            self.sign_out_button.config(text="Iniciar sesión")
            self.sign_in_button.place(relx=0.8, rely=0.1, anchor="center")
            self.sign_out_button.place_forget()

    def choose_login(self):
        login_window = tk.Toplevel(self)
        login_window.title("Elige el tipo de sesión")
        login_window.geometry("450x250")  # Ajusta el tamaño de la ventana

        frame = tk.Frame(login_window, padx=20, pady=10)
        frame.pack()
        
        tipo_usuario = tk.StringVar()
        cliente_radio = tk.Radiobutton(frame, text="Cliente", variable=tipo_usuario, value="cliente")
        cliente_radio.grid(row=0, column=0, sticky="w", pady=5)
        chef_radio = tk.Radiobutton(frame, text="Chef", variable=tipo_usuario, value="chef")
        chef_radio.grid(row=1, column=0, sticky="w", pady=5)
        mesero_radio = tk.Radiobutton(frame, text="Mesero", variable=tipo_usuario, value="mesero")
        mesero_radio.grid(row=2, column=0, sticky="w", pady=5)
        barman_radio = tk.Radiobutton(frame, text="Bar-Man", variable=tipo_usuario, value="bar-man")
        barman_radio.grid(row=3, column=0, sticky="w", pady=5)
        duenio_radio = tk.Radiobutton(frame, text="Dueño", variable=tipo_usuario, value="dueño")
        duenio_radio.grid(row=4, column=0, sticky="w", pady=5)
        
        button = tk.Button(frame, text="Ingresar", command=lambda: mostrar_formulario(tipo_usuario.get(), login_window))
        button.grid(row=5, columnspan=2, pady=5, padx=5)

def check_server_status(url):
    servidor_activo = False
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
            servidor_activo = True
        else:
            print(f"El servidor respondió con el código de estado: {response.status_code}")
            servidor_activo = False
    except requests.ConnectionError:
        print("No se pudo conectar al servidor.")
        servidor_activo = False
    
    return servidor_activo

def mostrar_formulario(tipo_usuario, login_window):
    form_window = tk.Toplevel(login_window)
    form_window.geometry("250x150")    
    form_window.title("Inicio de Sesión")
    

    if tipo_usuario == "cliente":
        name_label = tk.Label(form_window, text="Nombre:")
        name_label.grid(row=0, column=0, sticky="w", pady=10)
        name_entry = tk.Entry(form_window)
        name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        button = tk.Button(form_window, text="Ingresar", command=lambda: iniciar_sesion(name_entry.get(), tipo_usuario, form_window))
        button.grid(row=1, columnspan=2, pady=10, padx=10)
    else:
        name_label = tk.Label(form_window, text="Nombre:")
        name_label.grid(row=0, column=0, sticky="w", pady=10)
        name_entry = tk.Entry(form_window)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(form_window, text="Contraseña:")
        password_label.grid(row=1, column=0, sticky="w", pady=10)
        password_entry = tk.Entry(form_window, show="*")
        password_entry.grid(row=1, column=1, padx=10, pady=10)

        button = tk.Button(form_window, text="Ingresar", command=lambda: iniciar_sesion(name_entry.get(), tipo_usuario, form_window))
        button.grid(row=2, columnspan=2, pady=10, padx=10)

def iniciar_sesion(nombre, tipo_usuario, window):
    
    # Si el tipo de usuario es "cliente", solo se necesita el nombre para iniciar sesión
    if tipo_usuario == "cliente":
        # Realiza la lógica de inicio de sesión para el cliente con el nombre proporcionado
        # Aquí puedes llamar a la función de inicio de sesión del módulo "sesion.py"
        sesion.iniciar_sesion_cliente(nombre)
    else:
        # Si el tipo de usuario no es "cliente", se requiere nombre y contraseña para iniciar sesión
        # Puedes realizar la lógica de inicio de sesión con nombre y contraseña para otros tipos de usuarios
        # Aquí puedes llamar a la función de inicio de sesión del módulo "sesion.py" con nombre y contraseña
        sesion.iniciar_sesion_otro(nombre,password)
        
    # Cierra la ventana de inicio de sesión después de iniciar sesión
    window.destroy()
bg_image = Image.open("imagenes/background_image.png")


if __name__ == "__main__":
    app = RestauranteApp()
    app.mainloop()
