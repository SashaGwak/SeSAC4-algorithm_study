n, money = map(int, input().split())   
wallet = []				

for i in range(n):			
    coin = int(input())			
    wallet.append(coin)			

wallet.reverse()	

count=0				

for coin in wallet:			
        count = count + money // coin	
        money = money%coin	

print(count)	
