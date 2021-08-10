# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
input = sys.stdin.readline
from collections import deque as dq

def push(x):
  q.append(x)

def pop():
  if not q : print(-1)
  else: print(q.popleft())

def size():
  print(len(q))

def empty():
  if not q : print(1)
  else : print(0)

def front():
  if not q : print(-1)
  else : print(q[0])

def back():
  if not q : print(-1)
  else : print(q[-1])


n = int(input())
q = dq([])

for _ in range(n):
  command = input()

  if 'push' in command:
    com, num = command.split()
    push(int(num))
  
  elif 'pop' in command:
    pop()
  
  elif 'size' in command:
    size()
  
  elif 'empty' in command:
    empty()
  
  elif 'front' in command:
    front()
  
  else:
    back() 
