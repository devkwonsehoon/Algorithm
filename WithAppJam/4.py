import sys
input = sys.stdin.readline

for _ in range(int(input())):
  ox = list(input())
  sum = 0
  count = 1

  for idx in ox:

    if idx == "O":
      sum += count
      count += 1
    else: count = 1
      
  print(sum)