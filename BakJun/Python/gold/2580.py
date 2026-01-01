import sys
input = sys.stdin.readline


def sudoku(k): #K번째 0을 바꿔보자.
    if k == len(blanks): #0에서 바꾼 숫자가 k개면 출력하고 종료
        for i in board:
            print(*i)
        return True 
        #마지막에 딱 완성되어서 출력했을 때, True가 return되면, if문을 통해 연쇄적으로 True가 return되면서 다른 계산들 없이 깔끔하게 종료된다
    
    r, c = blanks[k] #k번째 0의 인덱스
    b = (r//3)*3 + (c//3) # k번째 0의 박스 인덱스

    for i in range(1, 10): #1~9까지 같은 행, 열, box 검사
        
        if not row[r][i] and not col[c][i] and not box[b][i]: #3가지 조건을 만족하면
            row[r][i] = col[c][i] = box[b][i] = True
            board[r][c] = i #해당 숫자 넣기


            if sudoku(k+1): #검사하면서 호출 같이 됨
                  return True #재귀 -> 실패하면 다음 i 돌아야 하니, for 문 안에 두기
 
            

            row[r][i] = col[c][i] = box[b][i] = False #False로 되돌리고 돌아가기
            board[r][c] = 0 #다시 0으로 바꾸고 돌아가기
    
    return False #for문 9개 다 실패했을때 False



board = [list(map(int, input().split())) for _ in range(9)]
blanks = [] #0인 값들의 위치 인덱스가 (r, c) 형태로 들어감

row = [[False]*10 for _ in range(9)] #row[0][1] == False면 1열에는 "1"이 없다.
col = [[False]*10 for _ in range(9)]
box = [[False]*10 for _ in range(9)]


for r in range(9):
    for c in range(9):
        n = board[r][c]
        if n == 0:
            blanks.append((r, c)) #0일때, 위치 인덱스 넣기
        else: #숫자가 있을때 row, col, box에 n True로 변환
            row[r][n] = True
            col[c][n] = True
            box_idx = (r//3)*3 + (c//3) #박스 번호 계산
            box[box_idx][n] = True


sudoku(0) #1에서 시작