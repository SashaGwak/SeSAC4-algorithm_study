import sys

n = int(input())

stack = []

for i in range(n):
    a = sys.stdin.readline().split() #split을 한 이유: push를 할 때는 push 1 이런 식으로 띄어쓰기를 하면서 값을 넣기 때문이다. 
    
    if a[0] == "push":
        stack.append(a[1]) #a리스트의 [0]은 push, pop, size등의 명령어가 들어가므로 a[1]에 들어가는 정수를 stack에 넣어주어어 한다. 
        
    elif a[0] == "pop":
        if len(stack) != 0:
            print(stack.pop()) #가장 위에 있는 값이란 가장 마지막에 들어온 값을 말한다. 
        else:
            print("-1")
    
    elif a[0] == "size":
        print(len(stack))
    
    elif a[0] == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
            
    elif a[0] == "top":
        if len(stack) == 0:
            print("-1")
        else: 
            print(stack[len(stack)-1]) #리스트는 0부터 시작하기 때문에 가장위에 있는 정수; 리스트의 가장 마지막 요소를 출력하기 위해서는 요소 개수에 -1을 해주어야 한다. 