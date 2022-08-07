import sys
N = int(sys.stdin.readline())
stack, result, find = [], [], True

now = 1
for i in range(N): 
    num = int(sys.stdin.readline())
    # 숫자 1부터 num 이하까지 스택에 입력
    while now <= num:
        stack.append(now)
        result.append("+")
        now += 1
        
    # 스택 꺼내기
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    #찾는 스택이 없을 경우
    else:
        find = False

if not find:
    print("NO")
else:
    for i in result:
        print(i)
    
    
