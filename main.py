import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sesion  # Importa el módulo de inicio de sesión
import requests
import json
import time

def main():
    # Llamar a la función para mostrar el menú antes de iniciar la aplicación principal
    #mostrar_menu()

    app = RestauranteApp()
    app.mainloop()

class RestauranteApp(tk.Tk):  # Hereda de tk.Tk
    def __init__(self):
        super().__init__()
        self.title("Ramen & Roll")
        self.attributes('-fullscreen', True)  
        
        self.nombre_usuario = None
        self.id = 0
        self.tipo_usuario = None

        try:
            self.bg_image = Image.open("imagenes/background_image.png")
            self.bg_image = self.bg_image.resize((self.winfo_screenwidth(), self.winfo_screenheight()))
            self.bg_image = ImageTk.PhotoImage(self.bg_image)
            self.bg_label = tk.Label(self, image=self.bg_image)
            self.bg_label.place(relx=0.5, rely=0.5, anchor="center")
        except Exception as e:
            print("Error al cargar la imagen de fondo:", e)

        restaurant_label = tk.Label(self, text="Ramen & Roll", font=("Helvetica", 36, "bold"), fg="white", bg="black")
        restaurant_label.place(relx=0.5, rely=0.1, anchor="center")
        
        self.orders_button2 = tk.Button(self, text="Menu Comida", font=("Helvetica", 24), command=self.open_menu_comidas, width=15)
        self.orders_button2.place(relx=0.5, rely=0.3, anchor="center")
        
        self.orders_button = tk.Button(self, text="Menu Bebidas", font=("Helvetica", 24), command=self.open_menu_bebidas, width=15)
        self.orders_button.place(relx=0.5, rely=0.4, anchor="center")
        
        # PARA EL CHEF, BARTENDER Y MESERO
       # self.orden_bebida = tk.Button(self, text="Orden bebida", font=("Helvetica", 24), command=self.mostrar_menu, width=15)
        #self.orden_bebida.place_forget()
        
        self.orden_comida = tk.Button(self, text="Orden Comida", font=("Helvetica", 24), command=self.open_menu_bebidas, width=15)
        self.orden_comida.place_forget()
        
        # PARA EL DUEÑO
        self.estadistica = tk.Button(self, text="Estadísticas", font=("Helvetica", 24), command=self.open_menu_bebidas, width=15)
        self.estadistica.place_forget()

        self.about_button = tk.Button(self, text="Acerca de nosotros", font=("Helvetica", 24), command=self.open_about_window, width=15)
        self.about_button.place(relx=0.5, rely=0.5, anchor="center")

        self.tables_button = tk.Button(self, text="Mesas disponibles", font=("Helvetica", 24), command=self.open_tables_window, width=15)
        self.tables_button.place(relx=0.5, rely=0.6, anchor="center")

        self.recommendations_button = tk.Button(self, text="Recomendaciones", font=("Helvetica", 24), command=self.open_recommendations_window, width=15)
        self.recommendations_button.place(relx=0.5, rely=0.7, anchor="center")

        close_button = tk.Button(self, text="Salir", font=("Helvetica", 24), command=self.close_all_windows, width=15)
        close_button.place(relx=0.5, rely=0.8, anchor="center")
        
        self.sign_out_button = tk.Button(self, text="Cerrar sesión", font=("Helvetica", 24), command=self.sign_out, width=15)
        self.sign_out_button.place(relx=0.8, rely=0.1, anchor="center")

        self.sign_in_button = tk.Button(self, text="Iniciar sesión", font=("Helvetica", 24), command=self.choose_login, width=15)
        self.sign_in_button.place(relx=0.8, rely=0.1, anchor="center")
            
    def open_about_window(self):
        acerca_ventana()

    def open_tables_window(self):
        mesas_ventana()

    def open_recommendations_window(self):
        recomendaciones_ventana()
        
    def open_menu_bebidas(self):
        self.verificar_sesion()
        abrir_ventana_pedidos()
        
    def open_menu_comidas(self):
        self.verificar_sesion()
        mostrar_menu()

        
    def close_all_windows(self):
        self.destroy()
        
    def sign_in(self):
        iniciar_sesion()

    def sign_out(self):
        self.nombre_usuario = None
        self.sesion_iniciada = False
        self.sign_out_button.config(text="Iniciar sesión")
        self.sign_in_button.place(relx=0.8, rely=0.1, anchor="center")
        self.sign_out_button.place_forget()
        self.orden_bebida.place_forget()
        self.orden_comida.place_forget()
        self.estadistica.place_forget()
        self.orders_button.place(relx=0.5, rely=0.3, anchor="center")
        self.orders_button2.place(relx=0.5, rely=0.4, anchor="center")
        self.about_button.place(relx=0.5, rely=0.5, anchor="center")
        self.tables_button.place(relx=0.5, rely=0.6, anchor="center")
        self.recommendations_button.place(relx=0.5, rely=0.7, anchor="center")
        with open('usuario.json', 'w') as file:
                json.dump({}, file)

    def verificar_sesion(self):
        if self.sesion_iniciada:
            self.sign_out_button.config(text=f"Salir como {self.nombre_usuario}")
            self.sign_in_button.place_forget()
            self.sign_out_button.place(relx=0.8, rely=0.1, anchor="center")
            if self.tipo_usuario == "chef" or self.tipo_usuario == "mesero":
                self.orden_bebida.place(relx=0.33, rely=0.5, anchor="center")
                self.orden_comida.place(relx=0.66, rely=0.5, anchor="center")
                self.about_button.place_forget()
                self.tables_button.place_forget()
                self.recommendations_button.place_forget()
                self.orders_button.place_forget()
                self.orders_button2.place_forget()
            elif self.tipo_usuario == "bartender":
                self.orden_bebida.place(relx=0.5, rely=0.5, anchor="center")
                self.orden_comida.place_forget()
                self.about_button.place_forget()
                self.tables_button.place_forget()
                self.recommendations_button.place_forget()
                self.orders_button.place_forget()
                self.orders_button2.place_forget()
            elif self.tipo_usuario == "dueño":
                self.orden_bebida.place(relx=0.5, rely=0.2, anchor="center")
                self.orden_comida.place(relx=0.5, rely=0.4, anchor="center")
                self.estadistica.place(relx=0.5, rely=0.6, anchor="center")
                self.about_button.place_forget()
                self.tables_button.place_forget()
                self.recommendations_button.place_forget()
                self.orders_button.place_forget()
                self.orders_button2.place_forget()
        else:
            print("verificar_sesion(self): No hay sesión iniciada")

    def choose_login(self):
        login_window = tk.Toplevel(self)
        login_window.title("Elige el tipo de sesión")
        login_window.geometry("450x250")  # Ajusta el tamaño de la ventana

        frame = tk.Frame(login_window, padx=20, pady=10)
        frame.pack()
        
        tipo_usuario = tk.StringVar()
        cliente_radio = tk.Radiobutton(frame, text="Cliente", variable=tipo_usuario, value="cliente")
        cliente_radio.grid(row=0, column=0, sticky="w", pady=5)
        cliente_radio.select()  # Establecer como seleccionado por defecto
        chef_radio = tk.Radiobutton(frame, text="Chef", variable=tipo_usuario, value="chef")
        chef_radio.grid(row=1, column=0, sticky="w", pady=5)
        mesero_radio = tk.Radiobutton(frame, text="Mesero", variable=tipo_usuario, value="mesero")
        mesero_radio.grid(row=2, column=0, sticky="w", pady=5)
        barman_radio = tk.Radiobutton(frame, text="Bartender", variable=tipo_usuario, value="bartender")
        barman_radio.grid(row=3, column=0, sticky="w", pady=5)
        duenio_radio = tk.Radiobutton(frame, text="Dueño", variable=tipo_usuario, value="dueño")
        duenio_radio.grid(row=4, column=0, sticky="w", pady=5)
        
        button = tk.Button(frame, text="Ingresar", command=lambda: mostrar_formulario(tipo_usuario.get(), login_window))
        button.grid(row=5, columnspan=2, pady=5, padx=5)

def mostrar_formulario(tipo_usuario, login_window):
    form_window = tk.Toplevel(login_window)
    form_window.geometry("250x150")    
    form_window.title("Inicio de Sesión")
    

    if tipo_usuario == "cliente":
        name_label = tk.Label(form_window, text="Nombre:")
        name_label.grid(row=0, column=0, sticky="w", pady=10)
        name_entry = tk.Entry(form_window)
        name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        button = tk.Button(form_window, text="Ingresar", command=lambda: iniciar_sesion(name_entry.get(), form_window))
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

        button = tk.Button(form_window, text="Ingresar", command=lambda: iniciar_sesion_otro(name_entry.get(), password_entry.get(), tipo_usuario, form_window))
        button.grid(row=2, columnspan=2, pady=10, padx=10)

def iniciar_sesion(nombre, window):

    sesion.iniciar_sesion_cliente(nombre)
    
    window.destroy()
    verificar_sesion()
    
    
def iniciar_sesion_otro(nombre, password, tipo_usuario, window):
    print(nombre, password, tipo_usuario)
    
    sesion.iniciar_sesion_otro(nombre, password, tipo_usuario)
        
    window.destroy()
    verificar_sesion()
        
def verificar_sesion():
    with open('usuario.json', 'r') as file:
        data = json.load(file)
        if data:
            app.nombre_usuario = data['nombre']
            app.sesion_iniciada = True
            app.id = data['id']
            app.tipo_usuario = data['tipo_usuario']
        else:
            app.nombre_usuario = None
            app.sesion_iniciada = False
            app.id = 0
    app.verificar_sesion()

if __name__ == "__main__":
    # Borrar usuario.json
    with open('usuario.json', 'w') as file:
        json.dump({}, file)
    app = RestauranteApp()
    app.mainloop()
