import tkinter as tk

def acerca_ventana():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.attributes('-fullscreen', True)  # Set the window to fullscreen
    nueva_ventana.title("Acerca de nosotros")
    
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

    # Crear un widget de texto con barras de desplazamiento
    text_widget = tk.Text(nueva_ventana, wrap="word")
    text_widget.pack(fill="both", expand=True)

    # Agregar texto al widget de texto
    text_widget.insert("1.0", informacion_restaurante)

    # Agregar barras de desplazamiento
    scrollbar = tk.Scrollbar(nueva_ventana, command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar.set)
    
    # Cambiar estilo de fuente y tamaño
    text_widget.config(font=("Helvetica", 14))
    
    
    # Botón para cerrar la ventana
    close_button = tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy)
    close_button.pack()