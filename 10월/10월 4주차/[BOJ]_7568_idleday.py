# 7568 덩치
# 완전탐색(Brute-Force Search) : 모든 경우의 수 확인

N = int(input())    # 전체 사람 수
people = []         # 몸무게와 키를 담을 리스트

# 입력값 받기
for _ in range(N):
    # 각 사람의 몸무게와 키를 입력받아 튜플 형태로 리스트에 삽입
    weight, height = map(int, input().split())
    people.append((weight, height))

# 덩치 순위 구하기
for self in people:
    # 덩치 등수 초기값은 1
    rank = 1
    # 리스트의 모든 사람(자신 포함)과 비교
    for other in people:
        # 자신보다 더 큰 덩치의 사람이 있을 경우
        if self[0] < other[0] and self[1] < other[1]:  # (0: 몸무게, 1: 키)
            # 덩치 등수 +1
            rank += 1
    # 자신의 최종 덩치 등수 출력
    print(rank, end=" ")
