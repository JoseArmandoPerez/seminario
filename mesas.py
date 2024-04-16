import tkinter as tk

button_colors = ["green"] * 15
buttons = []  # Define the "buttons" list

def button_pressed(button_number):
    if button_colors[button_number] == "green":
        print(f"Button {button_number + 1} pressed")
        button_colors[button_number] = "red"
        buttons[button_number].config(bg="red")
        buttons[button_number].config(fg="white")
        buttons[button_number].config(state=tk.DISABLED)
        # función para guardar la mesa en la base de datos
        # guardar_mesa_en_base_de_datos(button_number + 1)
        
def mesas_ventana():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Mesas Disponibles")
    nueva_ventana.attributes('-fullscreen', True)

    for i in range(15):
        button = tk.Button(nueva_ventana, text=f"Mesa {i + 1}", bg="green", width=15, height=5, font=("Helvetica", 14), command=lambda i=i: button_pressed(i))
        button.grid(row=i // 5, column=i % 5, padx=80, pady=80)
        buttons.append(button)
