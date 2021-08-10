# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
import sys
n = int(sys.stdin.readline())

for _ in range(n):
  x, y = map(int, sys.stdin.readline().split(','))
  print(x+y)

# 숏코딩
# for x in [*open(0)][1:]:print(sum(eval(x)))


