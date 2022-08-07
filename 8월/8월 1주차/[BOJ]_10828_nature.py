# 10828 스택

import sys # sys 모듈 사용
A = int(sys.stdin.readline()) # input()를 사용하면 시간초과가 발생하기 때문에 사용

Stack = []

for i in range(A): # 명령을 A번 함
    
    S = sys.stdin.readline().split() # push 등을 입력 받을 때 split()해서 입력받음
    
    if S[0] == 'push': # push X : 정수 X를 스택에 넣는 연산
        Stack.append(S[1])
    elif S[0] == 'pop': # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력 
        if len(Stack)>0: 
            print(Stack.pop())
        else:  # 스택에 들어있는 정수가 없는 경우에는 -1을 출력
            print(-1)
    elif S[0] == 'size': # 스택에 들어있는 정수의 개수를 출력
        print(len(Stack))
    elif S[0] == 'empty': 
        if len(Stack) == 0 : # 스택이 비어있으면 1
            print(1)
        else: # 스택이 비어있지 않으면 0
            print(0)
    elif S[0] == 'top': # 스택의 가장 위에 있는 정수를 출력
        if len(Stack) > 0 :
            print(Stack[-1])
        else: # 스택에 들어있는 정수가 없는 경우에는 -1 출력
            print(-1)

# S[0] : 명령어 받기