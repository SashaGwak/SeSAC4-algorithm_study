a = int(input())
b = int(input())
c = int(input())
# why? 문제에서 a, b, c함수를 서로 다른 줄에서 받으라고 하였으므로 a, b, c = map(int, input().split())로 쓰면 안된다.

num = list(str(a*b*c)) # str: 문자열 형태로 객체를 변환시켜주는 것

for i in range(10):
    print(num.count(str(i))) # 위쪽에서 str로 숫자를 문자열로 변환시켜주었기 때문에 여기서도 str로 변환시켜주지 않는다면 문자열 리스트에서 숫자열 문자를 찾는것이 된다. 