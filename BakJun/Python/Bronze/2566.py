#<그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.
#예를 들어, 다음과 같이 81개의 수가 주어지면
#첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다. 주어지는 수는 100보다 작은 자연수 또는 0이다.
#첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다. 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.
B = []
ma = []

for _ in range(9):
    A = list(map(int, input().split()))
    B.append(A)
    ma.append(max(A))

print(max(ma))
print(ma.index(max(ma)) + 1 , B[ma.index(max(ma))].index(max(ma)) + 1)

#<GPT> - 이중 for문으로 정확히 탐색
#B = [list(map(int, input().split())) for _ in range(9)]

#max_num = -1
#row = col = 0

#for i in range(9):
#    for j in range(9):
#        if B[i][j] > max_num:
#            max_num = B[i][j]
#            row, col = i + 1, j + 1

#print(max_num)
#print(row, col)
