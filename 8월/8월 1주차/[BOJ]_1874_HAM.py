n = int(input())
count = 1
stack = []
result = []
temp = True #  flag 처리. 근데 flag 처리 왜 하는건지 아직 정확하게 이해하지 못했음.


for i in range(n) :
    x = int(input())

    while count < x :
        stack.append(count)
        result.append("+")
        count += 1
        
    if stack[-1] == x :
        stack.pop()
        result.append("-")
    else :
        temp = False
         # 이거 뭐임 어쩌라고?

if temp == False:
    print("NO")

else:
    print("\n".join(result)) # join?