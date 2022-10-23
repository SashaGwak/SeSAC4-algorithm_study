# 1541 잃어버린 괄호

# 입력값에서 '-' 기준으로 문자열 분리
s = input().split("-")

# 모든 숫자의 총합을 담기 위한 변수 sum 선언
sum = 0

# 맨 처음 숫자부터 '-'가 나오기 전까지의 숫자들을 각각 분리하고 모두 더하기
for i in s[0].split("+"):
    sum += int(i)

# '-'가 나온 이후의 숫자들을 각각 숫자로 분리하고 모두 빼기
for i in s[1:]:
    for j in i.split("+"):
        sum -= int(j)

# 결과 출력
print(sum)
