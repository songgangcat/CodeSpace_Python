#n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input())
total = 0

for i in range(n):
    total += i+1

print(total)

#변수 선언 전 total = 0등으로 초기화 시키는거 잊지 말기

#<GPT 1>
#n = int(input())
#total = 0

#for i in range(1, n+1):
#    total += i

#print(total)

#<GPT 2>
#n = int(input())
#total = n * (n + 1) // 2
#print(total)
