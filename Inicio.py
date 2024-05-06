import tkinter as tk
from PIL import Image, ImageTk
from main import RestauranteApp  # Importa la clase RestauranteApp desde main.py

class Screensaver(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Screensaver")
        self.attributes('-fullscreen', True)
        self.configure(background='white')

        # Cargar la imagen de la bandera de Japón
        japan_flag_image = Image.open("imagenes/japan_flag.png")
        japan_flag_image = japan_flag_image.resize((self.winfo_screenwidth(), self.winfo_screenheight()))
        japan_flag_photo = ImageTk.PhotoImage(japan_flag_image)
        self.japan_flag_label = tk.Label(self, image=japan_flag_photo)
        self.japan_flag_label.image = japan_flag_photo
        self.japan_flag_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Texto RAMEN&ROLL
        self.text_label = tk.Label(self, text="RAMEN&ROLL", font=("Helvetica", 36, "bold"), fg="red", bg="white")
        self.text_label.place(x=self.winfo_screenwidth() // 2, y=self.winfo_screenheight() // 2, anchor="center")

        # Vincular evento de clic
        self.bind("<Button-1>", self.open_main)

    def open_main(self, event):
        # Oculta la ventana del screensaver temporalmente
        self.withdraw()
        self.destroy()
        # Abre main.py
        RestauranteApp()

        # Muestra nuevamente la ventana del screensaver
        self.deiconify()

if __name__ == "__main__":
    app = Screensaver()
    app.mainloop()
