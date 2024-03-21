import tkinter as tk
from tkinter import messagebox

class RestauranteApp:
    def __init__(self, master):
        self.master = master
        master.title("Restaurante")
        master.attributes('-fullscreen', True)  # Abre la ventana principal en pantalla completa

        self.label = tk.Label(master, text="Bienvenido al Restaurante", font=("Helvetica", 24))
        self.label.pack(pady=50)

        master.bind("<Button-1>", self.open_info_window)  # Asociar evento de clic a la función open_info_window

    def open_info_window(self, event):
        self.info_window = tk.Toplevel(self.master)
        self.info_window.attributes('-fullscreen', True)  # Abre la segunda ventana en pantalla completa

        about_button = tk.Button(self.info_window, text="Acerca de nosotros", font=("Helvetica", 18), command=self.open_about_window)
        about_button.pack(pady=10)

        tables_button = tk.Button(self.info_window, text="Mesas disponibles", font=("Helvetica", 18), command=self.open_tables_window)
        tables_button.pack(pady=10)

        close_button = tk.Button(self.info_window, text="Cerrar", font=("Helvetica", 18), command=self.close_info_window)
        close_button.pack(pady=10)

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
        tables_window = tk.Toplevel(self.info_window)
        tables_window.title("Mesas Disponibles")

        # Aquí puedes mostrar información sobre las mesas disponibles

        close_button = tk.Button(tables_window, text="Cerrar", font=("Helvetica", 16), command=tables_window.destroy)
        close_button.pack(pady=10)

    def close_info_window(self):
        self.info_window.destroy()

def main():
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
