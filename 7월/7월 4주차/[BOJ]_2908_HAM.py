'''
상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 
예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
'''

# 숫자 거꾸로 출력해주는 함수 -> list 역순으로 넣기.
# 두 수의 대소 비교해주는 함수

a, b = input().split() # 왜 int로 한 번에 못 감쌀까?
a = int(a[::-1]) # [::-1] 역순 처리 해줌.
b = int(b[::-1])

if a > b :
    print(a)
else : # else도 : 넣어줘야. 
    print(b)


