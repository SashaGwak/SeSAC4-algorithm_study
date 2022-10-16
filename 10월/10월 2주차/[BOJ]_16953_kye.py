# b에서 a를 만들어 해결한다.
a, b = map(int, input().split())
cnt = 1
while True:
    if b == a:
        break
    elif (b % 2 != 0 and b % 10 != 1) or (b < a):
        cnt = -1
        break
    else:
        if b % 10 == 1:
            b //= 10
            cnt += 1
        else:
            b //= 2
            cnt += 1
            
print(cnt)

#while문을 통해 과정을 반복한다.
#만약 a == b면 while문을 break 한다.
#만약 b가 2로 나누어 떨어지지 않으며 b의 마지막 자리의 숫자가 1이 아니거나 b가 a보다 작다면 b에서 a를 만들 수 없는 경우(a에서 b를 만들 수 없는 경우)이므로 -1을 출력한다.
#만약 b의 마지막 자리의 숫자가 1이면 b에서 1을 제거한다.
#만약 b가 2로 나누어 떨어지면 2로 나눈다.