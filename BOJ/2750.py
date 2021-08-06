import sys
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
  num = int(input())
  nums.append(num)

print(*sorted(nums), sep="\n")