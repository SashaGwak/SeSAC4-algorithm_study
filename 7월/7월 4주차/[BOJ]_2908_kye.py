
#1. 런타임에러

num1 = input()
num2 = input()
reverse_num1 = ''
reverse_num2 = ''

for i in num1 :
    reverse_num1 = i + reverse_num1

for i in num2 :
    reverse_num2 = i + reverse_num2

if reverse_num1 > reverse_num2 :
    print(reverse_num1)
else:
    print(reverse_num2)
