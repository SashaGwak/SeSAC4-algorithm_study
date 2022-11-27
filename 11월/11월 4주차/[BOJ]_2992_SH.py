# 2992 크면서 작은수
# 결국 다음 순열이 존재하는 지 확인
from itertools import permutations 
n = input()
permu = (sorted(set(map(lambda x: ''.join(x), permutations(n, len(n))))))
# 가장 큰 수가 n과 같다면 0을 출력
print(0) if permu[-1] == n else print(permu[permu.index(n) + 1])

# 순열(permutaion)
# 순열 공식 => nPr = n!/(n-r)!
'''
from itertools import permutations
a = [1,2,3]
permute = permutations(a,2)
print(list(permute))

의 결과는
[(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]
'''
