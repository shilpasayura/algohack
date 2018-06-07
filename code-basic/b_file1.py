f = open("image.jpg", "rb")
data = f.read(1)
while (len(data) > 0):
      print(data)
      data = f.read(1)
f.close()
