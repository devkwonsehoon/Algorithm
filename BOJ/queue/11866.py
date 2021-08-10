from collections import deque

n, k = map(int, input().split())
q = deque([])
answer = deque([])

for i in range(1, n+1):
  q.append(i)

print("<", end="")
while q:
  q.rotate(-(k-1))
  print(q.popleft(), end="")
  if q : print(", ", end="")

print(">", end="")