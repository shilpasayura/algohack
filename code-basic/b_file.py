f = open("file1.txt", "rb")
data = f.read(1)
while (len(data) > 0):
      print(data)
      data = f.read(1)
f.close()
