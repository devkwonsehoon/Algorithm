# 널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 
# 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
# x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다

import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)