#

N, K = map(int, input().split())
list_a = []

for i in range(1, N+1):
    if N%i == 0:
        list_a.append(i)
    else:
        continue


if len(list_a) >= K:
    print(list_a[K-1])
else:
    print(0)