import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from recomendaciones import recomendaciones_ventana
from acerca import acerca_ventana
from mesas import mesas_ventana
from pedidos_bebidas import abrir_ventana_pedidos
from menu_comida import mostrar_menu
from sesion import iniciar_sesion
import requests
import json
import time

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

def main():
    # Llamar a la función para mostrar el menú antes de iniciar la aplicación principal
    mostrar_menu()

    app = RestauranteApp()
    app.mainloop()

class RestauranteApp(tk.Tk):  # Hereda de tk.Tk
    def __init__(self):
        super().__init__()
        self.title("Interfaz con Botones")
        self.attributes('-fullscreen', True)  # Set the window to fullscreen
        
        self.nombre_usuario = None
        self.sesion_iniciada = False
        self.id = 0

        # Cargar la imagen de fondo
        try:
            self.bg_image = Image.open("imagenes/background_image.png")
            self.bg_image = self.bg_image.resize((self.winfo_screenwidth(), self.winfo_screenheight()))
            self.bg_image = ImageTk.PhotoImage(self.bg_image)
            self.bg_label = tk.Label(self, image=self.bg_image)
            self.bg_label.place(relx=0.5, rely=0.5, anchor="center")
        except Exception as e:
            print("Error al cargar la imagen de fondo:", e)

        # Nombre del restaurante
        restaurant_label = tk.Label(self, text="Ramen & Roll", font=("Helvetica", 36, "bold"), fg="white", bg="black")
        restaurant_label.place(relx=0.5, rely=0.1, anchor="center")
        
        orders_button2 = tk.Button(self, text="Menu Comida", font=("Helvetica", 24), command=mostrar_menu, width=15)
        orders_button2.place(relx=0.5, rely=0.3, anchor="center")
        
        orders_button = tk.Button(self, text="Menu Bebidas", font=("Helvetica", 24), command=self.open_menu_bebidas, width=15)
        orders_button.place(relx=0.5, rely=0.4, anchor="center")

        about_button = tk.Button(self, text="Acerca de nosotros", font=("Helvetica", 24), command=self.open_about_window, width=15)
        about_button.place(relx=0.5, rely=0.5, anchor="center")

        tables_button = tk.Button(self, text="Mesas disponibles", font=("Helvetica", 24), command=self.open_tables_window, width=15)
        tables_button.place(relx=0.5, rely=0.6, anchor="center")

        recommendations_button = tk.Button(self, text="Recomendaciones", font=("Helvetica", 24), command=self.open_recommendations_window, width=15)
        recommendations_button.place(relx=0.5, rely=0.7, anchor="center")

        close_button = tk.Button(self, text="Salir", font=("Helvetica", 24), command=self.close_all_windows, width=15)
        close_button.place(relx=0.5, rely=0.8, anchor="center")
        
        # Botones de inicio y cierre de sesión
        self.sign_out_button = tk.Button(self, text="Cerrar sesión", font=("Helvetica", 24), command=self.sign_out, width=15)
        self.sign_out_button.place(relx=0.8, rely=0.1, anchor="center")

        self.sign_in_button = tk.Button(self, text="Iniciar sesión", font=("Helvetica", 24), command=self.sign_in, width=15)
        self.sign_in_button.place(relx=0.8, rely=0.1, anchor="center")
        
        # Llamar a la función para verificar si el servidor de http://192.168.100.89:5000/ está activo
        servidor_esta_activo = check_server_status("http://192.168.100.89:5000")
        if servidor_esta_activo:
            print("El servidor está activo.")
            # Mostrar un texto en la ventana principal
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
        
    def open_menu_comida(self):
        self.verificar_sesion()
        mostrar_menu()    
            
    def close_all_windows(self):
        self.destroy()
        
    def sign_in(self):
        iniciar_sesion()
        
    def sign_out(self):
        guardar_estado_usuario(False, None, None)
        self.nombre_usuario = None
        self.sign_in_button.place(relx=0.8, rely=0.1, anchor="center")
        self.sign_out_button.place_forget()

    # Ver por que no se puede acceder al self
    def verificar_sesion(self):
        self.sesion_iniciada, self.id, self.nombre_usuario = cargar_estado_usuario()
        print(f"Estado del usuario: {self.sesion_iniciada}, {self.nombre_usuario}")
        if(self.nombre_usuario != "None" or self.nombre_usuario != "null"):
            self.sign_out_button.config(text=f"Salir como {self.nombre_usuario}")
            self.sign_in_button.place_forget()
            self.sign_out_button.place(relx=0.8, rely=0.1, anchor="center")
        else:
            self.sign_out_button.config(text="Iniciar sesión")
            self.sign_in_button.place(relx=0.8, rely=0.1, anchor="center")
            self.sign_out_button.place_forget()
            
def cargar_estado_usuario():
    try:
        with open('config.json', 'r') as f:
            data = json.load(f)
            id_usuario = data['id_usuario']
            nombre_usuario = data['nombre_usuario']
            if(nombre_usuario != None or nombre_usuario != "null"):
                print(f"El usuario {nombre_usuario} ha iniciado sesión.")
                return True, id_usuario, nombre_usuario
            else:
                print("No hay usuario iniciado.")
                return False, "error", "error"
    except FileNotFoundError:
        return False, "error", "error"


def guardar_estado_usuario(usuario_iniciado, nombre_usuario, id_usuario):
    with open('config.json', 'w') as f:
        # Guarda el estado del usuario en un archivo JSON
        json.dump({'usuario_iniciado': usuario_iniciado, 'nombre_usuario': nombre_usuario, 'id_usuario': id_usuario}, f)
         
if __name__ == "__main__":
    guardar_estado_usuario(False, None, None)
    
    main()
