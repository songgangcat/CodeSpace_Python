#

X = int(input())

line = 0
count = 0

while X > count:
    line += 1
    count += line  
    # X가 count보다 작을 때, X의 line을 찾기 위해 계속 더함
    #count = 해당 line의 마지막 번호 / line = 대각선 줄번호(즉, 해당 대각선에 몇개 요소가 있는지를 표현)


a = X - (count - line)
#count - line => 해당 줄의 마지막 번호에서 해당 줄의 요소 개수만큼 차감 -> 전줄의 마지막 요소 번호가 됨

if line % 2 == 0:
    print(str(a)+"/"+str(line-a+1))
else:
    print(str(line-a+1)+"/"+str(a))