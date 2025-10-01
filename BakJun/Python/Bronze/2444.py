#예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
#첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

N = int(input())

for i in range(1, N):
    print(" "*(N-i) + "*"*(2*i-1))

print("*"*(2*N-1))

for i in range(N-1, 0, -1):
    print(" "*(N-i) + "*"*(2*i-1))


#<GPT1>
#N = int(input())

#for i in range(1, 2*N):
#    # 위쪽은 1~N, 아래쪽은 N+1~2N-1
#    if i <= N:
#        print(" "*(N-i) + "*"*(2*i-1))
#    else:
#        j = 2*N - i
#        print(" "*(N-j) + "*"*(2*j-1))

#<GPT2>
#N=int(input())
#print('\n'.join([(' '*(N-i)+'*'*(2*i-1)) for i in list(range(1,N))+list(range(N,0,-1))]))

