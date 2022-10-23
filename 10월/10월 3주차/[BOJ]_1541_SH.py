# 잃어버린 괄호(1541)
# 괄호를 쳐서 이 식의 값을 최소로 만들기
arr = input().split('-')
# -를 기준으로 괄호 치기 ex) 55 - (50+40)

# 결과값 저장
result = 0

# +으로 나누어 더해주기(-앞의 부분)
for i in arr[0].split('+'):
    result += int(i)
for i in arr[1:]:
    # - 뒤부분 -해주기
    for j in i.split('+'):
        result -= int(j)
        
print(result)