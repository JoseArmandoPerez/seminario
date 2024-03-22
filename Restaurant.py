import tkinter as tk
from tkinter import messagebox

class RestauranteApp:
    def __init__(self, master):
        self.master = master
        master.title("Restaurante")
        master.attributes('-fullscreen', True)  # Abre la ventana principal en pantalla completa

        # Configurar imagen de fondo
        self.background_image = tk.PhotoImage(file="background_image.png")
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Configurar menú emergente
        self.menu = tk.Menu(master, tearoff=0)
        self.menu.add_command(label="Acerca de nosotros", command=self.open_about_window)
        self.menu.add_command(label="Mesas disponibles", command=self.open_tables_window)
        self.menu.add_command(label="Recomendaciones", command=self.show_recommendations)
        self.menu.add_command(label="Salir", command=self.close_app)

        master.bind("<Button-1>", self.show_menu)  # Asociar evento de clic a la función show_menu

    def show_menu(self, event):
        self.menu.post(event.x_root, event.y_root)  # Mostrar menú en la posición del clic

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
        tables_window.attributes('-fullscreen', True)  # Abre la ventana de Mesas Disponibles en pantalla completa

        close_button = tk.Button(tables_window, text="Cerrar", font=("Helvetica", 16), command=tables_window.destroy)
        close_button.pack(pady=10)

    def show_recommendations(self):
        messagebox.showinfo("Recomendaciones", "¡Prueba nuestro delicioso ramen especial!")

    def close_app(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
