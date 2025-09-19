#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

list_a = [int(input()) for _ in range(9)]

print(max(list_a))
print(list_a.index(max(list_a)) + 1)

#for _ in range(x)
#⇒ _ == 반복은 하지만 변수는 쓰지 않겠다는 의미
#i 써도 차이는 x

#list.index() 함수 
# :list.index(찾을 값, 검색 시작 위치(기본0), 검색 끝낼 위치(기본 리스트 끝)) 
# ⇒ 반환값 = 리스트에서 x가 처음 등장하는 위치
