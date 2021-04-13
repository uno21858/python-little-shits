import qrcode

data = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
filename = "web.png"
img = qrcode.make(data)
img.save(filename)