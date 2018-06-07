p1=input()
#p1 = P.rstrip('\r\n')
p2=p1.split(". ")
p3=""
n=0
for val in p2:
    f=val[:1].upper()
    f=f+ val[1:]
    
    if (n==0):
        p3=f
    else:
        p3=p3 + ". " + f
        
    n=n+1
print(p3)
