import qrcode

# URL to embed in the QR code
# url1= "http://localhost:80/avend?action=start;http://localhost:80/avend?action=dispense&code=14"
# url3 = "http://localhost:80/avend?action=dispense&code=12"
# url1= "http://localhost:80/avend?action=dispense&code=14"
# url = "http://localhost:80/avend?action=dispense&code=14"
# url = "http://192.168.5.54:80/avend?action=start"
# url = "http://192.168.5.54:80/avend?token=token&devid=HAZ99&action=clear"
# url = "http://127.0.0.1:80/avend?token=token&devid=HAZ99&action=add&code=22"
# url = "http://127.0.0.1:80/avend?token=token&devid=HAZ99&action=add&code=22"
# url = "http://127.0.0.1:80/avend?token=token&devid=HAZ99&action=start"
# url = "https://www.google.com/"
# url = "http://127.0.0.1:80/avend?token=token&devid=HAZ99&action=start"
url = "http://127.0.0.1:80/avend?token=token&devid=HAZ99&action=dispense&code=12"


# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code, 1 is the smallest
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
    box_size=6,  # controls how many pixels each “box” of the QR code is
    border=2,  # controls how many boxes thick the border should be
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save the image
png = "dispense.png"
print("Wrote to {} ".format( png ))
img.save(png)