# 최댓값(2562)
# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수 3, 29, 38, 12, 57, 74, 40, 85, 61이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
import sys
numbers = []

for i in range(0,9):
    n = int(sys.stdin.readline())
    numbers.append(n)
    # numbers.append(int(input())) 으로 작성가능

print(max(numbers))
print(numbers.index(max(numbers)) + 1)
# index는 0부터 시작하므로 1 더해주기