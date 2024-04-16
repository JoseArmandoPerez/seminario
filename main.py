import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from recomendaciones import recomendaciones_ventana
from acerca import acerca_ventana
from mesas import mesas_ventana
from pedidos_bebidas import abrir_ventana_pedidos
from Registrar_comida import abrir_ventana_pedidos_comida
from sesion import iniciar_sesion
import requests

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

class RestauranteApp(tk.Tk):  # Hereda de tk.Tk
    def __init__(self):
        super().__init__()
        self.title("Interfaz con Botones")
        self.attributes('-fullscreen', True)  # Set the window to fullscreen

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
        
        orders_button2 = tk.Button(self, text="Menu Comida", font=("Helvetica", 24), command=self.open_menu_comida, width=15)
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
        
        sign_in_button = tk.Button(self, text="Iniciar Sesión", font=("Helvetica", 24), command=self.sign_in, width=15)
        sign_in_button.place(relx=0.8, rely=0.1, anchor="center")
        
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
        abrir_ventana_pedidos()
        
    def open_menu_comida(self):
        abrir_ventana_pedidos_comida()    

    def sign_in(self):
        iniciar_sesion()

    def close_all_windows(self):
        self.destroy()

def main():
    app = RestauranteApp()
    app.mainloop()

if __name__ == "__main__":
    main()

