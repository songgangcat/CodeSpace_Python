import sys
input = sys.stdin.readline

N = int(input())
who = set()
gom = 0

for _ in range(N):
    chat = input().rstrip()
    if chat == "ENTER":
        who.clear()
        continue
    elif chat not in who:
        who.add(chat)
        gom += 1
    else:
        continue

print(gom)

    