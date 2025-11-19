def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    while True:
        if is_prime(n):
            return n
        n += 1

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    if is_prime(n):
        print(n)
    else:
        print(next_prime(n))