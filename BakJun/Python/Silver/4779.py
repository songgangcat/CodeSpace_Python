import sys

def cantor(start, length):
    if length == 1:
        return

    third = length // 3
    mid_start = start + third
    mid_end = start + 2 * third

    for i in range(mid_start, mid_end):
        line[i] = " "

    cantor(start, third)
    cantor(start + 2 * third, third)


for s in sys.stdin:
    s = s.strip()
    if not s:        
        continue
    n = int(s)
    length = 3 ** n
    line = ["-"] * length
    cantor(0, length)
    print("".join(line))
