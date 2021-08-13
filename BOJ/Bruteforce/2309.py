
from itertools import combinations as c

lst = [int(input()) for _ in range(9)]
all_lst = list(c(lst, 7))

for i in all_lst:
  if sum(i) == 100:
    print(*sorted(i), sep="\n")
    break

