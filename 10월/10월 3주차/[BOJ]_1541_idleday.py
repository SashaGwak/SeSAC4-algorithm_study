# 1541 잃어버린 괄호

# 입력값에서 '-' 기준으로 문자열 분리
s = input().split("-")

# 모든 숫자의 총합을 담기 위한 변수 sum 선언
sum = 0

# 맨 처음부터 '-'가 나오기 전까지의 숫자들을
for i in s[0].split("+"):   # 각각 분리하고
    sum += int(i)           # 모두 더하기

# '-'가 나온 이후의 숫자들을
for i in s[1:]:
    for j in i.split("+"):  # 각각 분리하고
        sum -= int(j)       # 모두 빼기

# 결과 출력
print(sum)
