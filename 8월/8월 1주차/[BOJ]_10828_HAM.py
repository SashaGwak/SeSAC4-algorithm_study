# 스택
# 정수를 저장하는 스택을 구현한 후, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오

# list로 스택 구현.
# if 문으로 만들어보자.
# n = int(input())
# box = []
# if 1 <= n <= 10000 :

import sys # sys 모듈 불러오기.

n = int(sys.stdin.readline()) # 몇 번 입력받을건지
stack = [] # 스택 만들기.

def push(x): # 각각의 명령 정의
    stack.append(x)

def pop():
    if(len(stack)==0):
        print(-1)
    else:
        print(stack.pop()) # pop () :인덱스를 생략한 경우 마지막 값을 취득하고 삭제.

def size():
    print(len(stack))

def empty():
    if(len(stack) == 0) :
        print(1)
    else :
        print(0)

def top():
    if(len(stack)==0):
        print(-1)
    else :
        print(-1)

for i in range(n) :
    command = sys.stdin.readline().split()
    
    if (command[0] == 'push'):
        push(command[1])
    elif (command[0] == 'pop'):
        pop()
    elif (command[0] == 'size'):
        size()
    elif (command[0] == 'empty'):
        empty()
    elif (command[0] == 'top'):
        top()