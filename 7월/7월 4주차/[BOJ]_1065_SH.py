# 한수(1065)
# 문제 
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
N = int(input());
hansu = 0

for n in range(1, N + 1):
    if n <= 99:
        hansu += 1
    
    else: 
        nums = list((N))
        if nums[0] - num[1] == nums[1] - nums[2]:
            hansu += 1
print(hansu)