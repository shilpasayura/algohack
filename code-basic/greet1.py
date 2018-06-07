
def greetings(name,counter):
    if(counter > 10):
        return counter
    else:
        counter=counter+1  
        gtext="Welcome ." + name         
        print (gtext)
        greetings(name, counter)

name=input("Enter Name")
counter=0
greetings(name, counter)


        
