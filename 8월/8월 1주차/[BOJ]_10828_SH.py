# 스택 10828
import sys

N = int(sys.stdin.readline())
# 스택 생성
stack = []

for i in range(N):
    # 명령어 받기
    command = sys.stdin.readline().split()

    # push X :  정수 X를 스택에 넣는 연산
    if command[0] == 'push': 
        stack.append(command[1])

    # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력
    elif command[0] == 'pop':
        # 스택에 들어있는 정수가 없는 경우 -1을 출력
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    # 스택에 들어있는 정수의 개수를 출력
    elif command[0] == 'size': 
        print(len(stack))
    
    # 스택이 비어있으면 1 아니면 0을 출력
    elif command[0] == 'empty': 
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    # 스택의 가장 위에 있는 정수를 출력
    elif command[0] == 'top': 
        # 스택에 들어있는 정수가 없는 경우 -1을 출력
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
