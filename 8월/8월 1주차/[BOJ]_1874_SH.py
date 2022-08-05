# 스택 수열(1874)
import sys
n = int(input())

count = 1
stack = []   # stack 담을 리스트 
result = []  # 출력값 담을 리스트
flag = True  

for _ in range(n):
    num = int(sys.stdin.readline())

    # 입력되는 값이 count(1부터 시작~) 보다 같거나 크다면 append
    while count <= num:
        stack.append(count)
        # append할때마다 + 출력할 수 있도록 추가
        result.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        flag = False 

if not flag: 
    print('NO')
else:
    for i in result:
        print(i)