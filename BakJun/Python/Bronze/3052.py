#두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
#수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
#첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.
#첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.


list_a = [int(input()) for _ in range(10)]
list_b = []

for i in range(10):
    list_b.append(list_a[i]%42)

print(len(set(list_b)))

#<gpt>
#remainders = set()

#for _ in range(10):
#    num = int(input())
#    remainders.add(num % 42)

#print(len(remainders))


#set() => 집합(리스트같은거임), 중복값 자동 제거, len()등 사용 가능