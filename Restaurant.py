import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class RestauranteApp:
    def __init__(self, master):
        self.master = master
        master.title("Ramen & Roll")
        master.attributes('-fullscreen', True)  # Abre la ventana principal en pantalla completa

        # Cargar la imagen de fondo y ajustar su brillo
        self.bg_image = Image.open("imagenes/background_image.png")  # Reemplaza "background_image.png" con tu imagen de fondo
        self.bg_image = self.bg_image.point(lambda p: p * 0.5)  # Reducir el brillo de la imagen
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(master, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        # Mostrar el nombre del restaurante centrado
        self.restaurant_label = tk.Label(master, text="Ramen & Roll", font=("Helvetica", 36, "bold"), fg="white", bg="black")
        self.restaurant_label.place(relx=0.5, rely=0.5, anchor="center")  # Centrar el texto en ambos ejes

        master.bind("<Button-1>", self.move_text_up)  # Asociar evento de clic a la función move_text_up

    def move_text_up(self, event):
        # Desplazar el texto hacia arriba
        self.restaurant_label.place_configure(rely=0.1, anchor="n")  # Posicionar el texto en la parte superior de la ventana

        # Crear botones de menú
        about_button = tk.Button(self.master, text="Acerca de nosotros", font=("Helvetica", 24), command=self.open_about_window)
        about_button.place(relx=0.5, rely=0.5, anchor="center")

        tables_button = tk.Button(self.master, text="Mesas disponibles", font=("Helvetica", 24), command=self.open_tables_window)
        tables_button.place(relx=0.5, rely=0.6, anchor="center")

        recommendations_button = tk.Button(self.master, text="Recomendaciones", font=("Helvetica", 24), command=self.open_recommendations_window)
        recommendations_button.place(relx=0.5, rely=0.7, anchor="center")

        close_button = tk.Button(self.master, text="Salir", font=("Helvetica", 24), command=self.close_all_windows)
        close_button.place(relx=0.5, rely=0.8, anchor="center")

    def open_about_window(self):
        about_window = tk.Toplevel(self.master)
        about_window.title("Acerca de Nosotros")
        about_window.attributes('-fullscreen', True)  # Abre la ventana de Acerca de Nosotros en pantalla completa

        history_label = tk.Label(about_window, text="Historia: ...", font=("Helvetica", 16))
        history_label.pack(pady=10)

        address_label = tk.Label(about_window, text="Dirección: ...", font=("Helvetica", 16))
        address_label.pack(pady=10)

        mission_label = tk.Label(about_window, text="Misión: ...", font=("Helvetica", 16))
        mission_label.pack(pady=10)

        vision_label = tk.Label(about_window, text="Visión: ...", font=("Helvetica", 16))
        vision_label.pack(pady=10)

        about_window.bind("<Button-1>", lambda event: about_window.destroy())  # Cerrar la ventana de Acerca de Nosotros al hacer clic

    def open_tables_window(self):
        tables_window = tk.Toplevel(self.master)
        tables_window.title("Mesas Disponibles")

        # Aquí puedes mostrar información sobre las mesas disponibles

        close_button = tk.Button(tables_window, text="Cerrar", font=("Helvetica", 16), command=tables_window.destroy)
        close_button.pack(pady=10)

    def open_recommendations_window(self):
        recommendations_window = tk.Toplevel(self.master)
        recommendations_window.title("Recomendaciones")

        # Aquí puedes mostrar recomendaciones o platos especiales

        close_button = tk.Button(recommendations_window, text="Cerrar", font=("Helvetica", 16), command=recommendations_window.destroy)
        close_button.pack(pady=10)

    def close_all_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
