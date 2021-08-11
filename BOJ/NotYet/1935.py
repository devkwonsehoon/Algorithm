# 5
# ABC*+DE/-
# 1
# 2
# 3
# 4
# 5
# 해결중
import sys
input = sys.stdin.readline

n = int(input())
s = input()
opr = '+-*/'
nums = []

for _ in range(n):
  nums.append(int(input()))

for x in s:
  
  if x == '+':
    a = nums.pop()
    b = nums.pop()
    nums.append(a+b)
  
  elif x == '-':
    a = nums.pop()
    b = nums.pop()
    nums.append(a-b)

  elif x == '*':
    a = nums.pop()
    b = nums.pop()
    nums.append(a*b)
  
  elif x == '/':
    a = nums.pop()
    b = nums.pop()
    nums.append(a/b)