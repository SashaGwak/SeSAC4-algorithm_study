# 1874 스택 수열

N = int(input()) 
count = 1
S = [] # 스택
R = [] # 결과값
noMessage = True # 모르겠음

for i in range(N):
    x = int(input())

    while count <= x: 
        S.append(count) # 스택에는 숫자가 쌓이고
        R.append("+") # 결과값엔 "+"가 쌓임
        count += 1

    if S[-1] == x: # 마지막 숫자가 입력한 숫자랑 같다면 
        S.pop() # 스택에 마지막에 쌓인 숫자 제거됨
        R.append("-") # 결과값엔 "-"가 쌓임
    else:
        noMessage = False 

if noMessage == False: 
    print("NO")
else: # noMessage가 아직도 True라면 
    for i in R: # 결과값에 있는 요소들 출력됨
        print(i)