import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []

for _ in range(n):
    num = int(input())

    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
