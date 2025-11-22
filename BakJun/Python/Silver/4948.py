import sys
input = sys.stdin.readline

def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    return is_prime

while True:
    n = int(input())
    if n == 0:
        break
    A = sieve(2*n)
    list = [i for i, v in enumerate(A) if v]
    result = [x for x in list if n < x <= 2*n]
    print(len(result))