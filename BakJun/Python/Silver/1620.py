import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name = []
num = {}


for i in range(1, N+1):
    x = input().rstrip()
    name.append(x)
    num[x] = i
    
for i in range(M):
    x = input().rstrip()
    if x.isdigit() == True:
        print(name[int(x)-1])
    else:
        print(num[x])