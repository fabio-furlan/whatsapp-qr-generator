import qrcode

# Número de telefone
numero_telefone = "5511" 


link_whatsapp = f"https://wa.me/{numero_telefone}"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(link_whatsapp)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

img.save("qrcode_whatsapp.png")

print(f"QR code gerado para o número {numero_telefone}")
