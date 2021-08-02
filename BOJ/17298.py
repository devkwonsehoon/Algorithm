# 입력 #
# 4
# 3 5 2 7

# 출력 #
# 5 7 7 -1


import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
answer = [-1] * n
stack = []

for i in range(n):
  while stack and num_list[stack[-1]] < num_list[i]:
    answer[stack.pop()] = num_list[i]
  stack.append(i)
print(*answer)

