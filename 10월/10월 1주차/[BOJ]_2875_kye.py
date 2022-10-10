n, m, k = map(int, input().split()) # n 여학생, m 남학생 k 인턴십 학생 수
count = 0

while n+m >= k+3 and n>=2 and m>=1 : 
  n -= 2
  m -= 1
  count += 1

print(count)