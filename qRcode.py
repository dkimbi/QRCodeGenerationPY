import qrcode

# img = qrcode.make("Welcome to my page!")

img = qrcode.make('https://github.com/dkimbi')
imgGit = qrcode.make('https://github.com/')

img.save("myPageQR.png")

imgGit.save("gitHome.png")
