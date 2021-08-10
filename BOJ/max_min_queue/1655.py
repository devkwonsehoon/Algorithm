import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    
    heapq.heappush(heap, num)
    
    if n % 2 == 0: 
      print(heapq.heappop(heap))
    else:
      print(heapq.heappop(heap))
