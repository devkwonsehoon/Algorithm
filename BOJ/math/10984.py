# 2
# 4
# 3 4.3
# 2 2.0
# 4 0.0
# 2 4.0
# 3
# 4 0.0
# 4 0.0
# 3 0.0

import sys
input = sys.stdin.readline

test_case = int(input())
credit_sum = 0
grade_sum = 0

for _ in range(test_case):
  credit_sum = 0
  grade_sum = 0
  
  n = int(input())
  
  for _ in range(n):
    credit, grade = input().split()
    credit_sum += int(credit)
    grade_sum += (float(grade) * int(credit))

  print(credit_sum, round(grade_sum/credit_sum, 1))