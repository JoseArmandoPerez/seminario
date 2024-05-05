import tkinter as tk
from PIL import Image, ImageTk

def acerca_ventana():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Acerca de nosotros")
    
    # Configurar la ventana para que sea fullscreen
    nueva_ventana.attributes('-fullscreen', True)
    
    # Obtener el tamaño de la pantalla
    screen_width = nueva_ventana.winfo_screenwidth()
    screen_height = nueva_ventana.winfo_screenheight()
    
    # Cargar imagen de fondo
    bg_image = Image.open("imagenes_inicio/japon.jpg")
    bg_image = bg_image.resize((screen_width, screen_height))
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Crear un marco principal para contener la imagen y el cuadro de texto
    main_frame = tk.Frame(nueva_ventana)
    main_frame.pack(fill="both", expand=True)
    
    # Mostrar la imagen de fondo
    bg_label = tk.Label(main_frame, image=bg_photo)
    bg_label.place(relx=0.5, rely=0.5, anchor="center")
    
    # Información del restaurante
    informacion_restaurante = """
    ¡Bienvenido a nuestro restaurante!

    Historia:
    Nuestro restaurante fue fundado en 2005 por el chef renombrado Juan Pérez. Desde entonces, nos hemos dedicado a ofrecer deliciosos platos inspirados en la cocina tradicional mexicana, con un toque moderno y creativo.

    Misión:
    En nuestro restaurante, nos comprometemos a proporcionar a nuestros clientes una experiencia gastronómica excepcional, ofreciendo alimentos de la más alta calidad preparados con pasión y dedicación.

    Visión:
    Nos esforzamos por ser reconocidos como el mejor restaurante de la región, destacando por nuestra excelencia en servicio al cliente, innovación culinaria y compromiso con la comunidad.

    Dirección:
    Calle Principal #123, Colonia Centro, Ciudad, Estado, C.P. 12345
    """
    
    # Crear un marco para el cuadro de texto con desplazamiento vertical
    text_frame = tk.Frame(main_frame, bg="black", bd=10)
    text_frame.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.8)

    # Cuadro de texto con desplazamiento vertical
    text_widget = tk.Text(text_frame, wrap="word", bg="white", fg="black", bd=0, font=("MS Gothic", 16))
    text_widget.insert("1.0", informacion_restaurante)
    text_widget.pack(fill="both", expand=True)

    # Botón para cerrar la ventana
    close_button = tk.Button(main_frame, text="Cerrar", command=nueva_ventana.destroy, bg="black", fg="white", font=("MS Gothic", 16))
    close_button.place(relx=0.5, rely=0.9, anchor="center")

    # Actualizar el ciclo principal de eventos para mostrar la imagen de fondo
    nueva_ventana.update_idletasks()
    nueva_ventana.mainloop()

