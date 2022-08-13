# 9012 괄호

T = int(input()) # 입력 데이터의 수를 나타내는 정수 T

for i in range(T): 
    stack = []
    A = input()
    for j in A: 
        if j == '(': # '('가 있으면 '('를 stack에 append함
            stack.append(j)
        elif j == ')': 
            if stack: # ')'가 있으면 stack에 들어간 것을 pop해서 삭제
                stack.pop()
            else:
                print("NO")
                break
    else: # 반복이 완전히 끝나면 실행
        if not stack: # stack(list)가 비어있으면
            print("YES") 
        else:
            print("NO")

# for-else
# if not list