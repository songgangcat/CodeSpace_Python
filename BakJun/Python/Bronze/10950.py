#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오
#첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#각 테스트 케이스마다 A+B를 출력한다.

x = int(input())
list_a = []

for i in range(x):
    A, B = map(int, input().split())
    list_a.append(A + B) 

for i in range(x):
    print(list_a[i])



#x = int(input())
#list_a = []

#for i in range(x):
#    A, B = map(int, input().split())
#    list_a += str(A+B)
#     =>이 부분에서 , A+B가 17이면 list에 '1', '7' 로 입력됨 
#       => 요소 추가하는 .append() 사용하기.
#       걍복잡하니까 리스트 요소 추가 = .append()로 암기.
#       => list_a += [A+B]하면 되긴 함.

#for i in range(x):
#    print(list_a[i])