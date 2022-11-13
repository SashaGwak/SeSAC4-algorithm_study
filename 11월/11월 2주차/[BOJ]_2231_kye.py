n = int(input())
result = 0
for i in range(1,n):
    lst = list(map(int,str(i)))

    result = i+sum(lst)
    if result ==n:
        print(i)
        break 
    if i==n:
        print(0)