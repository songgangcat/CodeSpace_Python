#정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
#첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.
#N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

N = int(input())
list_a = []

while True:
    if N == 1:
        break
    for i in range(2, N+1):
        if N % i == 0:
            list_a.append(i)
            N //= i 
            break
        else:
            continue

print('\n'.join(map(str, list_a)))


#<GPT>
#N = int(input())
#i = 2
#while i * i <= N: #루트 N까지만 검사
#    if N % i == 0:
#        print(i)
#        N //= i #작은 수부터 하나씩 모두 체크하고 i 커짐
#    else:
#        i += 1

#if N > 1:
#    print(N)