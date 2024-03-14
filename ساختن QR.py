import qrcode
data = input ("entaer txt: ")
img = qrcode.make(data)
name = input ("enter name: ")
img.save (name)