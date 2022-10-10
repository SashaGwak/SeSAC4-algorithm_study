n = input() # 3의 배수인지 판별할 숫자.
n = sorted(n, reverse=True) # 미르코는 큰 수를 좋아함.

sum = 0
if '0' not in n:	# 우선은 input의 디폴트인 string으로 받았기에 '0' 문자로 적음
    print(-1) # 30의 배수여야 돼서 -1 출력
else:
    for i in n: # 각 자리 수 더해서 3의 배수 판별
        sum += int(i)
    if sum % 3 != 0 :	# 3의 배수 아닐 경우
        print(-1) 
    else :
        print(''.join(n)) # join : 리스트의 문자열 합쳐서 출력하기.