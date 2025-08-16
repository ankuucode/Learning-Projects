import qrcode as qr
#Generate Qr Code
def GenQr(data):
    q=qr.QRCode(
        version=1,
        error_correction=qr.ERROR_CORRECT_H,
        box_size=12,border=5
    )

    q.add_data(data)

    q.make(fit=True)
    img=   q.make_image(fill_color='red',back_color="black")

    img.save("Qr.png")
    print("Image saved")

data=input("Enter Your Data:")
GenQr(data)

