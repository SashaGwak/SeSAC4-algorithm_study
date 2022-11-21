from sys import stdin # 시간 초과 방지를 위한 stdin

n, m = map(int, stdin.readline().split()) # n, m: A, B 집합의 원소 개수
a = set(map(int, stdin.readline().split())) # set 자료구조를 이용해 A집합 원소 넣어주고
b = set(map(int, stdin.readline().split())) # B 넣어주고

res = a-b # res는 차집합 넣은 변수

if res:
    print(len(res))
    print(*sorted(list(res))) # *을 붙여주지 않으면 []가 붙은 상태로 출력됨. -붙이면 내림차순 정렬됨.
else:
    print(0)