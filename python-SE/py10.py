A=int(input("Number A"))
B= int(input("Number B "))
C=int(input("Number C"))

if A > B and A > C:
    print ("A is big", A)

if A > B and not(A > C):
    print ("C is big", C)

if not (A > B) and (B > C):
    print ("B is big", B)

