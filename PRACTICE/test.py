# 코테 꼼수
import sys
input = sys.stdin.readline
# 더 빨리 읽는다 => 시간 단축 개꿀

n, k = map(int, input().split()) # 종류와 합 입력받기 
coins = [] # 동전 종류 담을 리스트
for _ in range(n): coins.append(int(input())) # 동전 종류 입력받기

coins.sort(reverse=True) # 내림차순 정렬

print(coins)
result = 0

# k = 10000
for coin in coins: # 제일 큰 가치의 동전부터 반복
      
      print("coin", coin)
      result += k//coin # 합을 해당 동전으로 나눴을 때 몫을 count에 더한다!
      
      print("result", result)
      k = k % coin # 그리고 나머지 남은 돈을 K에 담아준다
      
      print("k",k)

print(result)













# money = 1000 - int(input()) 
# coin = [500, 100, 50, 10, 5, 1] # 가지고 있는 동전을 미리 저장
# count = 0
# for i in coin:
#     count += money // i # 나눈 몫만 누적 합
#     money %= i # 나눈 나머지만 업데이트
# print(count)