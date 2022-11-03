# 과자를 충분히 나눠줄 수 있는지 체크하는 함수
def check(x):
    total = 0
 
    for i in li:
        total += i // x
    # 과자의 수가 조카의 수보다 많으면 참
    return total >= n
 
n, m = map(int, input().split())
li = list(map(int, input().split()))
 
# 이진 탐색
s = 0
e = 10000000000
 
while s <= e:
    # 만약 같은 길이의 과자를 나눠줄 수 없다면,
    # s + e가 0이라는 말이므로, zerodivision error가 나오기 전에
    # 0을 출력하고 함수를 종료한다.
    if (s + e) == 0:
        print(0)
        exit()
 
    mid = (s + e) // 2
 
    if check(mid):
        ans = mid
        s = mid + 1
    else:
        e = mid - 1
 
print(ans)
