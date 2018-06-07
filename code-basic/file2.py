fileobject = open("file1.txt", "w")
lines = ["1st line", "2nd line", "3rd line"]
fileobject.writelines(lines)
fileobject.close()
