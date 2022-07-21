def primes(n):
    """ Returns  a list of primes < n """
    if n <= 2: return 0
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    return len([i for i in range(3,n,2) if sieve[i]]) + 1

def redJohn(N):
    if N == 0:
        return 1
    elif N < 0:
        return 0
    
    return primes(redJohn(N-1)) + primes(redJohn(N-4))
