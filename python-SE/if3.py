A=int(input("Enter A :"))
B=int(input("Enter B :"))
C=int(input("Enter C :"))

if (A > B):
    if (A > C) :
        print ("A is big")
    else:  # A < C
        print ("C is big")
else: # B > A
    if (A==B):
        if (A > C):
            print ("A and B are Big")
        else:
            print ("C is Big")
        
    
