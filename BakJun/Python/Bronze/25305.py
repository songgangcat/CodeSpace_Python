#

N, k = map(int, input().split())

list_x = map(int, input().split())

print(sorted(list_x, reverse=True)[k-1])