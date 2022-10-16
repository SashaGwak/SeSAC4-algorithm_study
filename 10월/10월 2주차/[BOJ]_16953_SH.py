# 16953 A -> B
# B -> A로 단축하는 가장 빠른 방법을 카운트 한다
# 변환 식이 모두 적용이 안된다면 변환 불가하므로 루프문을 빠르게 종료한다
A, B = map(int, input().split())

ans = 1

while A < B:
    if B == A: # A를 B로 바꾼 경우 
        break

    if B % 2 == 0:  # B 가 짝수인 경우
        B = B // 2 
        ans += 1
    
    elif B % 10 == 1: # B의 일의 자리가 1인 경우
        B = B // 10 
        ans += 1

    # 변환 불가능 할 때 break
    else: 
        ans = -1 
        break

# 변환 끝났을 때 A != B인지 체크 
if B != A: 
    ans = -1

print(ans)