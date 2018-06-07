name=input("Enter Your Name")
address=input("Enter Address") 
fileobject = open("name.txt", "w")
fileobject.write(name);
fileobject.write(address);
fileobject.close()
