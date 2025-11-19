import sys
import math

input = sys.stdin.readline

A, B = map(int, input().split())
C, D = map(int, input().split())

X = A*D + B*C
Y = B*D

g = math.gcd(X, Y)   

X //= g
Y //= g

print(X, Y)
