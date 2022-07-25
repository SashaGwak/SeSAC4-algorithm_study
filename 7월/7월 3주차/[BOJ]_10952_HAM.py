# A, B = int(input()),split()
# print(0, 0)

# print(A,B)

# split 함수를 제대로 기억하고 있지 않은듯.
# 입력의 마지막에 0 두 개가 들어온다?
# print 함수로 처리하면 안되나?
# 입력은 여러 개의 테스트 케이스로 이뤄져있다?
# B는 10이상이다.

# map 함수

while 1:
    a, b = map(int, input().split())
    if (a == 0 and b == 0) :
        break
    else:
        print(a + b)
