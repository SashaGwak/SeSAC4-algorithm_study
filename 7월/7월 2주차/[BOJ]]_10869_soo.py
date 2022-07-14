# 방법1
a, b = input().split()
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)//int(b))
print(int(a)%int(b))


# 방법2
a, b = map(int, input().split())
print(a+b, a-b, a*b, a//b, a%b, sep='\n')