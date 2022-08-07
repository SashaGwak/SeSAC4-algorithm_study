import sys
n = int(sys.stdin.readline())  # 주어지는 명령의 수

stack = []
for i in range(n+1):
    # sys.stdin.readline() = input()
    command = sys.stdin.readline().split() # '명령 숫자' 식으로 입력하기 떄문에 split()으로 구분한다.
    
    if command[0]=='push':        # 인덱스[0] == 'push'
        stack.append(command[1])  # 인덱스[1] 자리의 값을 stack 안에 넣는다.
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())    # pop(): 리스트의 마지막 요소를 돌려주고 그 요소를 제거한다.
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
