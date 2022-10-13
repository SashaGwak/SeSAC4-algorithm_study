before, after = map(int,input().split())

count = 1

while after != before: #A와 B가 같지 않다면 -> 계속 연산을 진행해야 함
    count += 1 #연산의 횟수 증가
    if after == before: #만일 A와 B가 같다면 break
        break
    tmp = after #B의 값을 tmp에 저장
    if after % 10 == 1: #10으로 나눈 값이 1이라면 -> 1의 자리 : 1
        after //= 10 #10으로 나눈 몫을 저장
    elif after % 2 == 0 : #2로 나눠진다면
        after //= 2  #2로 나눈 몫을 저장
    if tmp == after: #만일 연산 전의 값과 현재 값이 동일하다면 연산을 진행할 수 없는 값
        count = -1 
        break
        
        
print(count)