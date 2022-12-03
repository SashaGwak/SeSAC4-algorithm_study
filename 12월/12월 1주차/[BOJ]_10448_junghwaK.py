import sys
cnt = 1
arr = []
while 1: 
    if cnt*(cnt+1)//2 > 1000:
        break
    arr.append(cnt*(cnt+1)//2)
    cnt+=1

num = int(sys.stdin.readline())

for i in range(num):
    k = int(sys.stdin.readline())
    bool = False
    for j in range(len(arr)):
        if arr[j] >= K:
            tmp = j
            break
        else:
            tmp = j
    for x in range(len(arr[:tmp])):
        for y in range(x, len(arr[:tmp])):
            for z in range(y, len(arr[:tmp])):
                if K == arr[x]+arr[y]+arr[z]:
                    bool = True
                    break
                if bool:
                    break      
            if bool:
                break
        if bool:
            break
    if bool:
        print(1)
    else:
        print(0)



# num을 입력받기 전 cnt변수를 통해 arr에 공식에 맞는 수들 세팅
# num입력받고 K입력. bool을 False로 세팅
# 미리 입력받은 arr의 수 중에 어디까지 필요한지 걸러내는 작업수행
# 삼중 for문으로 값을 찾을 경우 bool을 True로 변경후 for문 탈출
# bool이 True일 경우 1출력, False일경우 0출력