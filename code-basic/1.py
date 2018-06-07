S=input()
N=input()
S1 = S.rstrip('\r\n')
N1 = int(N)
print (S1 * N1)
#2nd way
ts=""
n=0
while n < N1:  # condition for loop
    ts=ts + S
    n = n + 1
print (ts)
