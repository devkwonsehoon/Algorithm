# N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 
# 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.

import heapq as hq
import sys
input = sys.stdin.readline
card = []

n = int(input())

for _ in range(n): card.append(int(input()))
hq.heapify(card)
result = 0

while len(card) != 1:
  x = hq.heappop(card)
  y = hq.heappop(card)
  z = x+y
  result += z

  hq.heappush(card, z)

print(result)


