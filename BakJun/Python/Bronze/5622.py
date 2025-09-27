#https://u.acmicpc.net/9c88dd24-3a4c-4a09-bc50-e6496958214d/Screen%20Shot%202021-06-16%20at%2012.48.39%20AM.png
#상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
#전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
#숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

S = input().strip()
time = 0

for ch in S:
    if ch in "ABC": time += 3
    elif ch in "DEF": time += 4
    elif ch in "GHI": time += 5
    elif ch in "JKL": time += 6
    elif ch in "MNO": time += 7
    elif ch in "PQRS": time += 8
    elif ch in "TUV": time += 9
    elif ch in "WXYZ": time += 10

print(time)
 

