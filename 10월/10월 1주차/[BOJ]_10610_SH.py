# 30(10610번)
# 3의 배수가 되기 위한 조건 -> 모든 자릿수의 합이 3의 배수가 되면 된다 
# 또한 30의 배수이므로 숫자 내에 0이없다면 탈락 
n = input()
n = sorted(n, reverse=True)
# n = ['8', '8', '7', '5', '5', '4', '2', '0']
sum = 0

if '0' not in n: 
    print(-1)
else: 
    for i in n: 
        sum += int(i)
    if sum % 3 != 0: 
        print(-1)
    else: 
        print(''.join(n))