import sys
input = sys.stdin.readline

lst = list(set([input().rstrip() for _ in range(int(input()))]))

lst.sort()
lst.sort(key=len)

print(*lst, sep="\n")