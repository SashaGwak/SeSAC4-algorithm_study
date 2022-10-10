n = input()
n = sorted(n, reverse=True) 

sum = 0
if '0' not in n:	
    print(-1)
else:
    for i in n:        # 3의 배수인 경우 sum에 더하고
        sum += int(i)
    if sum % 3 != 0 :	# 3의 배수가 아닐 경우
        print(-1)
    else :
        print(''.join(n)) # n 문자열 모두 join 