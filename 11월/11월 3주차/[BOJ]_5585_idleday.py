# 5585 거스름돈
# 그리디 알고리즘

change = 1000 - int(input())        # 전체 거스름돈
coins = [500, 100, 50, 10, 5, 1]    # 큰 값부터 내림차순 정렬한 coins 배열

count = 0                            # 동전 총 개수

# 큰 액수의 동전부터 거슬러주면서 최소한의 동전 사용 
for coin in coins: 
    # 동전 총 개수 count에 change을 각 coin로 나눈 몫 더해주기
    count += change // coin
    # change는 이전 단계의 나머지가 된다
    change %= coin

# count 출력
print(count)