import qrcode

img = qrcode.make("Welcome to my page!")

img.save("MyWelcomeQR.png")
