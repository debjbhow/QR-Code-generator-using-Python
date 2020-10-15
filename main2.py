import qrcode

qr = qrcode.make('Hello World')
qr.save('myQR.png')

qr = qrcode.QRCode(
    version=1,
    box_size=15, 
    border=5
)

data= "https://www.linkedin.com/in/debjit-bhowmik-845476150/"
qr.add_data(data)
qr.make(fit= True)
img=qr.make_image(fill = "black", back_color = "white")
img.save("Debjit's QR Code.png")