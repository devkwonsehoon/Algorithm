import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
lst = []

q = deque([i+1 for i in range(N)])

while len(q) != 0:
  q.rotate(-K) # 그냥 K일시 오른쪽으로 회전해서 구하고자하는 값이랑 다른 값이 나옴
  lst.append(q.pop())

# list join 내장함수를 이용해서 붙이는데 lst안에는 숫자가 들어있기 때문에 str로 mapping
print('<' + ', '.join(map(str, lst)) + '>')




