import itertools

num = list(input()) # 숫자 입력받기
arr = list(itertools.permutations(num, len(num))) # 파이썬 라이브러리를 활용해 순열 구하기
arr.sort(reverse=True) # 오름차순 정렬

result = [] # 문자열을 숫자열로 합쳐서 저장할 배열 생성
for a in arr: # arr에서 값을 가져오기
  result.append("".join(a)) # 튜플을 문자열로 합침

idx = result.index("".join(num)) # 숫자가 있는 인덱스 번호를 찾기
print(result[idx-1] if idx != 0 else 0) # 제일 큰 수가 아니라면 현재보다 바로 큰 값을 출력하고 0을 출력한다.