
def getString():
    S=input()
    S1=S.rstrip('\r\n')
    return S1

def getNumber():
    N=input()
    if (N.isdigit()):
        N1 = int(N)
    else:
        N1=0     
    return N1

S=getString()
N=getNumber()
ts=""
n=0
while n < N:  # condition for loop
    ts=ts + S
    n = n + 1
print (ts)
