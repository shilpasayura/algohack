name=input("Enter Your Name ") 
fileobject = open("name.txt", "w")
fileobject.write(name);
fileobject.close()
