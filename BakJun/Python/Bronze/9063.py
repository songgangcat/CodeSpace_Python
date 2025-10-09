#
X = []
Y = []

N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    X.append(A)
    Y.append(B)

print((max(X)-min(X))*(max(Y)-min(Y)))