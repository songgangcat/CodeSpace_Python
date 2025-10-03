#예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.
#크로아티아 알파벳	변경
#č	c=
#ć	c-
#dž	dz=
#đ	d-
#lj	lj
#nj	nj
#š	s=
#ž	z=

S = input().strip()
list_a = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]\

for i in list_a:
    S = S.replace(i, "*")

print(len(S))