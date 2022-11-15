N = int(input()) #1 입력값 
result = 0 #2 N과 비교할 변수
for i in range(1, N+1) :  
    A = list(map(int, str(i))) #3 map함수로 처리
    result = i + sum(A) #4
    if result == N : #5
        print(i)
        break

    if i==N: #6
        print(0)