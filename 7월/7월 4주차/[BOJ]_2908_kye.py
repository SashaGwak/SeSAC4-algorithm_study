#문제: 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 
#예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
#두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
#입력: 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.
#출력: 첫째 줄에 상수의 대답을 출력한다.

#1. for loop
num1, num2 = map(str, input().split())
reverse_num1 = ''
reverse_num2 = ''

for i in num1 :                               # i 앞으로 수가 쌓인다. 
    reverse_num1 = i + reverse_num1           # 새 문자열 = a + 새 문자열('') 
                                              # 새 문자열 = b + 새 문자열('a') 
                                              # 새 문자열 = c + 새 문자열('ba')
                                              # 새 문자열 = d + 새 문자열('cba')

for i in num2 :
    reverse_num2 = i + reverse_num2

reverse_num1 = int(reverse_num1)
reverse_num2 = int(reverse_num2)


if reverse_num1 > reverse_num2 :
    print(reverse_num1)
else :
    print(reverse_num2)

#2. slice()로 문자열 순서 뒤집기
a, b = map(str, input().split())

a = int(a[::-1])
b = int(b[::-1])

if a > b :
    print(a)
else :
    print(b)

#3.reversed()
a, b = map(str, input().split())
reversed_a = "".join(reversed(a))
reversed_b = "".join(reversed(b))

reversed_a = int(reversed_a)
reversed_b = int(reversed_b)


if reversed_a > reversed_b :
    print(reversed_a)
else :
    print(reversed_b)
