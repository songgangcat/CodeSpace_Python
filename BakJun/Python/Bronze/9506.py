#완전수 구하기

while True:
    n = int(input())
    list_a = []

    if n == -1:
        break

    for i in range(1, n):
        if n%i == 0:
            list_a.append(i)

    S = " + ".join(list(map(str,list_a)))
    
    if sum(list_a) == n:
        print(n, "=", S) 
        continue
    else:
        print(n, "is NOT perfect.")
