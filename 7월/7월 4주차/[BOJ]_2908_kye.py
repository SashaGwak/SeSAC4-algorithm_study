#1. for loop
num1, num2 = map(str, input().split())
reverse_num1 = ''
reverse_num2 = ''

for i in num1 :
    reverse_num1 = i + reverse_num1

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
