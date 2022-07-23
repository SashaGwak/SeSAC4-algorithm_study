#2577(숫자의 개수)

A = int(input())
B = int(input())
C = int(input())

multi = list(str(A * B * C))

for i in range(10):
    print(multi.count(str(i)))


# list(str())
#   str -> 문자열로 변환
#   list -> 각각의 문자를 요소로 가지는 리스트로 변환 

# count()
#   매칭되는 갯수를 리턴해줌
