import sys
input = sys.stdin.readline

nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
s = input()

for num in nums:
    if num in s:
        s = s.replace(s[s.find(num):s.find(num)+len(num)], str(nums.index(num)))

print(int(s))
