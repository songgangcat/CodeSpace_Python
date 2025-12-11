#N**2의 별 사각형을 만들기
#N 정중앙 1/9를 공백으로 치환

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def draw(x, y, n):
    # n이 1이면 더 쪼갤 필요 없음 → 별 하나 출력
    if n == 1:
        star[x][y] = '*'
        return
    
    size = n // 3
    for i in range(3):
        for j in range(3):
            # 가운데(1,1) 블록은 공백
            if i == 1 and j == 1: #if문으로 가운데는 공백으로 치환, 나머지는 재귀
                for a in range(x + size, x + 2 * size):
                    for b in range(y + size, y + 2 * size):
                        star[a][b] = ' '
            else:
                draw(x + i * size, y + j * size, size)

N = int(input())
star = [[' ' for _ in range(N)] for _ in range(N)]

draw(0, 0, N)

for row in star:
    print(''.join(row))


#<성결 정답>

#N/3으로 각 범위 재귀 
#N = 3이면 return

#import sys
#input = sys.stdin.readline

#def pat(start_x, start_y, x):
#    if x < 3:
#        return
#    unit = x // 3
#    for i in range(start_y + unit, start_y + 2*unit):
#        for j in range(start_x + unit, start_x + 2*unit):
#           star[i][j] = ' ' # 중간 1/9 공백으로 치환
#    for i in range(start_x, start_x + x, unit):
#        for j in range(start_y, start_y + x, unit):
#            pat(i, j, unit)
#            
#    return
    
    
    

#N = int(input())
#star = []
#for _ in range(N):
#    star.append(["*" for _ in range(N)]) # N**2 별 사각형 만들기
#pat(0, 0, N)

#for row in star:
#    print(''.join(row))

