# 9095 1, 2, 3 더하기

N = int(input())

def S(N):
    if N == 1:
        return(1)
    elif N == 2:
        return(2)
    elif N == 3:
        return(4)
    else:
        return S(N-1) + S(N-2) + S(N-3)

for i in range(N):
    result = int(input())
    print(S(result))

# N이 1일 때 1 => 1개
# N이 2일 때 1 + 1, 2 => 2개
# N이 3일 때 1 + 1 + 1, 1 + 2, 2 + 1, 3 => 4개
# N이 4일 때 1 + 1 + 1 + 1, 1 + 1 + 2 ... => 7개
# N이 4일 떄 개수 = N이 1일 때 개수 + N이 2일 때 개수 + N이 3일 때 개수
# 즉, S(N) = S(N-1) + S(N-2) + S(N-3)
