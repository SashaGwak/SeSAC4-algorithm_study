a = int(input())
han = 0

for i in range(1, a+1):
    if i >= 100:
        i = str(i)
        if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
            han += 1
    else :
        han += 1
 
print(han)