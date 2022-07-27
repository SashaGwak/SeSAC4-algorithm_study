a, b = map(str,input().split())

a = int(a[::-1])
b = int(b[::-1])

if int(a) > int(b):
    print(a)
else : 
    print(b)