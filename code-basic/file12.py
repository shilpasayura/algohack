fileobject = open("file.txt", "w")
line1 = "1st line"
line2 ="2nd line"
fileobject.write(line1)
fileobject.writex("\n")
fileobject.write(line2)
fileobject.close()
