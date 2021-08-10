# 예제 2의 경우를 시뮬레이션 해보면,

# [1]
# [1,3]
# [1,3,5]
# [1,3,5,4]
# [1,3,5] (0을 불렀기 때문에 최근의 수를 지운다)
# [1,3] (0을 불렀기 때문에 그 다음 최근의 수를 지운다)
# [1,3,7]
# [1,3] (0을 불렀기 때문에 최근의 수를 지운다)
# [1] (0을 불렀기 때문에 그 다음 최근의 수를 지운다)
# [1,6]

line = int(input())
numList = []

for _ in range(line):
  num = int(input())
  if num != 0: numList.append(num)
  else: numList.pop()

answer = sum(numList)
print(answer)

# 숏코딩
# z=[]
# for s in open(0):
#  if a:=int(s):z+=[a]
#  else:z.pop()
# print(sum(z[1:]))