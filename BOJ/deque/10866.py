# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다.

import sys
input = sys.stdin.readline

from collections import deque

def push_front(x):
  q.appendleft(x)

def push_back(x):
  q.append(x)

def pop_front():
  if not q : print(-1)
  else : print(q.popleft())

def pop_back():
  if not q : print(-1)
  else : print(q.pop())

def size():
  print(len(q))

def empty():
  if not q : print(1)
  else : print(0)

def front():
  if not q : print(-1)
  else: print(q[0])

def back():
  if not q : print(-1)
  else: print(q[-1])

command_count = int(input())
q = deque()

for _ in range(command_count):
  command = input()

  if 'push_front' in command:
    com, x = command.split()
    push_front(int(x))
  
  elif 'push_back' in command:
    com, x = command.split()
    push_back(int(x))
  
  elif 'pop_front' in command:
    pop_front()
  
  elif 'pop_back' in command:
    pop_back()

  elif 'size' in command:
    size()
  
  elif 'empty' in command:
    empty()
  
  elif 'front' in command:
    front()
  
  else:
    back()