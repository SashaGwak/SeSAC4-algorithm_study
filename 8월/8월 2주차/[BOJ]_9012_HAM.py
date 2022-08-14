# 괄호
# 괄호 문자열은 ()만으로 구성된 문자열.
# 괄호가 짝이 맞으면 yes, 아니면 no

# first try
import sys
input = sys.stdin.readline

T = int(input())
A = []
for i in range(T) :
    A.append(input())

for i in range(T) :
    num1 = A[i].count('(')
    num2 = A[i].count(')')
    if num1 == num2 :
        print ('yes')
    else :
        print ("no")   # 문자열 갯수 세는 법?

# 2nd try.. 런타임에러(type, attribute)겪고, 틀렸습니다 겪고 옴.
# 다른 문제 풀이법 발견. 갯수세서 비교하지 말고 (일땐 더해주고 )일땐 빼주고
# 최종 sum이 0이 되도록

T = int(input())

for _ in range(T):
   check = input()
   Is = list(check)
   sum = 0

   for i in Is :
    if i == "(":
        sum += 1
    elif i == ")":
        sum -= 1
    if sum < 0 :
        print("no")
        break

    if sum > 0 :
        print("no")
    elif sum == 0 :
        print('yes')

# 다른 코드 3
N = int(input())

for _ in range(N) :
    count = 0
    stk = list(input())

    for i in range(len(stk)) :
        if stk[i] == "(" :
            count += 1
        else :
            count -= 1
        # 나갈 구멍을 만들어주려고..?
        # 이 라인이 왜 추가되는걸까? count>0일때도 실패
        # len(stk) 지나면 어차피 나와지잖아.
        if count < 0 : 
            break

    if count == 0 :
        print("yes")
    else :
        print("no")