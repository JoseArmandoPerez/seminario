import qrcode
from PIL import Image, ImageDraw, ImageFont

# Información del pedido
pedido_info = "Pedido #123: 2x Pizza Margarita, 1x Coca-Cola. Mesa 5."

# Generar código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(pedido_info)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white")

# Crear ticket
ticket = Image.new('RGB', (qr_img.width + 400, qr_img.height + 110), 'white')
d = ImageDraw.Draw(ticket)

# Agregar texto al ticket
font = ImageFont.load_default()
d.text((10,10), "Ticket del Restaurante", fill=(0,0,0), font=font)
d.text((10,30), pedido_info, fill=(0,0,0), font=font)

# Pegar el código QR en el ticket
ticket.paste(qr_img, (10, 50))

# Guardar el ticket
ticket.save("imagenes/ticket.png")

# Para mostrar el ticket en algunos entornos (como Jupyter Notebooks)
ticket.show()
