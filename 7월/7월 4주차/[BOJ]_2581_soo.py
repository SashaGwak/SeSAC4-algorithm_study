m = int(input())
n = int(input())
list = []

for i in range(m, n+1):
    count = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0: 
                count += 1
                break
        if count == 0:
            list.append(i)

if len(list) == 0 :
    print(-1)

else:
    print(sum(list))
    print(min(list))