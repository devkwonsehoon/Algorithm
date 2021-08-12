# 양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다. 

# 예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 
# 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다. 
# 이런식으로 다음과 같은 수열을 만들 수 있다.

# 33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...

nums = set(range(1, 10000))
non_nums = set()

for num in nums:
  for x in str(num):
    num += int(x)
  non_nums.add(num)

result = nums - non_nums
print(*sorted(result), sep="\n")