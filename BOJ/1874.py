# 1부터 n까지에 수에 대해 차례로 [push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop] 연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.
import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = []
count = 0
isCorrect = True

for _ in range(n):
  x = int(input())
  
  while count < x: # 첫 숫자만큼 push 해줘야하므로 ex) x=4 -> push 1,2,3,4 
    count += 1  
    stack.append(count)
    answer.append("+")
  
  if stack[-1] == x: # 4 , 3 pop
    stack.pop()
    answer.append("-")
  else:
    isCorrect = False
    break

if isCorrect == False: print("NO")
else: print("\n".join(answer))