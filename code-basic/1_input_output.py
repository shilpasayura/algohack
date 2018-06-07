#p1="python one is the first online revision for A/L students to help to get all marks for the python question. #python programming language is very easy to learn. this question is based on python strings."

p=input()
p2=p.split(". ")
p3=""
n=0
for val in p2:
    f=val[:1].upper()
    f1=val[1:]
    if (n==0):
        p3=f
    else:
        p3=p3 + ". " + f
        
    n=n+1
print(p3)
