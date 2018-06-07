A=int(input())
B=int(input())
B2=B**2

if (B-2) > 0 :
    C=A % (B-2)

    if ((A==B2) and (C==0)):
        print ("100%")
    elif ((A==B2) and (C!=0)):
        print ("50%")
    else:
        print ("0%")

