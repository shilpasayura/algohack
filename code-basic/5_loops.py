n=0
while (n < 5):
    S=input()
    S.rstrip('\r\n')
    N=int(S)
    if (N > 0):
        if (N % 2 == 1 ):
            print(N)
    n=n+1
