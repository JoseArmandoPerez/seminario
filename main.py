import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from recomendaciones import recomendaciones_ventana
from acerca import acerca_ventana
from mesas import mesas_ventana

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

        about_button = tk.Button(self, text="Acerca de nosotros", font=("Helvetica", 24), command=self.open_about_window, width=15)
        about_button.place(relx=0.5, rely=0.5, anchor="center")

        tables_button = tk.Button(self, text="Mesas disponibles", font=("Helvetica", 24), command=self.open_tables_window, width=15)
        tables_button.place(relx=0.5, rely=0.6, anchor="center")

        recommendations_button = tk.Button(self, text="Recomendaciones", font=("Helvetica", 24), command=self.open_recommendations_window, width=15)
        recommendations_button.place(relx=0.5, rely=0.7, anchor="center")

        close_button = tk.Button(self, text="Salir", font=("Helvetica", 24), command=self.close_all_windows, width=15)
        close_button.place(relx=0.5, rely=0.8, anchor="center")

    def open_about_window(self):
        acerca_ventana()

    def open_tables_window(self):
        mesas_ventana()

    def open_recommendations_window(self):
        recomendaciones_ventana()

    def close_all_windows(self):
        self.destroy()

def main():
    app = RestauranteApp()
    app.mainloop()

if __name__ == "__main__":
    main()
