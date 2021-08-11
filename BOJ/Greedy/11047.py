
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
result = 0

for _ in range(n):
  coins.append(int(input()))

coins.sort(reverse=True)

for coin in coins:
  if k == 0: break

  result += k//coin
  k%=coin

print(result)  
