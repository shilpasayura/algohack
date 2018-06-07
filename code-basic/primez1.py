i = 2

def isprime(N):
    global i, maxn
    print ( "Processing ", N , "/", i, N/i)

    if (N % i == 0 and N > i ): # check even
        return False
    i = i + 1
    if(N > i and i < maxn): # upto N-1 
        prime=isprime(N)
        return prime
    else:
        return True

N = int(input('Enter Number'))
maxn=round((N-1)/2)+1
print ("Max n ", maxn)
prime= isprime(N)
if (prime):
    print ( N , " is prime")
else:
    print ( N , " is not prime")
