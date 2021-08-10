# 배열을 정렬하는 것은 쉽다. 
# 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

nums = sorted([int(n) for n in input()], reverse=True)
print(*nums, sep="")

# 숏코딩
# print(*sorted(input())[::-1],sep="")
# 리스트 인덱싱 마지막 파라미터를 -1 로 주는 포인트; 
