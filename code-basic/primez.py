i = 2
def isprime(N):
    global i
    print ( "Processing ", N , "/", i, N/i)

    if (N % i == 0 and N > i ): # check even
        return False
    i = i + 1
    if(N > i): # upto N-1 
        prime=isprime(N)
        return prime
    else:
        return True

N = int(input('Enter Number'))
prime= isprime(N)
if (prime):
    print ( N , " is prime")
else:
    print ( N , " is not prime")
