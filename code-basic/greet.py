def greetings(name):
        gtext="Welcome ." + name         
        print (gtext)
        greetings(name)

name=input("Enter Name")
greetings(name)
