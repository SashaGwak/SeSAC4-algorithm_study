import itertools # 효율적인 반복을 위한 함수

X = list(input())

# itertools.permutations은 반복 가능 객체 중에서 r개를 선택한 순열을 반환하는 함수
L = list(itertools.permutations(X, len(X)))
L.sort(reverse=True) # 오름차순 정렬

result = [] # 문자열을 숫자열로 합쳐서 저장할 배열 생성

for i in L:
    result.append("".join(i)) # 투플을 문자열로 합침

I = result.index("".join(X)) # 숫자가 있는 인덱스 번호 찾기

print(result[I-1] if I != 0 else 0) # 제일 큰 수가 아니라면 현재보다 바로 큰 값을 출력하고 0을 출력