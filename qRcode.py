import qrcode

img = qrcode.make("Welcome to my page!")

img.save("WelcomeQR.png")
