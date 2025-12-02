import math

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r) 
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(nCr(M, N))