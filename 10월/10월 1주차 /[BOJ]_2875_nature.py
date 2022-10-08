# 2875 대회 or 인턴

# 여학생 수 N, 남학생 수 M, 인턴쉽에 참여해야하는 인원 K
N, M, K = map(int, input().split(()))

result = 0

# N(여자)이 두명 이상, M(남자)가 1명 이상, N + M(여자 + 남자)가 K(인턴쉽에 참여해야하는 인원) + 3명보다 많을 때 반복문 
while N >= 2 and M >= 1 and N + M >= K + 3:
    N -= 2 # 여자 두명 빼주고
    M -= 1 # 남자 한명 빼주고 
    result += 1 # 결과 값에 1 더해줌

print(result)